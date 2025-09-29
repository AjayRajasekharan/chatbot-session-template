import streamlit as st

# Rule-based chatbot = we hardcode responses in a dictionary
responses = {
    "hi": "Hello there! 👋",
    "bye": "Goodbye, see you soon!",
    "thanks": "You're welcome 🙂",
}

st.title("🤖 Rule-Based Chatbot")

# Take user input
user_input = st.text_input("Say something:")

if user_input:
    # Normalize input (lowercase)
    user_input = user_input.lower()

    if user_input in responses:
        st.write("Bot:", responses[user_input])
    else:
        st.write("Bot: Sorry, I don't understand that yet 😅")
