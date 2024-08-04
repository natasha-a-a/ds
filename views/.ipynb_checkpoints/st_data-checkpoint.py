import streamlit as st
from PIL import Image
import pandas as pd
df = pd.read_csv("https://miscprojects.fra1.digitaloceanspaces.com/ds/combined_data.csv")


st.title("Data Exploration")

# Data Exploration page

st.write("In this section, we will explore the data related to dog expenses. Below is an overview of the final dataset created.")
st.dataframe(df.head())
st.image('https://miscprojects.fra1.digitaloceanspaces.com/ds/p6.jpg', caption='Proportion of Most Common Dog Breeds')
st.write("The plot above shows the proportion of the most common dog breeds in Germany.")
st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/p7.jpg", caption="Food Cost Year (avg) by Breed", use_column_width=True)
st.write("The second plot provides further insights into average food cost per year for certain breeds.")
st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/p8-2.jpg", caption="Tendency to Bark or Howl by Size", use_column_width=True)
st.write("The third plot shows the tendency of dogs to bark or howl based on their size category. This can be correlated with different temperaments, since behaviour-related variables are thus important to understand when it comes to the potential lifetime costs of owning a dog.")
