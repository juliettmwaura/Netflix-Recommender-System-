import streamlit as st
import pickle
import pandas as pd

print(pickle.format_version)

df = pd.read_pickle('movie_data.pkl')
print (df)