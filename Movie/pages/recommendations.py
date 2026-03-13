import streamlit as st
import json
import os
from recommendation import recommend_movies

st.title("Get Recommendations")

if 'preferences' not in st.session_state:
    st.session_state.preferences = {}

# Questions
genres_options = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "TV Movie", "Thriller", "War", "Western"]
preferred_genres = st.multiselect("Preferred Genres", genres_options)
min_rating = st.slider("Minimum Rating", 0.0, 10.0, 7.0)

if st.button("Get Recommendations"):
    st.session_state.preferences = {
        "genres": preferred_genres,
        "min_rating": min_rating
    }
    recommendations = recommend_movies(st.session_state.username, st.session_state.preferences)
    st.header("Recommended Movies")
    if recommendations:
        for rec in recommendations:
            col1, col2 = st.columns([1, 2])
            with col1:
                if rec['poster']:
                    st.image(rec['poster'], width=100)
            with col2:
                st.write(f"**{rec['title']}** ({rec['release_year']})")
                st.write(f"Genres: {rec['genre']}")
                st.write(f"Rating: {rec['rating']}")
    else:
        st.write("No recommendations found. Try adjusting your preferences.")