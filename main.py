#!/usr/bin/env python3
"""news-image-20261124 v4 entry: publish the poster as /output/entry.png.

The poster itself is a fixed asset (entry.png, drawn for this entry); this
program's job is to prove the asset is a whole, in-limits PNG and to copy
it, byte for byte, to the output directory. It uses only the standard
library, takes no input, makes no network call, and always writes the
same bytes, so two runs produce an identical file.

Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import struct
import sys
import zlib
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
MAX_BYTES = 1_048_576          # competition limit: 1 MiB
MAX_SIDE = 1024                # competition limit: 1024 px per side
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_chunks(data):
    """Yield (type, payload) for every PNG chunk, checking structure."""
    if data[:8] != PNG_MAGIC:
        fail("entry.png is not a PNG (bad magic)")
    pos = 8
    seen_ihdr = False
    seen_iend = False
    while pos < len(data):
        if pos + 8 > len(data):
            fail("truncated chunk header")
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(data):
            fail(f"truncated {ctype.decode('ascii', 'replace')} chunk")
        payload = data[pos + 8:pos + 8 + length]
        (stored_crc,) = struct.unpack(">I", data[pos + 8 + length:end])
        if zlib.crc32(ctype + payload) & 0xFFFFFFFF != stored_crc:
            fail(f"bad CRC in {ctype.decode('ascii', 'replace')} chunk")
        if ctype == b"IHDR":
            seen_ihdr = True
            width, height = struct.unpack(">II", payload[:8])
            if width > MAX_SIDE or height > MAX_SIDE:
                fail(f"image is {width}x{height}, over the {MAX_SIDE}px limit")
        if ctype == b"IEND":
            seen_iend = True
            if end != len(data):
                fail("trailing bytes after IEND")
        yield ctype, payload
        pos = end
    if not seen_ihdr:
        fail("no IHDR chunk")
    if not seen_iend:
        fail("no IEND chunk")


def main():
    if not SOURCE.is_file():
        fail(f"missing {SOURCE.name} next to main.py")
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        fail(f"entry.png is {len(data)} bytes, over the {MAX_BYTES} limit")
    chunks = list(read_chunks(data))
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    width, height = struct.unpack(">II", chunks[0][1][:8])
    print(f"wrote {len(data)} bytes ({width}x{height} PNG, "
          f"{len(chunks)} chunks) to {target}")


if __name__ == "__main__":
    main()
