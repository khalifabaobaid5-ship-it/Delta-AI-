import streamlit as st
import json
import os

def load_user_data():
    if os.path.exists('../user_data.json'):
        with open('../user_data.json') as f:
            return json.load(f)
    return {"users": {}}

user_data = load_user_data()

st.title("Home")

st.write(f"Welcome, {st.session_state.username}!")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()

# Show some stats
user = user_data['users'][st.session_state.username]

st.header("Your Stats")

st.write(f"Movies rated: {len(user['watch_history'])}")

# Perhaps recent activity
if user['watch_history']:
    st.header("Recent Ratings")
    for item in user['watch_history'][-5:]:  # last 5
        st.write(f"{item['title']} - Rating: {item['rating']}")
else:
    st.write("No ratings yet. Start by searching and rating movies!")