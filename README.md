# chatbot-session-template
Test repo for chatbot session

## Set up and Run GitHub Codespaces
1) Click 'Use this template' option in green on the top right corner -> Create a new repository
2) After creating the repository → Code → Codespaces → **Create codespace on main**.
3) This should open a new window -> automatically runs pip install -r requirements.txt in the terminal, wait 5 to 10 minutes for set up.

## Run Chatbots

### Option 1
1. In Codespaces, press `Ctrl+Shift+P`.
2. Type **Run Task** and select:
   - `Run Chatbot (App 1)` for the rule-based chatbot
   - `Run Chatbot (App 2)` for the basic LLM chatbot
   - `Run Chatbot (App 3)` for the full chatbot with sidebar
3. When Streamlit starts, a port will appear (usually 8501).
4. Click the port link to open your chatbot in the browser.
5. To stop the chatbot, press `Ctrl+C` in the terminal.

### Option 2
1) In the terminal:
   - streamlit run app_name.py
2) Click on the Local URL in the terminal to open the app.
3)  When Streamlit starts, Codespaces will use **port 8501**.
   If prompted, set port visibility to **Public** (so others can view your demo).
4) Ctrl + C in terminal to close Streamlit App

## Notes
- Prefer **google/flan-t5-small** for Q&A style prompts.
- If downloads are slow the first time, wait—models are cached after first run.

