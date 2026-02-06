import streamlit as st
import requests

st.title("🍳 AI Recipe Chef")
st.write("Enter ingredients, and I'll suggest a recipe!")

# Task 1 Integration (Bonus: showing name matching in the same app)
st.sidebar.header("Task 1: Name Matcher")
name_input = st.sidebar.text_input("Find similar name:")
if st.sidebar.button("Search Name"):
    # We import the logic from Task 1 directly
    from task1_matcher import find_best_matches
    results = find_best_matches(name_input)
    st.sidebar.success(f"Best: {results['best_match']['name']}")
    st.sidebar.write(results['all_matches'])

# Task 2: Chatbot Interface [cite: 25]
user_input = st.chat_input("Enter ingredients (e.g., Egg, Onion)...")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_input:
    # 1. User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 2. Call API [cite: 26]
    with st.spinner("Chef is thinking..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/generate_recipe", 
                json={"ingredients": user_input}
            )
            if response.status_code == 200:
                recipe = response.json().get("recipe", "No recipe found.")
            else:
                recipe = "Error: Could not connect to the API."
        except Exception as e:
            recipe = f"Connection Error: {e}"

    # 3. AI Reply
    st.session_state.messages.append({"role": "assistant", "content": recipe})
    with st.chat_message("assistant"):
        st.write(recipe)