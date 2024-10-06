import nltk
from nltk.chat.util import Chat, reflections

# Download the necessary NLTK resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?", "Hi %1, what brings you here today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello! How can I help you?", "Hi there! How are you feeling today?"]
    ],
    [
        r"i am feeling (.*)",
        ["It's okay to feel %1. Can you tell me more about it?", "I'm sorry to hear that you're feeling %1. What do you think caused this feeling?"]
    ],
    [
        r"i need help with (.*)",
        ["It's great that you're reaching out for help! Can you elaborate on %1?", "I'm here to help! What specific assistance do you need with %1?"]
    ],
    [
        r"what should i do when i feel (.*)",
        ["It's important to talk to someone you trust. Have you considered that?", "Sometimes it helps to express your feelings. How about writing them down?"]
    ],
    [
        r"quit",
        ["Thank you for chatting. Take care and remember, you're not alone!", "Goodbye! Take care of yourself!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that. Can you rephrase?", "Could you tell me more about that?"]
    ]
]

# Create the chatbot
def mental_health_chatbot():
    print("Hi! I'm a mental health chatbot. How can I help you today? (type 'quit' to stop)")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    mental_health_chatbot()
