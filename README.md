# 🎬 IMDB Movie Recommender System

A **Content-Based Movie Recommendation System** built on the **IMDB Top 1000 Movies dataset**.  
It recommends movies similar to a selected one by analyzing features like **genres, overview, director, and cast** using **CountVectorizer** and **Cosine Similarity**.  

The project includes a **Streamlit Web App** with a clean UI, static movie posters, and custom background styling.  

---

## 📌 Features

- ✅ Content-Based Filtering (cosine similarity)  
- ✅ Metadata used: *Genre, Overview, Director, Cast*  
- ✅ Streamlit UI with transparent design  
- ✅ Static posters included  
- ✅ Precomputed similarity matrix for faster results  

---

## 🛠️ Tech Stack

- Python  
- scikit-learn (`CountVectorizer`, Cosine Similarity)  
- NLTK  
- Streamlit  
- Pickle (serialization)  

---

## 📂 Project Structure

### Mermaid Diagram
```mermaid
graph TD
  root[📂 IMDB-Movie-Recommender-System]
  root --> data[📄 imdb_top_1000.csv]
  root --> nb[📓 IMDB_Movies_Recommender.ipynb]
  root --> app[▶️ app.py]
  root --> model[📦 model.pkl]
  root --> sim[📦 similarity.pkl]
  root --> req[📝 requirements.txt]