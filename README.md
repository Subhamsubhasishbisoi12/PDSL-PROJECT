# 🌍 Multilingual Chatbot

A multilingual conversational AI built with Python, Streamlit, and Groq's LLaMA 3.3 model.

## Features

- Supports English, Spanish, French, German, Hindi, Japanese, Odia, and Arabic
- Uses `llama-3.3-70b-versatile` through Groq for fast inference
- Maintains multiple conversations in the Streamlit session
- Uses environment variables for API-key security

## Run locally

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .\.venv\Scripts\Activate.ps1
pip install -r Requirements.txt
cp .env.example .env  # Windows: copy .env.example .env
# Add GROQ_API_KEY to .env
streamlit run ui.py
```

## Screenshots

Add 2–3 application screenshots under `screenshots/` and reference them here:

<!-- ![Chat interface](screenshots/chat-interface.png) -->
<!-- ![Language selector](screenshots/language-selector.png) -->
<!-- ![Conversation history](screenshots/conversation-history.png) -->

## Security

`.env`, virtual environments, Python caches, and SSH keys are excluded by `.gitignore`. If a credential has ever been committed, revoke it and issue a replacement; deleting the current file does not remove it from Git history.

## Deployment

Deploy from Streamlit Community Cloud and add the resulting app URL here after deployment. Do not put the Groq key in the repository; configure `GROQ_API_KEY` in Streamlit Secrets.

## Structure

- `ui.py` — Streamlit interface
- `backend.py` — Groq client and chat logic
- `Requirements.txt` — dependencies
- `.env.example` — safe configuration template
