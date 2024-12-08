import streamlit as st
import pandas as pd

data=pd.read_csv("spam.csv", encoding="latin-1")
st.write(data)