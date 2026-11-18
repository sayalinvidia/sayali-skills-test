# nvidia-demo — plugin card

| | |
|---|---|
| Owner | Demo Product team (sync trial) |
| Source | `sayalinvidia/sayali-skills-test`, directory `plugin/` |
| Version | 1.0.0 |
| Bundled skills | `jetson-set-target`, `jetson-print-bsp-info` (each independently signed) |
| MCP servers | `nvidia-demo-docs` — local stdio, `mcp/demo_docs_server.py`, deps in `mcp/requirements.txt` |
| Hooks | `SessionStart` banner, `hooks/hooks.json` |
| Network access | none; the MCP server reads bundled files only |
| Boundaries | Demo content. Signature is a structural fixture for the fork trial, not an NVIDIA production signature. |
