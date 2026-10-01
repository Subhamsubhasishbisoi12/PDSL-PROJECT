# 🌍 Multilingual Chatbot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-red?style=flat-square)
![Groq LLM](https://img.shields.io/badge/Groq-LLaMA%203.3-orange?style=flat-square)

A fast, intelligent multilingual conversational AI built with **Python**, **Streamlit**, and **Groq's LLaMA 3.3** model. Chat naturally in 8+ languages with a modern, intuitive interface.

## ✨ Features

- 🗣️ **8+ Language Support** — English, Spanish, French, German, Hindi, Japanese, Odia, Arabic
- ⚡ **Fast LLM Inference** — Powered by Groq's LLaMA-3.3-70b-versatile (500+ tokens/sec)
- 💾 **Multi-Conversation Support** — Browse and resume previous chats from the sidebar
- 🎨 **Clean Modern UI** — Built with Streamlit for responsive, user-friendly experience
- 🔐 **Secure by Design** — API keys stored in `.env` (never committed to git)

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Groq API Key (free tier: [console.groq.com](https://console.groq.com/keys))

### Setup (Linux/macOS)
```bash
# Clone the repository
git clone https://github.com/Subhamsubhasishbisoi12/multilingual-chatbot.git
cd multilingual-chatbot

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r Requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
nano .env

# Run the app
streamlit run ui.py
```

### Setup (Windows PowerShell)
```powershell
# Create and activate virtual environment
py -3 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r Requirements.txt

# Configure API key
copy .env.example .env
# Edit .env with your GROQ_API_KEY (use Notepad or your editor)

# Run the app
streamlit run ui.py
```

The app will open at `http://localhost:8501`

## 📸 Screenshots

*Add screenshots here after deployment:*
- Main chat interface with language selector
- Conversation history sidebar
- Multi-language example

## 🌐 Live Demo

*Deploy on Streamlit Community Cloud:*
1. Push to GitHub (ensure `.env` is in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub account and select this repo
4. Set `GROQ_API_KEY` in Secrets section
5. Deploy!

**Live App:** *(Coming soon)* `https://multilingual-chatbot.streamlit.app`

## 📁 Project Structure

```
multilingual-chatbot/
├── ui.py                 # Streamlit frontend interface
├── backend.py            # Groq LLM client wrapper
├── Requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git exclusions (secrets, caches)
└── README.md             # This file
```

## 🔧 How It Works

**backend.py**: Wraps Groq API client and manages multilingual prompting
```python
from backend import MultilingualChatbot
bot = MultilingualChatbot()
response = bot.chat("Hola", language="Spanish")
```

**ui.py**: Streamlit UI with:
- Language selector (8 languages)
- Real-time chat interface
- Previous conversation browser
- Session state management

## 🔐 Security

⚠️ **Never commit secrets to git:**
- `.env` is gitignored — store `GROQ_API_KEY` here
- Private keys, passwords, and API credentials must never be added to version control
- If a secret is accidentally committed, revoke it immediately and regenerate a new one

## 📊 Model & Performance

- **Model**: LLaMA 3.3 70B Versatile (via Groq)
- **Temperature**: 0.7 (balanced creativity vs. consistency)
- **Max Tokens**: 512 per response
- **Speed**: Groq delivers 500+ tokens/second
- **Context**: Full conversation history maintained per session

## 📋 Dependencies

```
groq>=0.4.0
streamlit>=1.20.0
python-dotenv>=1.0.0
```

See `Requirements.txt` for exact pinned versions.

## 🛠️ Development

### Add a New Language

Edit `ui.py` lines 16–19:
```python
language = st.selectbox("Language", [
    "English", "Spanish", "French", "German",
    "Hindi", "Japanese", "Odia", "Arabic",
    "YOUR_LANGUAGE_HERE"  # Add new language
])
```

### Run Tests Locally
```bash
python -c "from backend import MultilingualChatbot; bot = MultilingualChatbot(); print(bot.chat('Hi'))"
```

## 🤝 Contributing

Contributions welcome! Fork this repo and submit a pull request.

## 📝 License

MIT License — See LICENSE file for details

## 👤 Author

**Subham Bisoi**  
[GitHub](https://github.com/Subhamsubhasishbisoi12) · [Email](mailto:bisoisubhamsubhasish@gmail.com)

---

**Built with ❤️ using Python, Streamlit, and Groq LLaMA**
