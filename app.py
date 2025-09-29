import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="LLM Chatbot (Session 2)", page_icon="🤖")

@st.cache_resource
def load_model(model_name: str = "google/flan-t5-small"):
    # text2text works well for Q&A / instruction style
    return pipeline("text2text-generation", model=model_name)

st.title("🤖 Simple LLM Chatbot (Hugging Face, free & open)")

with st.sidebar:
    model_choice = st.selectbox(
        "Model",
        ["google/flan-t5-small", "distilgpt2"],
        help="flan-t5-small is better for Q&A; distilgpt2 is a tiny text generator."
    )
    max_new_tokens = st.slider("Max new tokens", 16, 256, 128, 16)

pipe = load_model(model_choice)

user_input = st.text_input("Ask me anything:")
go = st.button("Ask")

if go and user_input.strip():
    with st.spinner("Thinking..."):
        if model_choice == "google/flan-t5-small":
            out = pipe(user_input, max_new_tokens=max_new_tokens, do_sample=True)
            st.write("**Bot:**", out[0]["generated_text"])
        else:
            # distilgpt2 uses text-generation task
            gen = pipeline("text-generation", model="distilgpt2")
            out = gen(user_input, max_new_tokens=max_new_tokens, do_sample=True)
            st.write("**Bot:**", out[0]["generated_text"])
