# vra-test-app

> [!WARNING]
> **Deliberately vulnerable.** This repository exists to exercise
> [VRA+](https://github.com/gboie/vra) remediation end to end. Do not deploy it.
> The "secrets" in it are made up.

What's inside, and what VRA+ is expected to do with it:

| Area | Planted issue | Expected VRA+ outcome |
|---|---|---|
| `requirements.txt` | Old Flask, requests, urllib3, Jinja2 | Upgraded in the PR, verified by `pytest` and the Docker build |
| `requirements.txt` | Werkzeug 2.2 — fixes need 3.x, which breaks Flask 2.2 | Draft PR: needs a human (upgrade Flask too) |
| `requirements.txt` | PyJWT 1.7 — 2.x returns `str`, a test expects `bytes` | Draft PR: needs a human |
| `app/` | `subprocess` with `shell=True`, TLS verification disabled | Semgrep rule fixes in the PR (flagged for review) |
| `web/` | Old `lodash` | Upgraded in `package.json` + `package-lock.json`, verified by `npm test` |
| `Dockerfile` | Root user, `ADD`, port 22, `MAINTAINER`, lone `apt-get update` | Dockerfile fixes in the PR, verified by `docker build` |
| `Dockerfile.tools` | Untagged base image | Pinned to a digest |
| `app/settings.py`, `tests/` | Hardcoded credentials | **Not patched** — an issue listing them with rotation steps |

## Run

```bash
pip install -r requirements.txt pytest && pytest -q
(cd web && npm ci && npm test)
docker build -t vra-test-app .
```
