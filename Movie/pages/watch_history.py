import streamlit as st
import json
import os

def load_user_data():
    if os.path.exists('../user_data.json'):
        with open('../user_data.json') as f:
            return json.load(f)
    return {"users": {}}

def save_user_data(data):
    with open('../user_data.json', 'w') as f:
        json.dump(data, f, indent=4)

st.title("Watch History")

user_data = load_user_data()
username = st.session_state.username
watch_history = user_data['users'][username]['watch_history']

if watch_history:
    for i, movie in enumerate(watch_history):
        st.subheader(f"{movie['title']} ({movie['release_year']})")
        st.write(f"Genres: {movie['genre']}")
        st.write(f"Your Rating: {movie['rating']}/5")
        st.write(f"Review: {movie['review'] or 'No review'}")
        if st.button(f"Delete {movie['title']}", key=f"delete_{i}"):
            del watch_history[i]
            save_user_data(user_data)
            st.rerun()
else:
    st.write("No watch history yet.")