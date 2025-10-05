# chatbot-session-template

## Set up and Run GitHub Codespaces
1) Click 'Use this template' option in the top right corner -> Create a new repository
2) After creating the repository → Code → Codespaces → **Create codespace on main**.
3) This should open a new window -> automatically runs pip install -r requirements.txt in the terminal, wait 5 to 10 minutes for set up.

## Run Chatbots on StreamLit
1) In the terminal:
   - streamlit run app_name.py
2) Click on the Local URL in the terminal to open the app.
3)  When Streamlit starts, Codespaces will use **port 8501**.
   If prompted, set port visibility to **Public** (so others can view your demo).
4) Ctrl + C in terminal to close Streamlit App

## How to close/stop Codespace
1. Go to the GitHub website.
2. You can click your profile picture (top right) → Your Codespaces [OR] go directly: https://github.com/codespaces [OR] Go to the repo on which you ran codespace
3. Find the Codespace you were working in (chatbot-session-template).
4. Click ••• (three dots) → Stop Codespace.

# Session 2 - Building Chatbots with LLMs
Welcome to Session 2 of the AI for Everyone: Practical GenAI & Chatbot Development program!
This session is your first deep-dive into coding AI chatbots — moving from simple rule-based logic to LLM-powered conversations using Hugging Face and Streamlit.

## 🎯 Learning Objectives
By the end of this session you will be able to:
- Explain the difference between rule-based and LLM-based chatbots
- Build a chatbot using the Hugging Face pipeline()
- Tune parameters like temperature, top-p and max tokens
- Create a simple Streamlit UI for your chatbot
- Understand how different models behave and where to use each

## Folder Guide for Session 2
| Folder                   | What it contains                      | Purpose                               |
| ------------------------ | ------------------------------------- | ------------------------------------- |
| **/notebooks/**          | Jupyter Notebooks for guided learning | Step-by-step concepts and experiments |
| **/rule_based_chatbot/** | Python scripts for simple chatbots    | Understand hard-coded logic           |
| **/llm_basics/**         | Basic LLM examples with/without UI    | First hands-on LLM chatbot            |
| **/llm_advanced/**       | Multi-model selection and parameters  | Explore temperature, tokens, top-p    |
| **/exercises/**          | In-class and take-home activities     | Practice and build your own chatbot   |
| **/resources/**          | Reading links and extra tutorials     | Optional reference material           |

## How to Use the Session 2 Material
1. Start with /notebooks/
-- Open each .ipynb file in Codespaces → Run cell by cell
-- Compare rule-based vs LLM outputs
-- Play with parameters to see how answers change
2. Move to /rule_based_chatbot/ and /llm_basics/
-- Run the CLI and UI versions to see the difference
-- Understand how Streamlit turns Python scripts into apps
3. Explore /llm_advanced/
-- Test different models (flan-t5-small, distilgpt2, DialoGPT-small)
-- Experiment with temperature and max tokens
4. Work on /exercises/
-- Start with the in-class exercise notebook (during session)
-- Continue with the take-home exercise to build your own personality-based chatbot

## 🧭 Tips for Students

- Wait for Codespace setup to finish before running anything
- Use Restart Kernel › Run All if a notebook freezes
- Stop Streamlit apps with Ctrl + C in the terminal
- Save your progress frequently by committing to GitHub
- Try multiple prompts and parameter values — your experiments help you learn