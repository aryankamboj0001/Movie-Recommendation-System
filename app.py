import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    movies = pd.read_pickle("movies_df.pkl")
    tfidf_matrix = pickle.load(open("tfidf_matrix.pkl","rb"))
    indices = pickle.load(open("indices.pkl","rb"))
    return movies, tfidf_matrix, indices

movies, tfidf_matrix, indices = load_data()

# Recommend function
def recommend(movie):

    idx = indices[movie]

    sim_scores = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    sim_scores = list(enumerate(sim_scores))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices]


# ---------- UI ----------

st.markdown(
"""
<h1 style='text-align:center; font-size:50px;'>
🎬 Movie Recommender
</h1>
<p style='text-align:center; font-size:20px; color:gray;'>
Discover movies similar to your favorites
</p>
""",
unsafe_allow_html=True
)

st.write("")
st.write("")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Search Movie",
    movie_list,
    index=None,
    placeholder="Type movie name..."
)

st.write("")

if st.button("🎥 Show Recommendations"):

    recommendations = recommend(selected_movie)

    st.markdown("## 🍿 Recommended Movies")

    cols = st.columns(5)

    for i in range(10):

        with cols[i % 5]:

            st.markdown(
                f"""
                <div style="
                padding:15px;
                border-radius:10px;
                background:#111;
                text-align:center;
                font-size:16px;
                ">
                ⭐ {recommendations.iloc[i]}
                </div>
                """,
                unsafe_allow_html=True
            )