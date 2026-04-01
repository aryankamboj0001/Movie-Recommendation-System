# 🎬 Movie Recommendation System

A full-stack Movie Recommendation System that uses **NLP and Machine Learning** to recommend similar movies.  
It integrates **IMDb API** for movie details and **YouTube API** for trailers.

---

## 🚀 Live Demo
👉 https://movie-recommendation-system-e4r7rtpgnlr8yrq6taxhqh.streamlit.app/

---

## ✨ Features

- Content-based recommendation using **TF-IDF + cosine similarity**
- Movie details using **IMDb API**
- Trailer playback using **YouTube API**
- FastAPI backend for API handling
- Streamlit frontend for UI

---

## 🛠️ Tech Stack

**Backend**
- FastAPI  
- Python  
- Scikit-learn  

**Frontend**
- Streamlit  

**Libraries**
- Pandas, NumPy  

---

## 🧠 How It Works

1. Text preprocessing  
2. TF-IDF vectorization  
3. Cosine similarity calculation  
4. Recommend similar movies  

---

## 📂 Project Structure


Movie-Recommendation-System/
│
├── app.py
├── main.py
├── movies_metadata.csv
├── tfidf.pkl
├── tfidf_matrix.pkl
├── indices.pkl
├── df.pkl
├── assets/
├── sc/
└── README.md


---

## ⚙️ Setup

```bash
git clone https://github.com/aryankamboj0001/Movie-Recommendation-System.git
cd Movie-Recommendation-System

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
▶️ Run
uvicorn main:app --reload
streamlit run app.py
🔑 Environment Variables

Create a .env file:

IMDB_API_KEY=your_key
YOUTUBE_API_KEY=your_key
📈 Future Improvements
Add user authentication
Save favorite movies
Hybrid recommendation system
👨‍💻 Author

Aryan Kumar
https://github.com/aryankamboj0001
