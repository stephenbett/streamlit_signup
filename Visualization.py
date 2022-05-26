from distutils.command.upload import upload
from functools import cache
from pickle import GLOBAL
import matplotlib
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
matplotlib.use("Agg")
import pydeck as pdk
# import seaborn as sns
# import plotly.figure_factory  as ff



def app():
    st.title('Visualization')
    

@st.cache
def san():
     san = pd.read_csv("Police_Department_Incidents_-_Previous_Year__2016_.csv")
     return st.write(san.head(200))
 

     
visual_header = st.container()
bar =st.container()
histogram =st.container()
uploader = st.container()
with visual_header:

    san = pd.read_csv("Police_Department_Incidents_-_Previous_Year__2016_.csv")
    st.write(san.head(200))

with  bar:
    data =pd.read_csv("data.csv")
    st.write(data)
    # data.bar_chart()
    plt.show()
    # st.plotly_chart()
    # st.bar_chart(data['Category','DayOfWeek'])
    
with histogram:
   sann= pd.read_csv("Police_Department_Incidents_-_Previous_Year__2016_.csv"[:200]) 
   sann.hist()
   plt.show()
   st.pyplot()
    


with uploader:
    # uploader_file =st.sidebar.file_uploader(
    #     label="Upload your CSV or Excel file",
    #     type=['csv','xlsx'])
    # san = pd.read_csv("Police_Department_Incidents_-_Previous_Year__2016_.csv")
    @st.cache
    def data():
        data =pd.read_csv('data.csv')
        st.write(data.head(20))
        numeric_columns =list(data.select_dtypes(['float','int']).columns)
        chart_select = st.sidebar.selectbox(
            label="Select the chart type",
            options=['Scatterplots','Lineplots','Histogram','Boxplot','Heatmap','Bargraph']
        )
        
        if chart_select == 'Scatterplots':
            st.sidebar.subheader("Scatterplot settings")
            x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
            y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
            plot =plt.scatter(san, x=x_values, y=y_values)
            st.plotly_chart(plot)
        elif chart_select == 'Lineplots':
            st.sidebar.subheader("Lineplots settings")
            x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
            y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
            plot =plt.scatter(san, x=x_values, y=y_values)
            st.plotly_chart(plot)
        elif chart_select == 'Histogram':
            st.sidebar.subheader("Histogram settings")
            x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
            y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
            plot =plt.scatter(san, x=x_values, y=y_values)
            st.plotly_chart(plot)