import streamlit as st
import numpy as np
import pandas as pd

st.title('Machine learning app')
st.info('Predicts species about penguins')
with st.expander('Data'):
  st.write('**Raw Data**')
  data=pd.read_csv("https://raw.githubusercontent.com/shoyo44/ml-project/refs/heads/master/penguins_data.csv")
  data
  st.write('**Dependent Data (X)')
  X_raw=data.drop(['Species'],axis=1)

