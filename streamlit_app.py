import streamlit as st
import numpy as np
import pandas as pd

st.title('Machine learning app')
st.info('Predicts species about penguins')
with st.expander('Data'):
  st.write('**Raw Data**')
  data=pd.read_csv("https://raw.githubusercontent.com/shoyo44/ml-project/refs/heads/master/penguins_data.csv")
  data
  st.write('**Indepemdent Data (X)**')
  X_raw=data.drop(['species','Unnamed: 6'],axis=1)
  X_raw
  st.write('**Dependent Data (Y)**')
  Y=data.species
  Y
with st.expander('Data Visualization'):
  st.scatter_chart(data=data,x='body_mass_g',x_label="Body Mass",y='flipper_length_mm',y_label="Flipper Length",color='species')
  st.line_chart(data=data,x='species',x_label="Species",y='island',y_label="Island")
  st.bar_chart(data=data,x='species',y='island',color='sex') 
with st.sidebar:
  st.header('Input features')
  island=st.selectbox('Island',('Torgersen', 'Biscoe', 'Dream'))
  bill_length_mm=st.slider('Bill Length',5.4,333,75)
  flipper_length_mm=st.slider('Flipper Length',14.01,,333,193)
  body_mass_g=st.slider('body_mass',333,6300,3340)
  bill_depth_mm=st.slider('Bill Depth',1.9,,333,54)
  sex=st.selectbox('Gender',('Male','Female'))


