# 📚 Study Assistant

An AI-powered study assistant built with Streamlit and Groq (LLaMA 3.3).

## Features

- 💬 **Chat** — Ask about any topic with customizable tone, detail level, and education level
- 📝 **Quiz** — Auto-generate multiple choice quizzes on any subject
- 🃏 **Flashcards** — Generate flashcards for quick revision

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/study-assistant.git
cd study-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key
Create the file `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
Get a free key at [console.groq.com](https://console.groq.com)

### 4. Run the app
```bash
streamlit run main.py
```

## Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo
4. Add `GROQ_API_KEY` in the Secrets section
5. Deploy!

## Tech Stack

- [Streamlit](https://streamlit.io) — UI framework
- [Groq](https://groq.com) — Free LLM API
- [LLaMA 3.3 70B](https://groq.com) — AI model
