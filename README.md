# BOOKXPERT

# AI Assignment: Name Matcher & Recipe Chatbot

This repository contains a complete solution for the AI Assignment. It features two main components:
1.  **Task 1: Name Matching System** - Uses fuzzy logic to find similar names from a dataset.
2.  **Task 2: Local AI Chatbot** - A full-stack application (FastAPI + Streamlit) that uses a local LLM to suggest recipes based on user ingredients.

## 📂 Project Structure

Ensure your project folder is organized as follows:

```text

BOOKXPERT/
│
├── requirements.txt          # Project dependencies (FastAPI, Streamlit, Torch, etc.)
├── task1_matcher.py          # Script for Task 1: Name Matching
├── task2_api.py              # Script for Task 2b: Backend API (FastAPI)
├── task2_ui.py               # Script for Task 2c: Frontend Interface (Streamlit)
├── task2_train.py            # (Optional) Script for fine-tuning the model
├── recipes.json              # Data file for training/testing
└── README.md                 # Project documentation


🛠️ Step 1: Environment Setup
Before running any code, you must set up a clean Python environment to avoid conflicts.

1.1 Create the Virtual Environment

Open your terminal in the project folder and run the command for your OS:

Windows:

Bash
python -m venv venv
Mac / Linux:

Bash
python3 -m venv venv
(Note: If Linux fails, try sudo apt install python3-venv first).

1.2 Activate the Environment

You must activate the environment every time you open a new terminal.

Windows:

Bash
.\venv\Scripts\activate
Mac / Linux:

Bash
source venv/bin/activate
Success Check: You should see (venv) at the start of your command line.

1.3 Install Dependencies

Install all required libraries including trl to ensure smooth execution:

Bash
pip install -r requirements.txt
🚀 Step 2: Run Task 1 (Name Matcher)
Objective: Input a name and get the most similar matches from the dataset.

Ensure your terminal has (venv) active.

Run the matcher script:

Bash
python task1_matcher.py
Verification:

Input: Type Geeta

Output: The system should return Best Match: Geetha along with a similarity score.

🍳 Step 3: Run Task 2 (Recipe Chatbot)
Objective: A chatbot that suggests recipes based on ingredients (e.g., "Egg, Onion").

Important: This task requires two separate terminals running at the same time.

3a. Start the Backend (Terminal 1)

Open a new terminal window.

Activate the environment (.\venv\Scripts\activate or source venv/bin/activate).

Run the API server:

Bash
uvicorn task2_api:app --reload
Wait for the message: Application startup complete.

The backend is now live at http://127.0.0.1:8000

3b. Start the Frontend (Terminal 2)

Open a second new terminal window.

Activate the environment again.

Run the UI app:

Bash
streamlit run task2_ui.py
This will automatically open your browser to the Chatbot.

If not, manually visit http://localhost:8501.

Verification

In the browser, type Egg, Onion into the chat box.

Press Enter.

Result: The AI Assistant should reply with a recipe (e.g., "Scramble the eggs...").
