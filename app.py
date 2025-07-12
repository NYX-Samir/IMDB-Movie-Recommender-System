import pickle
import streamlit as st
import pandas as pd



st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.socinvestigation.com/wp-content/uploads/2023/07/how-to-increase-imdb-rating.png");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    .stMarkdown, .stText, .stHeader {
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid white;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        transition: 0.3s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        background-color: rgba(255, 255, 255, 0.3);
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)


movies = pickle.load(open('model.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommender(movie_name):
    movie_name = movie_name.lower()
    matches = movies[movies['Series_Title'].str.lower().str.contains(movie_name)]

    if matches.empty:
        st.error(f"Sorry, '{movie_name}' or similar title was not found in the database")
        return [], []

    index = matches.index[0]
    distance = list(enumerate(similarity[index]))
    sorted_dist = sorted(distance, reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in sorted_dist:
        recommended_movie_names.append(movies.iloc[i[0]].Series_Title)
        recommended_movie_posters.append(movies.iloc[i[0]].Poster_Link)

    return recommended_movie_names, recommended_movie_posters


st.set_page_config(layout="wide")
st.header('IMDB Movies Recommender System')

st.markdown(
    """
    ⚠️ **Note:** This demo uses a limited dataset of **1000 movies** due to Kaggle constraints.  
    Poster images are from a static snapshot because **TMDB API is blocked in India** and live poster fetching is disabled.
    And Sorry Banners are also too old and blurry
    """,
    unsafe_allow_html=True
)

movies = pickle.load(open('model.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['Series_Title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    names, posters = recommender(selected_movie)
    if names:
        cols = st.columns(5)
        for idx in range(len(names)):
            with cols[idx]:
                st.image(posters[idx], use_container_width=True)
                st.caption(names[idx])
