import streamlit as st
from transformers import pipeline

st.title("LLM Chatbot (Basic)")

# Load a small Hugging Face model (FLAN-T5 Small)
# "pipeline" is a ready-to-use wrapper for different AI tasks
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

# Take user input
user_input = st.text_input("Ask me anything:")

if user_input:
    # Generate response using the LLM
    response = chatbot(user_input, max_new_tokens=50)[0]["generated_text"]
    st.write("Bot:", response)
