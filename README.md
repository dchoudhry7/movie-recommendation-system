# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System that suggests movies based on similarity between movie features such as genres, keywords, and descriptions.

---

## 🚀 Overview

This project builds a content-based recommendation engine that helps users discover movies similar to their interests. It processes movie metadata and computes similarity scores to recommend the most relevant movies.

---

## 🧠 Features

- Recommend movies based on a selected title  
- Fast similarity-based recommendations  
- Uses real-world movie dataset  
- Simple and efficient implementation  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  

---

## 📂 Project Structure

movie-recommendation-system/
│
├── data/                # Dataset files
├── model/              # Saved model files
├── main.py             # Core recommendation logic
├── app.py              # Application file (if UI used)
├── requirements.txt    # Dependencies
└── README.md

---

## ⚙️ How It Works

1. Data is cleaned and relevant features are selected  
2. Text features are converted into vectors using techniques like CountVectorizer  
3. Cosine similarity is computed between movies  
4. Top similar movies are recommended based on input  

---

## 📦 Installation

git clone https://github.com/dchoudhry7/movie-recommendation-system.git  
cd movie-recommendation-system  
pip install -r requirements.txt  

---

## ▶️ Usage

python main.py  

OR  

streamlit run app.py  

---

## 📊 Dataset

The system uses a movie dataset containing titles, genres, and descriptions to generate recommendations.

---

## 🔮 Future Improvements

- Add collaborative filtering  
- Build a hybrid recommendation system  
- Improve recommendation accuracy  
- Deploy as a web application  
