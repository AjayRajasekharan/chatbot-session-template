# LLM Chatbot (Streamlit UI version)
# This uses a small "mini brain" model from Hugging Face.
# Runs as a web app with a textbox.

import streamlit as st
from transformers import pipeline

st.title("LLM Chatbot")

# Load the model once (outside the input loop)
generator = pipeline("text2text-generation", model="google/flan-t5-small")

# Input box for user
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Say something:", key="input_text")
    submitted = st.form_submit_button("Send")  # Triggered on Enter or click

if submitted and user_input:
    # Generate a response
    st.write("User:", user_input)
    response = generator(user_input, max_new_tokens=50)[0]["generated_text"]

    # Show the bot's reply
    st.write("Bot:", response)
