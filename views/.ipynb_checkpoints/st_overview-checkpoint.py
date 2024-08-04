import streamlit as st
from PIL import Image

st.title("Pet Expense Management")
st.write("### About the Project")
col1, col2 = st.columns([1,2])
cover = Image.open('/Users/natashaaa/ds/may24_bds_int_pet_expense/src/streamlit/cover.png') 
col1.image(cover, caption=None,)
col2.write(
        """
        This presentation is the culmination of a three-month data science group project completed with DataScientest as part of a bootcamp. 
        
        The Pet Expense Management concept has its origins in the business case of Paw à Peau, which is building a platform to convert pet data into actionable insights for pet owners. 
        
        The project’s challenge was to
        translate the benefits of collecting data into financial terms and create an anomaly-based alert system.
        """)
st.write("""
        The project consisted of three phases:
        - Data exploration
        - Data modelling
        - Project defense
        """)
col3, col4 = st.columns([1,1])
col4.download_button(label="Download Report",
        data=PDFbyte,
        file_name="https://miscprojects.fra1.digitaloceanspaces.com/ds/final_report.pdf,
        mime='application/octet-stream')
col3.link_button("View Source Code", "https://github.com/DataScientest-Studio/may24_bds_int_pet_expense")

