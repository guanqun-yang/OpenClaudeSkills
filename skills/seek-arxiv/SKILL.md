---
name: seek-arxiv
description: Search the titles, authors and abstracts of arXiv papers submitted since 2011 on the local machine with the ArxivDB command-line tool. Use when the user asks to find, identify or cite arXiv papers, or to collect related work on a topic.
---

# seek-arxiv

[ArxivDB](https://github.com/guanqun-yang/ArxivDB) stores the title, authors, abstract and categories of arXiv papers submitted since January 2011, as JSON Lines files in a git repository. A GitHub workflow adds new and revised papers daily at 06:00 UTC. The ArxivDB command-line tool ranks papers with BM25, a keyword-ranking formula, and works offline once the repository is cloned.

## Locate the checkout

```bash
ARXIVDB_DIR="${ARXIVDB_DIR:-$HOME/ArxivDB}"
test -d "$ARXIVDB_DIR/data" || git clone --depth 1 https://github.com/guanqun-yang/ArxivDB "$ARXIVDB_DIR"
cd "$ARXIVDB_DIR"
```

The clone downloads about CLONE_SIZE. Run the commands below from `$ARXIVDB_DIR`.

## Prepare the index

1. Fetch the latest papers with `git pull --ff-only`. Skip this step when the machine is offline.
2. Build the index when `index/meta.json` is missing, or when a search prints `warning: index is from data of ...`:

   ```bash
   pip install -e .              # first time only: installs bm25s, PyStemmer, numpy and scipy
   python -m arxivdb build       # BUILD_TIME, peak memory about BUILD_MEMORY
   ```

3. If pip cannot install packages, or the machine has less memory than the build needs, run `python -m arxivdb build --backend sqlite` instead. The SQLite backend needs only the Python standard library and builds in BUILD_TIME_SQLITE with little memory. It returns a paper only when the paper contains every query word, so give it fewer words per query.

## Search

```bash
python -m arxivdb search "retrieval augmented generation" -n 20
python -m arxivdb search "direct preference optimization" --years 2023- --cat cs.CL --cat cs.LG
python -m arxivdb search "graph neural network molecular property" --cat cs --json
```

- `-n 20` sets the number of results. The default is 10.
- `--years 2020-2023` keeps papers by the submission year of their first version, which the tool reads from the arXiv ID. The forms `2024`, `2022-` and `-2015` also work.
- `--cat cs.CL` keeps papers in one category. A whole archive such as `cs`, `math` or `hep-th` also works, and repeating the option accepts papers in any of the given categories.
- `--json` prints one JSON record per line with the full abstract. The default output shortens abstracts to 300 characters.

A search usually takes SEARCH_TIME, most of it spent loading the index. It uses the backend that `build` ran last.

## Read full records

`python -m arxivdb get 2005.11401 2106.09685v2` prints the full records as JSON lines. It reads `data/` directly, so it works before the index exists.

## Write queries that BM25 can match

bm25s, the library behind the default backend, scores a paper by the query words it contains, and gives rare words more weight. It matches words, so a synonym the paper does not use earns nothing.

- Use the words that papers put in titles and abstracts. Write an acronym together with its expansion, such as `RAG retrieval augmented generation`.
- For a topic, run several short queries with different wording, and merge the results.
- The tool ignores common words such as `the`, `of` and `all`, and it reduces words to their stems, so `models` also matches `model`.
- To find a known paper, search for its exact title. Titles count three times in the ranking. In a test with 24 well-known papers, the exact title put the paper in the top 10 for 21 of them, and first for 12.

## Cite papers

Cite a paper by its title, first author, year and `https://arxiv.org/abs/<id>`. Before an ID goes into a document, confirm it with `get`.

## Coverage limits

- The data covers arXiv alone, from January 2011. Older papers, and papers published elsewhere, are missing.
- Each record holds the title, authors, abstract and categories. For full text, venue or citation counts, use another source.
- Papers announced after the last daily update, or after your last `git pull`, are missing.
