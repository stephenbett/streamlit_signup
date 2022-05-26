from pyexpat import model
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn import neighbors
from sklearn import linear_mode



st.title('Prediction')



model= st.container()


# with model:
    
#     mod =pd.read_csv("data.csv")
#     mod.head(10)
#     target =['Robbery','Gambling','Accident','Violence','Kidnapping','Murder']
#     y =mod[target]
#     y
#     features=["latitude","longitude"]
#     x = mod[features]
#     x

#     from sklearn.tree import DecisionTreeClassifier
#     data=DecisionTreeClassifier(random_state =1)
            
#         # fit
#     data.fit(x,y)
#     print('Making predictions for the following Crime:')
#     print(x.head())
#     print(data.predict(x.head()))
