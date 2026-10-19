# Building Beautiful PPTX Decks by Generating OOXML Directly

Generate the `.pptx` as raw Office Open XML with Python's standard library, then look at every slide by rendering the real file to images with LibreOffice. This guide is topic-agnostic: the method is the same whether the deck is a performance review, a design proposal, or a research summary. It replaces two things that do not work well: the `python-pptx` package (often unavailable behind a locked network) and a LaTeX/TikZ mock-up (it renders a proxy, not the real deck).

## Why Generate OOXML Directly

Three reasons decide the approach.

1. A `.pptx` is a ZIP of XML parts, so Python's built-in `zipfile` and string formatting are enough; no third-party package is needed.
2. `python-pptx` frequently cannot be installed in a corporate sandbox (blocked index, SSL interception), so depending on it is fragile.
3. A TikZ or LaTeX mock-up renders a PDF that only looks like the deck. It verifies the wrong artifact, and translating its layout back to native shapes reintroduces every difference. Render the real `.pptx` instead.

## Dependencies, and Why Each Is Needed

Install three tools; a fourth is optional.

- Python 3 (standard library only): writes the `.pptx`. `zipfile` packs the parts; plain f-strings produce the XML.
- LibreOffice (`soffice`): converts the real `.pptx` to PDF without a GUI. It reads the actual OOXML and lays it out close to PowerPoint, so it exposes defects that XML checks cannot see, such as text overflow, wrapping, and a missing background.
- Poppler (`pdftocairo` or `pdftoppm`): converts that PDF to one PNG per slide, which is what you actually read.
- Optional: the brand's fonts installed locally (check with `fc-list`). You need them only to render and embed the real typeface.

## The See-It Feedback Loop Is the Core Discipline

You cannot improve what you cannot see, so render and look after every change.

- Render: `soffice --headless --convert-to pdf --outdir OUT deck.pptx`, then `pdftocairo -png -r 120 OUT/deck.pdf OUT/slide`.
- Read the PNGs. Judge spacing, overflow, hierarchy, and color against the brand.
- Make a watcher that re-renders on file change, so the loop is hands-free once started.

Four gotchas waste the most time:

1. A freshly installed LibreOffice (Homebrew cask) carries a macOS quarantine flag that makes the headless convert fail silently. Clear it once: `xattr -dr com.apple.quarantine /Applications/LibreOffice.app`.
2. A command sandbox can block the helper socket `soffice` opens for conversion. If convert exits non-zero with no output, run `soffice` outside the sandbox (the user's own terminal, or the watcher).
3. Point `soffice` at a writable profile with `-env:UserInstallation=file:///tmp/...` when the default profile location is not writable.
4. Write the `.pptx` atomically: build to `deck.pptx.tmp`, then `os.replace` it onto `deck.pptx`, so the watcher never reads a half-written file.

## The OOXML Skeleton

A minimal deck needs these parts inside the ZIP.

- `[Content_Types].xml` and `_rels/.rels`
- `ppt/presentation.xml` and its `.rels`
- `ppt/theme/theme1.xml`
- `ppt/slideMasters/slideMaster1.xml` and its `.rels`
- `ppt/slideLayouts/slideLayout1.xml` and its `.rels`
- `ppt/slides/slideN.xml` and a `.rels` per slide, plus `ppt/media/` and `ppt/fonts/`

Keep these facts nearby.

- Units are EMU, at 914400 per inch. A 16:9 slide is 12192000 by 6858000.
- `<p:bg>` must be the first child of `<p:cSld>`, before `<p:spTree>`. Placed inside `<p:spTree>` it is ignored, and the background silently disappears.
- Hyperlinks are per-slide relationships: each `<a:hlinkClick r:id="...">` needs a matching external relationship in that slide's `.rels`.
- Reset the shape-id counter at the start of each slide; ids must be unique within a slide.
- Embed fonts through `<p:embeddedFontLst>` plus `fntdata` parts so the deck keeps its typeface on another machine.

## Validate Structurally on Every Build

Automated checks catch what the eye cannot, and the eye catches what they cannot. Run both.

- ZIP integrity (`testzip`).
- XML well-formedness of every part.
- Geometry bounds: no shape sits off the slide.
- Hyperlink relationships: every `rId` used in a slide is defined in its `.rels`.

## Match a Brand Without Guessing

Read the design system from a reference template rather than inventing one.

- Unzip the reference `.pptx` and read its theme colors (`clrScheme`), embedded fonts, logo image, footer pattern, and any reusable shape geometry.
- Reuse the real embedded fonts and the real logo image. Use the brand's installed fonts when they are present.

## Content Structure Is One Pyramid

Arrange slides so the argument is visible, following the Minto order.

- Cover, then a governing slide, then one divider per main point, then content slides.
- The governing slide states the single thesis in one sentence and lists the main points, five or fewer.
- Each divider restates one main point. The content slides under it advance that point in a stated order (time, structure, or importance).

## Slide Headers Are Complete Sentences

Write every header as a sentence that states the slide's conclusion, not a topic label. "Gemma matches GPT quality at two to three times the speed, so we chose it" tells the reader the point; "Model comparison" makes them hunt for it.

## Content Slide Anatomy

Give every content slide the same parts, so the deck reads as one system.

- A title sentence, at most two lines.
- A thin accent rule under the title.
- A context line (date and source channel).
- Left column: three to five bullets, one claim each, in readable type.
- Right column: one result callout holding a single headline number.
- A sources line at the bottom.

## Formatting That Reads as One System

Hold the visual language constant.

- Use the brand palette and fonts, one separator style, and generous whitespace.
- Set code in monospace: variable names, function names, file names, and parameters. Mark them with backticks in the source data and render those spans in a monospace face. Choose Courier New, because it is present in PowerPoint on Windows and Mac and in Google Slides, so it never substitutes. Adapt the code color to the background (a dark accent on light slides, a light accent on dark cards).
- Keep type readable. Body text around 14 point or larger, titles larger. When text does not fit, cut words rather than shrink the font.

## Richness Without Clutter

Add detail that earns its place.

- One headline metric per slide, in the result callout.
- Native diagrams for process steps or future work, drawn as boxes, arrows, and chips, so they stay editable and sharp. Avoid pasted images for anything you can draw.
- Real hyperlinks to the backing report, sheet, or pull request, both inline in the sources line and as a button.

## Accuracy and Provenance for Decision Decks

When a deck informs a decision or a review, verify before you assert.

- Check facts against ground truth, not chat history: git log and blame, trackers, and the files themselves. What shipped often differs from what was proposed, including renamed functions and dropped features.
- Attribute authorship precisely. Credit teammates for their own pull requests, and separate "proposed" from "shipped" and "deferred."
- Derive timelines from commit dates (actual effort), not from first-mention-to-merge spans, which overstate duration.
- Put a verifiable source on every claim.

## A Reusable Generator Shape

Keep the generator small and split content from rendering.

- Helpers: a text box with backtick-to-monospace parsing, a rectangle, an ellipse, a line, a bullet list, a result callout, a flow step, builders for cover and divider and content slides, a footer, a logo, and a per-slide hyperlink registry.
- Data: hold each slide's title, context, bullets, result, links, and optional diagram in plain data structures. Rendering stays in the helpers, so one command rebuilds the whole deck.

## Checklist Before Sending

Confirm all of the following.

- You viewed the rendered PNGs, not only the validation output.
- Every header is a sentence, and the pyramid holds from cover to last slide.
- Every claim is sourced and checked against ground truth.
- Code is in monospace, fonts are readable, and no em dashes remain.
- Links resolve, fonts are embedded, and the file opens in PowerPoint and Google Slides.
