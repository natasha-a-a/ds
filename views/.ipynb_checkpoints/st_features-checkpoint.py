import streamlit as st
from PIL import Image

st.title("Feature Engineering")

st.write(
        """

Our biggest challenge and the most time-consuming part of the project was the data preparation. We joined many different datasets and went through an extensive feature engineering process due to missing, dirty, or incorrectly formatted
data. 
""")

st.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/pem_datamap.jpg")

st.subheader("Data Enrichment")

st.write("""
To begin with, the financial data available in the foundation dataset was incomplete and based on dogs living in the US: the costs were not at all accurate for Germany. So, we enriched the dataset with financial data from German scientific literature, our own primary research within the Berlin pet community and our own calculations for training and medical costs. Following the calculations of individual genetic ailments and common training costs (local cost data in Berlin was used) to address certain behavioural
problems, we removed all cost data apart from *yearly_final_costs*, which we used as our target variable.
""")

st.subheader("Resampling")
st.write("""

We further standardized the data by ensuring certain thresholds for breed inclusion in the dataset, this
included the minimum number of dogs which belonged to a given breed population (>=100 records), as well as
the acceptable amount of missing key data. For example, dog breeds missing our key behaviour
traits were dropped from the dataset. 

""")


col1, col2, col3 = st.columns([1,1,1])
col2.image("https://miscprojects.fra1.digitaloceanspaces.com/ds/Poodle.png", caption='Poodles unfortunately did not make the cut!', width=200)

st.subheader("Standardization")

st.write("""

We chose to represent mixed breeds by splitting them into three different size categories and using the mode for missing data, i.e. for behaviour traits, as well as figures from research findings such as longevity, reduced insurance cost. We made the decision not to associate the mixed breed population with any specific genetic ailments.

""")

st.subheader("Transformation")


st.write("""

The foundation dataset had provided breed categorization based on the American Kennel Club, but we later changed this to the categorization provided by the Fédération Cynologique Internationale (an umbrella organization governing pedigree dogs in most of regions of the world) as these were breed function-specific and more relevant to Germany.

""")

st.subheader("Dimensionality Reduction")

st.write("""    
We dropped the following variables, due to better representation through other variables, irrelevance or insufficient data:
- *neutered*
- *grooming_required*
- *food_cost_year*
- *lifetime_cost*
- *adapts_well_to_apartment_living*
- *bite_statistics*

""")

st.subheader("One-Hot Encoding")

st.write("""

As a final step, we expanded 'breed' and ‘genetic_ailments’ through one hot encoding in order to have a more
detailed breakdown of the costs and to transform different breeds into variables. 

        """)