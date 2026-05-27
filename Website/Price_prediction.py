import pipeline
import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.set_page_config(page_title="Viz_demo")

st.title("Price Prediction Page")

columns = ['property_type',	'sector',	'bedRoom',	'bathroom',	'balcony',	'agePossession',	'built_up_area',	'servant room','store room',	'furnishing_type'	,'luxury_category'	,'floor_category']

with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipelines = pickle.load(file)

st.header('Enter your inputs')

property_pred = st.selectbox('Property type',['flat','house'])

sector_pred = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

bedroom_pred = int(st.selectbox('Bedroom', sorted(df['bedRoom'].unique().tolist())))

bathroom_pred = int(st.selectbox('Bathroom', sorted(df['bathroom'].unique().tolist())))

balcony_pred = st.selectbox('Balcony', sorted(df['balcony'].unique().tolist()))

agePossession_pred = st.selectbox('Age Possession', sorted(df['agePossession'].unique().tolist()))

built_up_area_pred = float(st.number_input('Built Up Area'))

servant_area_pred = int(st.selectbox('Servant room', [0,1]))

store_room_pred = int(st.selectbox('Store room', [0,1]))

furnishing_type_pred = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

luxury_prop_pred = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))

floor_cat_pred = st.selectbox('Floor category', sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):

    data = [[property_pred, sector_pred, bedroom_pred, bathroom_pred, balcony_pred, agePossession_pred, built_up_area_pred, servant_area_pred, store_room_pred, furnishing_type_pred, luxury_prop_pred, floor_cat_pred]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']
    df2 = pd.DataFrame(data, columns=columns)

    st.dataframe(df2)

    prediction = np.expm1(pipelines.predict(df2))[0]
    low = prediction-0.22
    high = prediction+0.22

    st.text('The price of the property is between {} Cr and {} Cr'.format(round(low,2),round(high,2)))
