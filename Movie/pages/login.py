import streamlit as st
import json
import os
import bcrypt

def load_user_data():
    if os.path.exists('../user_data.json'):
        with open('../user_data.json') as f:
            return json.load(f)
    return {"users": {}}

def save_user_data(data):
    with open('../user_data.json', 'w') as f:
        json.dump(data, f, indent=4)

user_data = load_user_data()

st.title("Login / Sign Up")

tab1, tab2 = st.tabs(["Login", "Sign Up"])

with tab1:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in user_data['users'] and bcrypt.checkpw(password.encode(), user_data['users'][username]['password'].encode()):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid credentials")

with tab2:
    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")
    if st.button("Sign Up"):
        if new_user in user_data['users']:
            st.error("User already exists")
        else:
            hashed = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt()).decode()
            user_data['users'][new_user] = {"password": hashed, "watch_history": [], "preferences": {}}
            save_user_data(user_data)
            st.success("Account created! Please login.")