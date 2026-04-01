🎬 Movie Recommendation System
A full-stack Movie Recommendation System that uses Natural Language Processing (NLP) and Machine Learning to recommend similar movies.
It integrates IMDb API for movie details and YouTube API for trailers.

🚀 Live Demo

👉 https://movie-recommendation-system-e4r7rtpgnlr8yrq6taxhqh.streamlit.app/

✨ Key Features
🎯 Smart Recommendations
Content-based filtering using TF-IDF + cosine similarity
🎥 Watch Trailers
Integrated YouTube API for instant trailer playback
⭐ Movie Details
IMDb API for ratings, posters, and overview
⚡ FastAPI Backend
High-performance API handling ML logic
🌐 Interactive UI
Built with Streamlit for smooth user experience
🧠 ML Pipeline (How it Works)
4
Text preprocessing (lowercase, stopwords removal)
Convert text → numerical vectors using TF-IDF
Compute similarity using cosine similarity
Recommend top similar movies
🏗️ System Architecture
4
Frontend (Streamlit) → User input & display
Backend (FastAPI) → Recommendation logic
ML Model → TF-IDF + similarity
External APIs → IMDb + YouTube
🛠️ Tech Stack
👨‍💻 Backend
FastAPI
Python
Scikit-learn
Pandas, NumPy
🎨 Frontend
Streamlit
🔗 APIs
IMDb API
YouTube Data API
📂 Project Structure
Movie-Recommendation-System/
│
├── app.py                  # Streamlit UI
├── main.py                 # FastAPI backend
├── movies_metadata.csv
├── tfidf.pkl
├── tfidf_matrix.pkl
├── indices.pkl
├── df.pkl
├── assets/
├── sc/
└── README.md
⚙️ Setup & Installation
git clone https://github.com/aryankamboj0001/Movie-Recommendation-System.git
cd Movie-Recommendation-System

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
▶️ Run Locally
Start Backend
uvicorn main:app --reload
Start Frontend
streamlit run app.py
🔑 Environment Variables

Create .env file:

IMDB_API_KEY=your_key
YOUTUBE_API_KEY=your_key
📈 Future Enhancements
🔐 User authentication system
❤️ Save favorite movies
🤖 Hybrid recommendation (content + collaborative)
☁️ Deploy backend separately (AWS / Render)
💼 Resume-Ready Points (USE THIS 🔥)

You can copy these into your resume:

Built a full-stack movie recommendation system using FastAPI and Streamlit
Implemented NLP-based recommendation engine using TF-IDF and cosine similarity
Integrated IMDb and YouTube APIs to enhance user experience with real-time data
Designed scalable backend APIs and interactive frontend UI
Improved recommendation efficiency using optimized similarity computation
👨‍💻 Author

Aryan Kumar
🔗 https://github.com/aryankamboj0001

⭐ Support

If you like this project, give it a ⭐ on GitHub!
