<!-- Auto-generated guidance for AI coding agents. Keep concise and actionable. -->
# Copilot instructions for this repository

Purpose: Quickly orient an AI coding agent to be productive in this repository and to safely modify code or add files. Update this file if you learn project-specific conventions.

**Repository Snapshot**:
- **Top-level:** contains a single file named `Multilingual Chatbot` (currently empty).
- **No obvious language manifests found:** there is no `package.json`, `requirements.txt`, `pyproject.toml`, `Dockerfile`, or `README.md` in the repo root.

**Exploration Checklist (first actions)**
- **List files:** run a recursive directory listing to locate source, manifests, and tests:
  - PowerShell: `Get-ChildItem -Recurse -Force | Where-Object { $_.PSIsContainer -eq $false }`
- **Search for common manifests:** look for `package.json`, `requirements.txt`, `pyproject.toml`, `setup.py`, `Dockerfile`, `README.md`, `src/`, `tests/`.
- **Open README(s):** if present, follow any developer setup instructions before changing code.

**When nothing obvious exists**
- **Ask the repo owner** for the intended language, framework, entrypoint, and test commands before making substantive changes.
- Prefer creating a minimal scaffold (e.g., `README.md`, `src/`, `tests/`) only after confirming the intended stack.

**Common run / test patterns (examples — adapt after discovery)**
- **Python (if found):** `python -m venv .venv; .\\.venv\\Scripts\\Activate.ps1; pip install -r requirements.txt; pytest`
- **Node (if found):** `npm install; npm test` (or `pnpm install; pnpm test` if `pnpm-lock.yaml` present)

**Merging policy for existing agent docs**
- If `.github/copilot-instructions.md` or `AGENT.md` exists, preserve any project-specific commands and examples; merge new guidance only to add missing, verifiable facts.
- Cite concrete file paths when recommending changes (e.g., "Update `src/app.py` to..."), not speculative filenames.

**What to look for in code to determine architecture**
- **Service boundaries:** search for folders named `api`, `server`, `worker`, `functions`, or `services`.
- **Data flow / models:** look for `models/`, `schemas/`, `db/`, or ORM configs (`alembic/`, `migrations/`).
- **Integration points:** look for `Dockerfile`, `.env`, `config/`, cloud infra files (`terraform/`, `azure-pipelines.yml`, `github/workflows/`).

**Safety & edits**
- Do not assume behavior without tests or a README. Add tests with the same style found in the repo (pytest, jest, etc.).
- When adding files, update `README.md` with the minimal instructions you used to verify changes.

**Examples from this repo**
- There are currently no discoverable build or test files. Before implementing features, ask: "Which language/framework should I use? Do you have an existing code snapshot or starter template?"

If anything here is unclear or you can provide the intended language/framework, I will update this file with concrete commands and examples.
