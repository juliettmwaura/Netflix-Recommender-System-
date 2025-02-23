import streamlit as st
import pickle

movies = pickle.load(open('movie_data.pkl', 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")
st.selectbox("Select movie from dropdown", movies_list)



if st.button("Show Recommend"):
    pass