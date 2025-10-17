import streamlit as st

st.title("Rule-Based Chatbot")

# RULES: We store fixed responses in a dictionary
responses = {
    "hi": "Hello there!",
    "bye": "Goodbye, see you soon!",
    "thanks": "You're welcome",
    "how are you?": "I'm good, how are you?",
}

# Input box for the user (instead of typing in console)
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Say something:", key="input_text")
    submitted = st.form_submit_button("Send")  # Triggered on Enter or click

if submitted and user_input:
    # Normalize input (make lowercase so 'Hi' and 'hi' are the same)
    normalized_input = user_input.lower().strip()

    st.write("User:", user_input)
    if normalized_input in responses:
        # If user says something we know → reply from dictionary
        st.write("Bot:", responses[normalized_input])
    else:
        # If it's not in dictionary → default reply
        st.write("Bot: Sorry, I don't understand that yet...")

    # Clear the input box after processing
    st.session_state.input_box = ""
