# LLM Chatbot (CLI version)
# This uses a small "mini brain" model from Hugging Face.
# Runs in the console.

from transformers import pipeline

# Load the model once
# "flan-t5-small" = a small instruction-following model (fast to run)
generator = pipeline("text2text-generation", model="google/flan-t5-small")

print("LLM Chatbot (type 'bye' to exit)")

while True:
    # Take input from the user
    user_input = input("You: ")

    # Exit if user types 'bye'
    if user_input.lower().strip() == "bye":
        print("Bot: Goodbye, see you soon!")
        break

    # Generate a response (limit to 50 tokens so it doesn't ramble)
    response = generator(user_input, max_new_tokens=50)[0]["generated_text"]

    # Print the bot's reply
    print("Bot:", response)
