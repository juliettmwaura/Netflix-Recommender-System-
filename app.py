
import pickle
import pandas as pd

print(pickle.format_version)

df = pd.read_pickle('movie_data.pkl')

similarity = pickle.load(open("similarity.pkl",'rb'))

movies_list = df['title'].values

import streamlit as st

st.header("Netflix Recommender System")
selectvalue=st.selectbox("select movie from dropdown", df_list)

def recommend(movie):
    index= new_df[new_df['title'] == movie].index[0]
    distance = sorted(list(enumerate(similar[index])), reverse=True, key=lambda vector:vector[1])
    for i in distance[0:5]:
        print (new_df.iloc[i[0]].title)