# 🎬 IMDB Movie Recommender System

A **Content-Based Movie Recommendation System** built on the **IMDB Top 1000 Movies dataset**.  
It recommends movies similar to a selected one by analyzing features like **genres, overview, director, and cast** using **CountVectorizer** and **Cosine Similarity**.  

The project includes a **Streamlit Web App** with a clean UI, static movie posters, and custom background styling.  

---

## 📌 Features

- ✅ **Content-Based Filtering** – finds movies similar to your selection.  
- ✅ Uses **metadata**: *Genre, Overview, Director, Cast*.  
- ✅ **Cosine Similarity** for movie comparison.  
- ✅ **Streamlit Web App** with transparent UI and background.  
- ✅ Static **poster display** for selected recommendations.  

---

## 🛠️ Tech Stack

- **Python**  
- **scikit-learn** (`CountVectorizer`, Cosine Similarity)  
- **NLTK**  
- **Streamlit**  
- **Pickle** (model serialization)  

---

## 📂 Project Structure

```mermaid
graph TD
    A[📂 IMDB-Movie-Recommender-System] --> B[📄 imdb_top_1000.csv]
    A --> C[📓 IMDB_Movies_Recommender.ipynb]
    A --> D[▶️ app.py]
    A --> E[📦 model.pkl]
    A --> F[📦 similarity.pkl]
    A --> G[📝 requirements.txt]
