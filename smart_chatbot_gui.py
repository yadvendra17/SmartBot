import tkinter as tk
from tkinter import scrolledtext
import string
import nltk
from datetime import datetime

nltk.download('punkt')

# Define keyword-based responses
responses = {
    "greeting": ["hi", "hello", "hey"],
    "feeling": ["how are you", "how r u", "how are you doing"],
    "creator": ["who made you", "who created you", "who built you"],
    "joke": ["joke", "funny", "tell me a joke"],
    "time": ["time", "what time", "current time"],
    "name": ["your name", "what is your name", "who are you"],
    "bye": ["bye", "goodbye", "see you"],
    "hours": ["working hours", "office hours", "what are your working hours"],
    "location": ["where is your office", "office location", "where are you located"],
    "contact": ["contact support", "how to contact", "customer support", "how do I contact support"]
}

def get_reply(category):
    replies = {
        "greeting": "Hey there! 👋",
        "feeling": "I'm doing great! How about you?",
        "creator": "I was created by Yadvendra during his internship! 💻",
        "joke": "Why did the computer go to therapy? It had too many bugs! 😂",
        "time": "The current time is " + datetime.now().strftime("%I:%M %p"),
        "name": "I'm SmartBot, your Python chatbot assistant! 🤖",
        "bye": "Goodbye! Have a great day! 👋",
        "hours": "Our working hours are Monday to Friday, 9 AM to 6 PM.",
        "location": "Our office is located at KIIT University, Bhubaneswar.",
        "contact": "You can contact us at support@example.com or call 1800-123-456."
    }
    return replies.get(category, "Hmm... I don't know how to reply yet.")

def clean_input(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def chatbot_response(user_input):
    cleaned = clean_input(user_input)
    for category, keywords in responses.items():
        for keyword in keywords:
            if keyword in cleaned:
                return get_reply(category)
    return "I'm not sure how to respond to that. Try rephrasing?"

# GUI Setup
def send_message():
    user_input = entry_box.get()
    if user_input.strip() == "":
        return
    chat_area.insert(tk.END, f"You: {user_input}\n")
    bot_reply = chatbot_response(user_input)
    chat_area.insert(tk.END, f"SmartBot: {bot_reply}\n\n")
    entry_box.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("SmartBot - GUI Chatbot")
root.geometry("500x500")

# Chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='normal', font=("Arial", 11))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry and send button
entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=5, fill=tk.X)

entry_box = tk.Entry(entry_frame, font=("Arial", 12))
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry_box.bind("<Return>", lambda event: send_message())

send_button = tk.Button(entry_frame, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(side=tk.RIGHT)

# Start message
chat_area.insert(tk.END, "SmartBot 🤖: Hello! Ask me anything (type 'bye' to exit)\n\n")

# Run GUI loop
root.mainloop()
