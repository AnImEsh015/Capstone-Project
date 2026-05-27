import pipeline
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from fontTools.misc.bezierTools import approximateQuadraticArcLength

st.set_page_config(page_title="Recommend Apartments")

location_df = pickle.load(open('Dataset/location_distance.pkl', 'rb'))

st.title("Select Location and Radius")

selected_location = st.selectbox('Location',sorted(location_df.columns.to_list()))
selected_radius = st.number_input("Radius in kms")
if st.button('Search'):
    apartment = []
    result = location_df[location_df[selected_location] < selected_radius*1000][selected_location].sort_values()
    for keys,values in result.items():
        st.text((str(keys)+'-->'+str(round(values/1000))+ 'kms'))
