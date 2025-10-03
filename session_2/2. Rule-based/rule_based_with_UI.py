import streamlit as st

# Rule-Based Chatbot (Streamlit UI version)
# This runs as a small web app instead of the console.

st.title("Rule-Based Chatbot")

# RULES: We store fixed responses in a dictionary
responses = {
    "hi": "Hello there!",
    "bye": "Goodbye, see you soon!",
    "thanks": "You're welcome",
    "how are you?": "I'm good, how are you?",
}

# Input box for the user (instead of typing in console)
user_input = st.text_input("Say something:")

if user_input:
    # Normalize input (make lowercase so 'Hi' and 'hi' are the same)
    user_input = user_input.lower().strip()

    # If user says something we know → reply from dictionary
    if user_input in responses:
        st.write("Bot:", responses[user_input])
    else:
        # If it's not in dictionary → default reply
        st.write("Bot: Sorry, I don't understand that yet...")
