import streamlit as st
import json
import os
from cinemagoer import IMDb

movie_api = IMDb()

def load_user_data():
    if os.path.exists('../user_data.json'):
        with open('../user_data.json') as f:
            return json.load(f)
    return {"users": {}}

def save_user_data(data):
    with open('../user_data.json', 'w') as f:
        json.dump(data, f, indent=4)

@st.cache_data
def get_popular_movies():
    try:
        popular = movie_api.get_popular100_movies()
        movies = []
        for m in popular[:50]:  # limit to 50
            movie = movie_api.get_movie(m.movieID)
            movies.append({
                "title": movie.get('title', 'N/A'),
                "genre": ", ".join(movie.get('genres', [])),
                "release_year": str(movie.get('year', 'N/A')),
                "rating": movie.get('rating', 'N/A'),
                "poster": movie.get('cover url', None),
                "id": m.movieID
            })
        return movies
    except Exception as e:
        st.error(f"Error fetching popular movies: {e}")
        return []

popular_movies = get_popular_movies()

st.title("Rate Movies")

movie_query = st.text_input("Start typing movie name")

filtered_movies = [m for m in popular_movies if movie_query.lower() in m['title'].lower()]

if filtered_movies:
    selected_title = st.selectbox("Select a movie to rate", [m['title'] for m in filtered_movies])
    selected_movie = next(m for m in filtered_movies if m['title'] == selected_title)

    col1, col2 = st.columns([1, 2])
    with col1:
        if selected_movie['poster']:
            st.image(selected_movie['poster'], width=150)
    with col2:
        st.write(f"**{selected_movie['title']}** ({selected_movie['release_year']})")
        st.write(f"Genres: {selected_movie['genre']}")
        st.write(f"IMDb Rating: {selected_movie['rating']}")

    rating = st.slider("Your Rating", 1, 5)
    review = st.text_area("Your Review")

    if st.button("Submit Rating"):
        user_data = load_user_data()
        username = st.session_state.username
        watch_entry = {
            "title": selected_movie['title'],
            "genre": selected_movie['genre'],
            "rating": rating,
            "review": review,
            "release_year": selected_movie['release_year']
        }
        user_data['users'][username]['watch_history'].append(watch_entry)
        save_user_data(user_data)
        st.success("Rating submitted!")
else:
    st.write("Type to search for movies to rate.")