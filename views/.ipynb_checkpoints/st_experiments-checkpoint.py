import streamlit as st
from PIL import Image

st.title("Experiments")
col1, col2, col3 = st.columns([1,3,1])
col1.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/Husky.png")
col2.write("""
We were convinced that our advanced models suffered from overfitting and so we examined the performance of other models. Another strategy we employed was to play around with the dataset and variables. We split the dataset vertically in order to test for variable bias. We further removed the "breed" variable and substituted it with groups of breeds. We also binarized the target variable, changed the target variable (to predict "breed"), and reorganized the breed groups.
""") 
col3.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/German_Shepherd.png")

st.subheader("Classification Model Performance")

st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/acc_score_experiment.JPG", caption="Classification Model Performance")
    
# Display the second table image
st.subheader("Random Forest - Regression Model Performance")
st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/regression_rf.JPG", caption="Regression Model Performance")