# Project-03 — Multilingual Chatbot (Python)

This repository contains a small Python prototype of a multilingual chatbot (Streamlit UI + backend client). The remote `backend.py` uses the `groq` client and expects an API key to be provided via environment variables.

## Prerequisites
- Python 3.10+ (Windows) or the version used to create the venv
- PowerShell (Windows)

## Setup (PowerShell)

1. Create and activate a virtual environment (use the `py` launcher if available):

```powershell
py -3 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r Requirements.txt
```

3. Create a `.env` file from `.env.example` and set your `GROQ_API_KEY`:

```powershell
copy .env.example .env
# then edit .env with your secret (do NOT commit .env)
```

4. Run the UI (Streamlit):

```powershell
streamlit run ui.py
```

## Notes
- `backend.py` reads the Groq API key from the `GROQ_API_KEY` environment variable and raises an error if it is missing.
- Do not commit secrets. Use `.env` (ignored by git) or a secure secret manager.
- If you accidentally committed a secret, rotate/revoke the key immediately.

## Files
- `ui.py` — Streamlit UI
- `backend.py` — Chat client wrapper (uses `GROQ_API_KEY` env var)
- `Requirements.txt` — Python dependencies

If you want, I can also add a `CONTRIBUTING.md` or CI workflow next.
