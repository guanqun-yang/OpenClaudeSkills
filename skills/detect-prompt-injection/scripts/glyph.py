#!/usr/bin/env python3
"""Detect hidden PDF text by comparing glyph-level extraction (PyMuPDF) with
metadata-respecting extraction (pdftotext). Text present only in pdftotext
output is hidden/injected."""

import subprocess
import sys
import fitz  # PyMuPDF


def find_zero_width_text(pdf_path: str) -> list[str]:
    """Find text lines where most glyphs have zero-width bounding boxes."""
    doc = fitz.open(pdf_path)
    hidden_lines = []
    for page in doc:
        blocks = page.get_text("rawdict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                total_chars = 0
                zero_width_chars = 0
                line_text_parts = []
                for span in line.get("spans", []):
                    chars = span.get("chars", [])
                    for c in chars:
                        bbox = c["bbox"]
                        w = bbox[2] - bbox[0]
                        total_chars += 1
                        if w == 0.0:
                            zero_width_chars += 1
                    line_text_parts.append("".join(c["c"] for c in chars))
                line_text = "".join(line_text_parts).strip()
                if total_chars > 5 and zero_width_chars / total_chars > 0.5 and line_text:
                    hidden_lines.append(line_text)
    doc.close()
    return hidden_lines


def verify_with_pdftotext(pdf_path: str, hidden_lines: list[str]) -> list[str]:
    """Cross-check that hidden lines appear in pdftotext output."""
    result = subprocess.run(
        ["pdftotext", pdf_path, "-"],
        capture_output=True, text=True, check=True,
    )
    pdftotext_out = result.stdout
    confirmed = []
    for line in hidden_lines:
        if line[:40] in pdftotext_out:
            confirmed.append(line)
    return confirmed


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    hidden_lines = find_zero_width_text(pdf_path)
    confirmed = verify_with_pdftotext(pdf_path, hidden_lines)

    if confirmed:
        print(f"[!] Found {len(confirmed)} hidden text block(s) with zero-width glyphs:\n")
        for i, text in enumerate(confirmed, 1):
            print(f"  Block {i}: {text[:120]}{'...' if len(text) > 120 else ''}")
        print()
        sys.exit(1)
    elif hidden_lines:
        print(f"[!] Found {len(hidden_lines)} suspicious zero-width text block(s) (not confirmed by pdftotext):\n")
        for i, text in enumerate(hidden_lines, 1):
            print(f"  Block {i}: {text[:120]}{'...' if len(text) > 120 else ''}")
        print()
        sys.exit(1)
    else:
        print("[OK] No hidden text detected — all glyphs have normal dimensions.")
        sys.exit(0)


if __name__ == "__main__":
    main()
