import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-recommendation-system-tk8s.onrender.com/" or "http://127.0.0.1:8000"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# =============================
# CSS
# =============================
st.markdown("""
<style>
.small-muted{
color:#6b7280;
font-size:0.9rem;
}
.movie-title{
font-size:0.9rem;
font-weight:600;
}
.movie-card{
transition: transform 0.2s ease;
}
.movie-card:hover{
transform: scale(1.05);
}
.hero-img img{
height:200px;
object-fit:cover;
border-radius:10px;
}
img{
border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# SESSION STATE
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"

if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

# =============================
# NAVBAR
# =============================
nav1, nav2 = st.columns([1,6])

with nav1:
    if st.button("🏠 Home"):
        st.session_state.view = "home"
        st.rerun()

grid_cols = 5

# =============================
# API CALL
# =============================
def api_get_json(path, params=None):
    try:
        r = requests.get(
            f"{API_BASE}{path}",
            params=params,
            timeout=20
        )

        if r.status_code != 200:
            st.error(f"API Error {r.status_code}")
            st.text(r.text)
            return None

        if not r.text.strip():
            st.error("Empty API response")
            return None

        return r.json()

    except Exception as e:
        st.error("Request Failed")
        st.write(e)
        return None

# =============================
# POSTER GRID - FIXED VERSION
# =============================
def poster_grid(cards, cols=5):
    if not cards:
        st.warning("No movies found")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0

    for r in range(rows):
        columns = st.columns(cols)

        for c in range(cols):
            if idx >= len(cards):
                break

            movie = cards[idx]
            idx += 1

            poster = movie.get("poster_url")
            title = movie.get("title")
            tmdb_id = movie.get("tmdb_id")
            rating = movie.get("vote_average")
            release = movie.get("release_date")

            year = release[:4] if release else ""

            with columns[c]:
                if poster:
                    # ✅ FIXED: Removed deprecated use_column_width
                    st.image(poster, width=250)

                st.markdown(
                    f"""
                    <div class="movie-card">
                    <div class="movie-title">{title}</div>
                    ⭐ {rating} | {year}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button("Open", key=f"{tmdb_id}_{idx}"):
                    st.session_state.view = "details"
                    st.session_state.selected_tmdb_id = tmdb_id
                    st.rerun()

# =============================
# HERO BANNER
# =============================
st.markdown(
"""
<div class="hero-img">
<img src="https://image.tmdb.org/t/p/original/9BBTo63ANSmhC4e6r62OJFuK2GL.jpg" width="100%">
</div>
""",
unsafe_allow_html=True
)

st.title("🎬 Movie Recommender")

# =============================
# HOME PAGE
# =============================
if st.session_state.view == "home":
    search = st.text_input(
        "Search movie",
        placeholder="Batman, Avengers, Love..."
    )

    if search:
        st.caption(f"Results for **{search}**")

        with st.spinner("Searching movies..."):
            data = api_get_json(
                "/tmdb/search",
                {"query": search}
            )

        if data:
            results = data.get("results", [])

            cards = []
            for m in results:
                cards.append({
                    "tmdb_id": m.get("tmdb_id") or m.get("id"),
                    "title": m.get("title"),
                    "poster_url": TMDB_IMG + m["poster_path"] if m.get("poster_path") else None,
                    "vote_average": m.get("vote_average"),
                    "release_date": m.get("release_date")
                })

            poster_grid(cards, grid_cols)

    else:
        st.subheader("🔥 Trending Movies")

        with st.spinner("Loading movies..."):
            home = api_get_json("/home")

        if home:
            poster_grid(home, grid_cols)

# =============================
# DETAILS PAGE - FINAL FIXED
# =============================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id

    if st.button("⬅ Back"):
        st.session_state.view = "home"
        st.rerun()

    with st.spinner("Loading movie details..."):
        movie = api_get_json(f"/movie/id/{tmdb_id}")

    # 🔥 DEBUG (optional - remove later)
    # st.write(movie)

    if movie:
        st.header(movie.get("title"))

        col1, col2 = st.columns([1, 2])

        with col1:
            poster = movie.get("poster_url")
            if poster:
                st.image(poster, width=300)

        with col2:
            st.subheader("📖 Overview")
            st.write(movie.get("overview"))

            st.markdown("---")

            # 🎬 TRAILER SECTION (FINAL FIX)
            trailer_url = movie.get("trailer_url")

            st.subheader("🎬 Trailer")

            if trailer_url:
                st.video(trailer_url)   # ✅ ALWAYS SHOW VIDEO
            else:
                st.warning("Trailer not available")

        st.divider()

        # =============================
        # RECOMMENDATIONS
        # =============================
        st.subheader("🎯 Recommendations")

        rec = api_get_json(
            "/recommend/genre",
            {"tmdb_id": tmdb_id}
        )

        if rec:
            poster_grid(rec, grid_cols)