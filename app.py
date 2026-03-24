import streamlit as st
import pickle
import requests

# Load data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# TMDB API KEY
API_KEY = "your_tmdb_api_key"

# Recommend function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)),
                        reverse=True,
                        key=lambda x: x[1])[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]


# Fetch poster + trailer
def fetch_details(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    data = requests.get(url).json()

    if data["results"]:
        movie = data["results"][0]
        movie_id = movie["id"]

        poster = "https://image.tmdb.org/t/p/w500" + str(movie.get("poster_path", ""))

        video_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}"
        videos = requests.get(video_url).json()

        trailer = None
        for v in videos.get("results", []):
            if v["type"] == "Trailer":
                trailer = f"https://www.youtube.com/watch?v={v['key']}"

        return poster, trailer

    return None, None


# UI
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommender System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Recommend"):
    names = recommend(selected_movie)

    for name in names:
        st.subheader(name)

        poster, trailer = fetch_details(name)

        if poster:
            st.image(poster)

        if trailer:
            st.video(trailer)
        else:
            st.write("No trailer available")