import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("Analysis Page")
#CHOROPETH_MAP
st.subheader('Choropleth map')
st.set_page_config(page_title='Plotting Demo')
lat_long_df = pd.read_csv('Dataset/lat_long_df.csv')
group_df = lat_long_df.groupby('sector')[['price','built_up_area','latitude','longitude']].mean()

figure = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
st.plotly_chart(figure,use_container_width=True)

#WORD_CLOUD
wordcloud_df = pd.read_csv('Dataset/WordCloudFinal.csv')
st.subheader('Word cloud map')
option = st.selectbox(
    "Select Sector",
    wordcloud_df['sector']
)

if st.button("Find Word Cloud"):
    selected_sector = wordcloud_df[wordcloud_df['sector'] == option]
    text = selected_sector['furnishDetail'].to_string()
    wordcloud = WordCloud(
        width=400,
        height=400,
        background_color='white'
    ).generate(text)

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    st.pyplot(fig)

#Area vs Price graph
df_new = pd.read_csv('Dataset/gurgaon_properties_post_feature_selection_v2.csv')
st.header("Area vs Price")

option = st.selectbox("Select Property Type",['house','flat'])
if option == 'house':
    df1 = df_new[df_new['property_type']=='house']
    fig1 = px.scatter(df1,x=df1['built_up_area'],y=df1['price'],color='bedRoom',title='Area vs Price',width=800,height=400)
    st.plotly_chart(fig1,use_container_width=True)
else:
    df2 = df_new[df_new['property_type']=='flat']
    fig1 = px.scatter(df2, x=df2['built_up_area'], y=df2['price'], color='bedRoom', title='Area vs Price', width=1000,
                      height=500)
    st.plotly_chart(fig1, use_container_width=True)

#Pie plot for number of rooms in a flat
st.header("Number of rooms in a flat")
total_option = df_new['sector'].unique().tolist()
total_option.insert(0,'Overall')
options = st.selectbox('Select Sector',total_option)

if options == 'Overall':
    fig2 = px.pie(df_new, names = df_new['bedRoom'],width = 600,height=400)
    st.plotly_chart(fig2, use_container_width=True)

else:
    fig3 = px.pie(df_new[df_new['sector']==options], names='bedRoom', width=600, height=400)
    st.plotly_chart(fig3, use_container_width=True)


# Side by side BHK price comparison

st.header('Side by side BHK price comparison')
fig4 = px.box(df_new[df_new['bedRoom']<=4],x='bedRoom',y='price')
st.plotly_chart(fig4, use_container_width=True)

#Distplot
st.header("Side by side Distplot for property type")
fig4 = plt.figure(figsize=(10,4))
sns.distplot(df_new[df_new['property_type']=='house']['price'],label='House')
sns.distplot(df_new[df_new['property_type']=='flat']['price'],label='Flat')
plt.legend()
st.pyplot(fig4)


