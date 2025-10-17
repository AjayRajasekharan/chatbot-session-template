# Rule-Based Chatbot (CLI version)
# This runs in the terminal/console, not in a web app.

# RULES: We store fixed responses in a dictionary
responses = {
    "hi": "Hello there!",
    "bye": "Goodbye, see you soon!",
    "thanks": "You're welcome",
    "how are you?": "I'm good, how are you?",
}

print("Rule-Based Chatbot (type 'bye' to exit)")

while True:
    # Take user input from console
    user_input = input("You: ")

    # Normalize input (lowercase for easier matching)
    user_input = user_input.lower().strip()

    # If user says 'bye' → exit
    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    # Check dictionary for known responses
    if user_input in responses:
        print("Bot:", responses[user_input])
    else:
        print("Bot: Sorry, I don't understand that yet...")
