import nltk
import string
import difflib

# Download punkt tokenizer if not already present
nltk.download('punkt')

# Define keyword-based intents
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

# Reply generator
def get_reply(category):
    from datetime import datetime
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

# Clean user input
def clean_input(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Smart matching using difflib
def chatbot_response(user_input):
    cleaned = clean_input(user_input)

    for category, keywords in responses.items():
        for keyword in keywords:
            # Use fuzzy matching with threshold
            ratio = difflib.SequenceMatcher(None, cleaned, keyword).ratio()
            if keyword in cleaned or ratio > 0.75:
                return get_reply(category)

    return "I'm not sure how to respond to that. Try rephrasing?"

# Chat loop
print("SmartBot 🤖: Hello! Ask me anything (type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("SmartBot:", get_reply("bye"))
        break
    print("SmartBot:", chatbot_response(user_input))
