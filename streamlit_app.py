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
  X_raw=data.drop('species',axis=1)
  X_raw
  st.write('**Dependent Data (Y)**')
  Y=data.species
  Y
with st.expander('Data Visualization'):
  st.scatter_chart(data=data,x='body_mass_g',x_label="Body Mass",y='flipper_length_mm',y_label="Flipper Length",color='species')
  st.line_chart(data=data,x='species',x_label="Species",y='island',y_label="Island")
  st.bar_chart(data=data,x='species',y='island',color='sex') 
with st.sidebar('Input Features'):
  st.selectbox('species',('Adelie', 'Gentoo', 'Chinstrap'))
