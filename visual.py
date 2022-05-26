import streamlit as st
# import plotly_express as px
import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
import plotly.figure_factory as  ff

st.title("Data Visualization App")

st.sidebar.subheader("visualization Settings")

global df
file= st.sidebar.file_uploader(label ="Upload your csv or Excel file.(200MB max)",
                         type=['csv','xlsx'])




if file is not None:
    print('hello')
    try:
        df =pd.read_csv(file)
    except Exception as e:
        print(e)
        df =pd.read_excel(file)
        
        
try:            
    st.write(df)
except Exception as e:
        print(e)
        st.write('Please upload file to the application.')
        


plt.rcParams['figure.figsize'] = (20, 9)
plt.style.use('fivethirtyeight')

color = plt.cm.spring(np.linspace(0, 1, 15))
df['PdDistrict'].value_counts().plot.bar(color = color)
plt.title('District with Most Crime',fontsize = 30,color = 'b')
plt.xticks(rotation = 90, color = 'b')
st.write(plt)    
# plt.rcParams['figure.figsize'] = (20, 9)
# df['Category']
# plt.title('Major Crimes in Sanfrancisco', fontweight = 30, fontsize = 20)
# plt.xticks(rotation = 90)
# plt.show()
# st.plotly_chart(plt)

    