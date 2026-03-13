from cinemagoer import IMDb

movie_api = IMDb()

def recommend_movies(username, preferences):
    try:
        top = movie_api.get_top250_movies()
        recs = []
        for m in top[:100]:  # check more movies
            movie = movie_api.get_movie(m.movieID)
            genres = movie.get('genres', [])
            rating = movie.get('rating', 0)
            if (not preferences['genres'] or any(pref_genre.lower() in g.lower() for g in genres for pref_genre in preferences['genres'])) and rating >= preferences['min_rating']:
                recs.append({
                    "title": movie.get('title', 'N/A'),
                    "genre": ", ".join(genres),
                    "release_year": str(movie.get('year', 'N/A')),
                    "rating": rating,
                    "poster": movie.get('cover url', None)
                })
                if len(recs) >= 10:
                    break
        return recs
    except Exception as e:
        print(f"Error: {e}")
        return []
