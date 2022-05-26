import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def app():
    st.title('Data')

header = st.container()
info =st.container()
description = st.container()
shapes= st.container()
null= st.container()
not_null= st.container()
colmn =st.container()
pred = st.container()


with header:
    st.title("DATA SET")
    san = pd.read_csv("Police_Department_Incidents_-_Previous_Year__2016_.csv")
    st.write(san.head(200))
with colmn:
    st.write(san.columns)

with info:
    st.subheader("Data information")
    st.write(san.info())

with  description:
    st.subheader("Describing the Data")
    st.write(san.describe())

with shapes:
    st.subheader("Data Shape")
    san.shape

with null:
    st.subheader('Checking if there are any null values')
    st.write(san.isnull().sum())
    

with pred:
    st.header("Data for Prediction")
    data =pd.read_csv("data.csv")
    st.write(data.head())
    
# with not_null:
#     st.subheader("Removing null values")
#     san1=st.write(san.dropna())
#     st.write(san1.isnull())