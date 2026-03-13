import streamlit as st
import json
import os
from cinemagoer import IMDb

# No config needed for cinemagoer
movie_api = IMDb()

# Load user data
def load_user_data():
    if os.path.exists('user_data.json'):
        with open('user_data.json') as f:
            return json.load(f)
    return {"users": {}}

def save_user_data(data):
    with open('user_data.json', 'w') as f:
        json.dump(data, f, indent=4)

user_data = load_user_data()

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

if not st.session_state.logged_in:
    pages = [st.Page("pages/login.py", title="Login")]
else:
    pages = [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/search_movies.py", title="Search Movies"),
        st.Page("pages/rate_movies.py", title="Rate Movies"),
        st.Page("pages/recommendations.py", title="Get Recommendations"),
        st.Page("pages/watch_history.py", title="Watch History"),
    ]

pg = st.navigation(pages)
pg.run()
