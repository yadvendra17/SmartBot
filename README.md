# SmartBot 🤖

A context-aware Python chatbot with both a command-line interface and a Tkinter GUI. Built using NLP techniques for fuzzy intent matching, SmartBot understands natural language variations and responds to a range of conversational and informational queries.

---

## Features

- **Intent recognition** — keyword matching with fuzzy similarity scoring via `difflib`
- **NLP preprocessing** — tokenisation and text cleaning using NLTK
- **Dual interface** — run as a terminal chatbot or a desktop GUI application
- **Extensible** — add new intents and responses with minimal changes

---

## Project Structure

```
smartbot/
├── smart_chatbot.py       # CLI version
├── smart_chatbot_gui.py   # GUI version (Tkinter)
├── requirements.txt
└── .gitignore
```

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/yadvendra/smartbot.git
cd smartbot
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the chatbot**

Terminal version:
```bash
python smart_chatbot.py
```

GUI version:
```bash
python smart_chatbot_gui.py
```

---

## Supported Intents

| Intent | Example Input |
|---|---|
| Greeting | "Hi", "Hello", "Hey" |
| Feeling | "How are you?" |
| Name | "What is your name?" |
| Creator | "Who made you?" |
| Joke | "Tell me a joke" |
| Time | "What time is it?" |
| Working hours | "What are your office hours?" |
| Location | "Where is your office?" |
| Contact | "How do I contact support?" |
| Exit | "Bye", "Goodbye" |

---

## Tech Stack

`Python` &nbsp; `NLTK` &nbsp; `difflib` &nbsp; `Tkinter`

---

## Author

**Yadvendra** — IT Student | [GitHub](https://github.com/yadvendra17) · [LinkedIn](https://linkedin.com/in/yadvendra)
