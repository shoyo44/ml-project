import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
st.title('Machine learning app')
st.info('Predicts info about penguins')
with st.expander('Data'):
  st.write('**Raw Data**')
  data=pd.read_csv("https://raw.githubusercontent.com/shoyo44/ml-project/refs/heads/master/penguins_data.csv")
  data
  st.write('**Independent Data (X)**')
  X_raw=data.drop(['species','Unnamed: 6'],axis=1)
  X_raw
  st.write('**Dependent Data (Y)**')
  Y_raw=data.species
  Y_raw
with st.expander('Data Visualization'):
  st.scatter_chart(data=data,x='body_mass_g',x_label="Body Mass",y='flipper_length_mm',y_label="Flipper Length",color='species')
  st.line_chart(data=data,x='species',x_label="Species",y='island',y_label="Island")
  st.bar_chart(data=data,x='species',y='island',color='sex') 
with st.sidebar:
  st.header('Input features')
  island=st.selectbox('Island',('Torgersen', 'Biscoe', 'Dream'))
  bill_length_mm=st.slider('Bill Length',32.1,59.6,43.9)
  flipper_length_mm=st.slider('Flipper Length',172.0,231.0,200.9)
  body_mass_g=st.slider('body_mass',2700.0,6300.0,4207.0)
  bill_depth_mm=st.slider('Bill Depth',13.1,21.5,17.1)
  sex=st.selectbox('Gender',('Male','Female'))
dff={'island':island,
    'bill_length_mm':bill_length_mm,
    'flipper_length_mm':flipper_length_mm,
    'body_mass_g':body_mass_g,
    'bill_depth_mm':bill_depth_mm,
    'sex':sex}
input_data=pd.DataFrame(dff,index=[0])
input_penguins=pd.concat([input_data,X_raw],axis=0)
with st.expander('Input Features'):
  st.write("**Input Data**")
  input_data
  st.write("**Combined data**")
  input_penguins


encode=['island','sex']
df_penguins=pd.get_dummies(input_penguins,prefix=encode)

input_a=df_penguins[:1]
x=df_penguins[1:]
target_dict={'Adelie':0, 'Gentoo':1, 'Chinstrap':2}
def encode_x(val):
  return target_dict[val]
input_enc=Y_raw.apply(encode_x)
with st.expander('Data Preparation'):
   st.write("**Encoded Independent Values (X)**")
   input_a
   st.write('**Encoded Dependent Values (Y)**')
   input_enc
clf = RandomForestClassifier()
clf.fit(x,input_enc)
prediction=clf.predict(input_a)
prob=clf.predict_proba(input_a)
data_f=pd.DataFrame(prob)
data_f.columns = ['Adelie', 'Chinstrap', 'Gentoo']
st.subheader("**Pediction of Species**")
st.write("**Enter the info of the Species**")
input_data
st.dataframe(data_f, column_config={
           "Adelie": st.column_config.ProgressColumn('Adelie',
                                                     format='%f',
                                                     min_value=0,
                                                     max_value=1),
           "Gentoo": st.column_config.ProgressColumn('Gentoo',
                                                     format='%f',
                                                     min_value=0,
                                                     max_value=1),
            "Chinstrap": st.column_config.ProgressColumn('Chinstrap',
                                                     format='%f',
                                                     min_value=0,
                                                     max_value=1)}
             ,hide_index=True)
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(str(penguins_species[prediction][0]))

 

                       

