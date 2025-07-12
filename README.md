A content-based movie recommender using a 1000-movie IMDB dataset. It extracts features from metadata (genre, overview, director, cast) using CountVectorizer and suggests top 5 similar movies via cosine similarity. Built with Streamlit, it includes static poster display, custom background, and transparent UI elements.

Constraints:
    Only 1000 movies due to Kaggle limits
    TMDB API blocked in India; posters are static

Tech Stack:
Python,Sckit-learn,nltk,CountVectorizer, cosine similarity, Streamlit, pickle
