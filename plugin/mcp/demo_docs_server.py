#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Minimal stdio MCP server exposing the bundled skills' SKILL.md files as
resources. DEMO only — exists to show an MCP server travelling inside a
mirrored plugin."""
import json, os, sys
from pathlib import Path

ROOT = Path(os.environ.get("DEMO_DOCS_ROOT", Path(__file__).resolve().parent.parent / "skills"))

def resources():
    return [{"uri": f"skill://{p.parent.name}", "name": p.parent.name, "mimeType": "text/markdown"}
            for p in sorted(ROOT.glob("*/SKILL.md"))]

def handle(req):
    m, i = req.get("method"), req.get("id")
    if m == "initialize":
        return {"jsonrpc": "2.0", "id": i, "result": {"protocolVersion": "2025-06-18", "capabilities": {"resources": {}},
                "serverInfo": {"name": "nvidia-demo-docs", "version": "1.0.0"}}}
    if m == "resources/list":
        return {"jsonrpc": "2.0", "id": i, "result": {"resources": resources()}}
    if m == "resources/read":
        name = req["params"]["uri"].split("://", 1)[1]
        text = (ROOT / name / "SKILL.md").read_text()
        return {"jsonrpc": "2.0", "id": i, "result": {"contents": [{"uri": req["params"]["uri"], "mimeType": "text/markdown", "text": text}]}}
    if i is not None:
        return {"jsonrpc": "2.0", "id": i, "error": {"code": -32601, "message": f"unknown method {m}"}}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    resp = handle(json.loads(line))
    if resp:
        sys.stdout.write(json.dumps(resp) + "\n"); sys.stdout.flush()
