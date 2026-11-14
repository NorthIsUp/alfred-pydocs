"""Print docs.python.org's Sphinx inventory (objects.inv) as JSON rows: name, role, url."""

import json
import re
import urllib.request
import zlib

URL = "https://docs.python.org/3/objects.inv"
# Every documented Python object; std:label and friends are page sections, not objects.
ROLES = {"py:class", "py:function", "py:method", "py:module", "py:exception", "py:data", "py:attribute"}
LINE = re.compile(r"(?P<name>.+?)\s+(?P<role>\S+:\S+)\s+-?\d+\s+(?P<uri>\S*)\s+(?P<display>.*)")

raw = urllib.request.urlopen(URL, timeout=60).read()
# Four plain header lines, then the zlib-compressed entries.
header = raw.split(b"\n", 4)
# Link the exact release (3.15), so URLs don't drift when /3/ moves on.
version = header[2].decode().removeprefix("# Version:").strip() or "3"
body = zlib.decompress(header[4]).decode()
rows = []
for line in body.splitlines():
    if (m := LINE.fullmatch(line)) and m["role"] in ROLES:
        uri = m["uri"].replace("$", m["name"]) if m["uri"].endswith("$") else m["uri"]
        url = f"https://docs.python.org/{version}/{uri}"
        rows.append({"name": m["name"], "role": m["role"].removeprefix("py:"), "url": url})
print(json.dumps(rows))
