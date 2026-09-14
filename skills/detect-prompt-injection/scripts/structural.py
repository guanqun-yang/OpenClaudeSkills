#!/usr/bin/env python3
"""Detect hidden ActualText in PDF accessibility structures using pikepdf."""

import sys
import pikepdf


def scan_for_actual_text(pdf_path: str) -> list[str]:
    """Scan PDF content streams for /ActualText entries and return hidden texts."""
    hidden_texts = []
    pdf = pikepdf.open(pdf_path)
    for page in pdf.pages:
        raw = page.get("/Contents")
        if raw is None:
            continue
        streams = list(raw) if isinstance(raw, pikepdf.Array) else [raw]
        for stream_obj in streams:
            if isinstance(stream_obj, pikepdf.objects.Object) and hasattr(stream_obj, 'objgen'):
                stream_obj = pdf.get_object(stream_obj.objgen)
            data = bytes(stream_obj).decode("latin-1")
            for marker in ["/ActualText"]:
                idx = 0
                while True:
                    idx = data.find(marker, idx)
                    if idx == -1:
                        break
                    paren_start = data.find("(", idx)
                    if paren_start == -1:
                        idx += len(marker)
                        continue
                    depth = 0
                    paren_end = paren_start
                    for i in range(paren_start, len(data)):
                        if data[i] == "(" and (i == 0 or data[i - 1] != "\\"):
                            depth += 1
                        elif data[i] == ")" and (i == 0 or data[i - 1] != "\\"):
                            depth -= 1
                            if depth == 0:
                                paren_end = i
                                break
                    text = data[paren_start + 1 : paren_end]
                    if text.strip():
                        hidden_texts.append(text)
                    idx = paren_end + 1
    pdf.close()
    return hidden_texts


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    hidden = scan_for_actual_text(pdf_path)

    if hidden:
        print(f"[!] Found {len(hidden)} hidden ActualText block(s):\n")
        for i, text in enumerate(hidden, 1):
            print(f"  Block {i}: {text[:120]}{'...' if len(text) > 120 else ''}")
        print()
        sys.exit(1)
    else:
        print("[OK] No hidden ActualText found.")
        sys.exit(0)


if __name__ == "__main__":
    main()
