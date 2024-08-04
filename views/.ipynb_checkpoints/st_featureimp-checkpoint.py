import streamlit as st
from PIL import Image

st.header("Feature Importance and Correlation")
st.write("*This section provides insight into the feature importance considered before and after dimensionality reduction by principal component analysis (PCA) was applied. The correlation matrix demonstrates the relationship between features and the cost categories of the target variable.*")

st.subheader("Feature Importance - Top 50")
#st.write("TEXT ABOUT FEATURE IMPORTANCE-TOP 50")

st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/feature_importances_before_PCA_class.png", use_column_width=True)
st.subheader("Feature Selection")

st.write("The features were selected based on a threshold >= 0.01")
st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/feature_importances_after_selection_class.png", use_column_width=True)

st.subheader("Correlation Matrix")

#st.write("TEXT ABOUT FEATURE IMPORTANCE-TOP 50")
st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/correlation_matrix_with_target.png", use_column_width=True)