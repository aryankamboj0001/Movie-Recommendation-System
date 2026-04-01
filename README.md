<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=🎬%20CineMatch&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=AI-Powered%20Movie%20Recommendation%20Engine&descAlignY=60&descSize=18" width="100%"/>

<br/>

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://movie-recommendation-system-e4r7rtpgnlr8yrq6taxhqh.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br/>

> *Discover your next favorite movie — powered by NLP, cosine similarity, and real-time IMDb + YouTube integration.*

<br/>

</div>

---

## ✨ What is CineMatch?

**CineMatch** is a full-stack, AI-powered Movie Recommendation System that understands the *language* of cinema. Type in a movie you love — and the engine will instantly surface the most similar titles using **TF-IDF vectorization** and **cosine similarity**, enriched with live data from IMDb and YouTube.

<br/>

<div align="center">

| 🎯 Smart Recs | 🎥 Trailers | ⭐ IMDb Data | ⚡ Fast API | 🌐 Smooth UI |
|:-:|:-:|:-:|:-:|:-:|
| Content-based NLP filtering | Instant YouTube playback | Ratings, posters & overviews | FastAPI ML backend | Built with Streamlit |

</div>

<br/>

---

## 🧠 How It Works — ML Pipeline

```
  User Input (Movie Title)
         │
         ▼
  ┌─────────────────────────────────┐
  │  1. Text Preprocessing          │
  │     Lowercase · Stopword Remove │
  └───────────────┬─────────────────┘
                  │
                  ▼
  ┌─────────────────────────────────┐
  │  2. TF-IDF Vectorization        │
  │     Text → Numerical Vectors    │
  └───────────────┬─────────────────┘
                  │
                  ▼
  ┌─────────────────────────────────┐
  │  3. Cosine Similarity           │
  │     Find Most Similar Movies    │
  └───────────────┬─────────────────┘
                  │
                  ▼
  ┌─────────────────────────────────┐
  │  4. Enrich with External APIs   │
  │     IMDb · YouTube              │
  └───────────────┬─────────────────┘
                  │
                  ▼
       🎬 Top-N Recommendations
```

<br/>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CineMatch                            │
│                                                             │
│   ┌──────────────┐      ┌──────────────┐                   │
│   │  🌐 Frontend  │ ───► │  ⚡ Backend   │                   │
│   │  (Streamlit)  │ ◄─── │  (FastAPI)   │                   │
│   └──────────────┘      └──────┬───────┘                   │
│                                │                            │
│                    ┌───────────┼───────────┐                │
│                    ▼           ▼           ▼                │
│             ┌────────────┐  ┌──────┐  ┌────────┐           │
│             │ 🤖 ML Model │  │ IMDb │  │   📺   │           │
│             │ TF-IDF +   │  │  API │  │YouTube │           │
│             │ Similarity  │  └──────┘  └────────┘           │
│             └────────────┘                                  │
└─────────────────────────────────────────────────────────────┘
```

<br/>

---

## 🛠️ Tech Stack

<div align="center">

### Backend
![Python](https://img.shields.io/badge/Python-FFD43B?style=flat-square&logo=python&logoColor=blue)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=FastAPI&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)

### Frontend
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

### External APIs
![IMDb](https://img.shields.io/badge/IMDb-F5C518?style=flat-square&logo=imdb&logoColor=black)
![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white)

</div>

<br/>

---

## 📂 Project Structure

```
🎬 Movie-Recommendation-System/
│
├── 📄 app.py                  # Streamlit frontend UI
├── ⚡ main.py                  # FastAPI backend & ML logic
├── 🗃️  movies_metadata.csv     # Core dataset
│
├── 🤖 ML Artifacts/
│   ├── tfidf.pkl              # Trained TF-IDF vectorizer
│   ├── tfidf_matrix.pkl       # Pre-computed TF-IDF matrix
│   ├── indices.pkl            # Movie index mapping
│   └── df.pkl                 # Processed dataframe
│
├── 🖼️  assets/                 # Static assets & images
├── 📸 sc/                     # Screenshots
├── 📋 requirements.txt
└── 📖 README.md
```

<br/>

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- IMDb API Key → [Get it here](https://rapidapi.com/hub)
- YouTube Data API v3 Key → [Get it here](https://console.cloud.google.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/aryankamboj0001/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Create & Activate Virtual Environment

```bash
# Create environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
IMDB_API_KEY=your_imdb_api_key_here
YOUTUBE_API_KEY=your_youtube_api_key_here
```

### 5. Run the Application

**Start the FastAPI Backend:**
```bash
uvicorn main:app --reload
```
> Backend runs at `http://localhost:8000`

**Start the Streamlit Frontend** *(in a new terminal)*:
```bash
streamlit run app.py
```
> Frontend runs at `http://localhost:8501`

<br/>

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/recommend` | Get movie recommendations |
| `GET` | `/movie/{title}` | Fetch movie metadata |

<br/>

---

## 📈 Roadmap

- [x] Content-based filtering with TF-IDF + cosine similarity
- [x] IMDb API integration (ratings, posters, overview)
- [x] YouTube trailer playback
- [x] FastAPI backend with ML pipeline
- [x] Streamlit interactive UI
- [ ] 🔐 User authentication system
- [ ] ❤️ Save & manage favorite movies
- [ ] 🤖 Hybrid recommendations (content + collaborative filtering)
- [ ] ☁️ Separate cloud backend deployment (AWS / Render)
- [ ] 📊 User analytics dashboard

<br/>

---

## 🤝 Contributing

Contributions are always welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

<br/>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<br/>

---

<div align="center">

**Made with ❤️ by [Aryan Kamboj](https://github.com/aryankamboj0001)**

⭐ Star this repo if you found it helpful!

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
