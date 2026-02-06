# BOOKXPERT

# AI Assignment: Name Matcher & Recipe Chatbot

This repository contains a complete solution for the AI Assignment. It features two main components:
1.  **Task 1: Name Matching System** - Uses fuzzy logic to find similar names from a dataset.
2.  **Task 2: Local AI Chatbot** - A full-stack application (FastAPI + Streamlit) that uses a local LLM to suggest recipes based on user ingredients.

## 📂 Project Structure

Ensure your project folder is organized as follows:

```text
AI_Assignment/
│
├── requirements.txt          # Project dependencies (FastAPI, Streamlit, Torch, etc.)
├── task1_matcher.py          # Script for Task 1: Name Matching
├── task2_api.py              # Script for Task 2b: Backend API (FastAPI)
├── task2_ui.py               # Script for Task 2c: Frontend Interface (Streamlit)
├── task2_train.py            # (Optional) Script for fine-tuning the model
├── recipes.json              # Data file for training/testing
└── README.md                 # Project documentation


🛠️ Step 1: Environment Setup (Zero to Hero)
Before running the code, you must set up a clean Python environment. This ensures all dependencies work correctly without affecting your system.

1. Check Python Version

Ensure you have Python 3.8 or higher installed.

python --version
# OR
python3 --version

2. Create a Virtual Environment

Run the command appropriate for your operating system:

For Windows:

Bash
python -m venv venv
For Mac / Linux:

Bash
python3 -m venv venv
(Note for Linux users: If this fails, run sudo apt install python3-venv first).

3. Activate the Environment

You must activate the environment every time you open a new terminal to work on this project.

For Windows:

Bash
.\venv\Scripts\activate
For Mac / Linux:

Bash
source venv/bin/activate
Successful activation is indicated by (venv) appearing at the start of your command line.

4. Install Dependencies

With the environment active, install the required libraries:

Bash
pip install -r requirements.txt
🚀 Step 2: How to Run Task 1 (Name Matcher)
Objective: Input a name and get the most similar matches from the dataset.

Open your terminal and ensure (venv) is active.

Run the script:

Bash
python task1_matcher.py
Verification:

Input: Type Geeta

Output: The system should return Best Match: Geetha with a high similarity score.

🍳 Step 3: How to Run Task 2 (Recipe Chatbot)
Objective: A chatbot that suggests recipes based on ingredients (e.g., "Egg, Onion").

Important: This task requires two separate terminals running simultaneously (one for the Backend API, one for the Frontend UI).

Terminal 1: Start the Backend (API)

Open a new terminal window.

Activate the environment (source venv/bin/activate or .\venv\Scripts\activate).

Run the FastAPI server:

Bash
uvicorn task2_api:app --reload
Wait for the message: Application startup complete.

The API is now live at http://127.0.0.1:8000

Terminal 2: Start the Frontend (UI)

Open a second terminal window.

Activate the environment again.

Run the Streamlit app:

Bash
streamlit run task2_ui.py
This command will automatically open your web browser to the Chatbot interface.

If it doesn't open automatically, visit http://localhost:8501 in your browser.

Verification

In the web interface, type Egg, Onion into the chat box.

Press Enter.

Expected Output: The AI Assistant replies with a recipe (e.g., "Scramble the eggs...").

