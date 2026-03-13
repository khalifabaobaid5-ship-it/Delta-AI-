import streamlit as st
import json
import os
from cinemagoer import IMDb

movie_api = IMDb()

@st.cache_data
def search_movies(query):
    try:
        results = movie_api.search_movie(query)
        movies = []
        for m in results[:10]:  # limit to 10
            movie = movie_api.get_movie(m.movieID)
            movies.append({
                "title": movie.get('title', 'N/A'),
                "genre": ", ".join(movie.get('genres', [])),
                "release_year": str(movie.get('year', 'N/A')),
                "rating": movie.get('rating', 'N/A'),
                "poster": movie.get('cover url', None),
                "overview": movie.get('plot outline', '')
            })
        return movies
    except Exception as e:
        st.error(f"Error searching movies: {e}")
        return []

st.title("Search Movies")

query = st.text_input("Enter movie title")
if st.button("Search") and query:
    results = search_movies(query)
    if results:
        for r in results:
            col1, col2 = st.columns([1, 3])
            with col1:
                if r['poster']:
                    st.image(r['poster'], width=100)
            with col2:
                st.write(f"**{r['title']}** ({r['release_year']})")
                st.write(f"Genres: {r['genre']}")
                st.write(f"Rating: {r['rating']}")
                if st.button(f"Show Overview for {r['title']}", key=f"overview_{r['title']}"):
                    st.write(r['overview'])
    else:
        st.write("No movies found.")