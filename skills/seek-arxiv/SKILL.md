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

The clone downloads about 1.1 GB and occupies 4.3 GB. In one test, it took 6.4 minutes. With an index, the checkout needs about 10 GB of disk. Run the commands below from `$ARXIVDB_DIR`, or from anywhere after the install in step 2.

## Prepare the index

1. Fetch the latest papers with `git pull --ff-only`. Skip this step when the machine is offline.
2. Install the packages once with `python -m pip install -e .`, preferably inside a virtual environment. Writing `python -m pip` installs into the same Python that runs the commands below. The install adds the packages `bm25s`, `PyStemmer`, `numpy` and `scipy`.
3. Build the index when `index/meta.json` is missing, or when a search prints `warning: data/ changed after this index was built`. Choose the backend first:
   - If `python -c "import bm25s, Stemmer"` succeeds and the machine has at least 16 GB of memory, run `python -m arxivdb build`. In one test, the build took 5.3 minutes and 5.7 GB of disk, with a peak memory footprint of 12.6 GB.
   - Otherwise, run `python -m arxivdb build --backend sqlite`. It needs only the Python standard library. In the same test, it took 3 minutes and 5.6 GB of disk, with under 50 MB of memory.

If bm25s is missing, `build` stops before it touches the existing index. An outdated index still answers searches, but it misses the papers changed since the build. `search` uses whichever backend `build` ran last.

## Search

```bash
python -m arxivdb search "retrieval augmented generation" -n 20
python -m arxivdb search "direct preference optimization" --years 2023- --cat cs.CL --cat cs.LG
python -m arxivdb search "graph neural network molecular property" --cat cs --json
```

- `-n 20` sets the number of results. The default is 10.
- `--years 2020-2023` keeps papers by the submission year of their first version, which the tool reads from the arXiv ID. The forms `2024`, `2022-` and `-2015` also work.
- `--cat cs.CL` keeps papers listed in a category, including papers cross-listed there from another primary category. A whole archive such as `cs`, `math` or `hep-th` also works, and repeating the option accepts papers in any of the given categories.
- `--json` prints one JSON record per line with the full abstract and the score. The default output shortens abstracts to 300 characters.

A search usually takes about 1 second with bm25s. With SQLite, it usually takes under 1 second, and up to about 5 seconds when the query holds only very common words. When nothing matches, `search` prints nothing.

## Read full records

`python -m arxivdb get 2005.11401 2106.09685v2` prints the full records as JSON lines. It reads `data/` directly, so it works before the index exists. It drops a version suffix such as `v2`, and it prints nothing for an ID it does not hold.

## Write queries the backend can match

Both backends match words, reduced to their stems, so `models` also matches `model`. Neither matches synonyms. Use the words that papers put in titles and abstracts, and for a topic, run several short queries with different wording and merge the results.

With bm25s, the default backend:

- A paper scores higher for each query word it contains, and rare words count more. The tool drops 33 common words such as `the`, `of`, `is` and `for`.
- Write an acronym together with its expansion, such as `RAG retrieval augmented generation`.
- To find a known paper, search for its exact title with `-n 20`. Titles count three times in the ranking. In a test with 24 well-known papers, the exact title put the paper in the top 10 for 21 of them, and first for 12.

With SQLite, a paper must contain every query word, including `the` and `of`. Use two to four distinctive words per query. A full title works less well. In one test, the LoRA paper ranked 20th for its own title with SQLite, against 6th with bm25s.

## Cite papers

Cite a paper by its title, first author, year and `https://arxiv.org/abs/<id>`. Before an ID goes into a document, confirm it with `get`, and treat empty output as an unknown ID.

## Coverage limits

- The data covers arXiv alone, from January 2011. Older papers, and papers published elsewhere, are missing.
- Each record holds the title, authors, abstract and categories. For full text, venue or citation counts, use another source.
- Papers announced after the last daily update, or after your last `git pull`, are missing.
