# LLM Chatbot (Streamlit UI version)
# This uses a small "mini brain" model from Hugging Face.
# Runs as a web app with a textbox.

import streamlit as st
from transformers import pipeline

st.title("LLM Chatbot")

# Load the model once (outside the input loop)
generator = pipeline("text2text-generation", model="google/flan-t5-small")

# Input box for user
user_input = st.text_input("Ask me something:")

if user_input:
    # Generate a response
    response = generator(user_input, max_new_tokens=50)[0]["generated_text"]

    # Show the bot's reply
    st.write("Bot:", response)
