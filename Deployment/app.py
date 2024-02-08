#Import Library
import streamlit as st

#Import file lainnya
import eda
import prediction

#sidebar
page = st.sidebar.selectbox('Pilih Halaman : ', ('EDA', 'Prediction'))

#Run page jika menu side bar di pilih
if page == 'EDA' : 
    eda.run()
else:
    prediction.run()