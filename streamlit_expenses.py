import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from PIL import Image


# Dataset manipulation
df = pd.read_csv("train.csv")
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

# Set the title of the sidebar
st.sidebar.title("Navigation")
# Define the page navigation options
pages = ["Introduction", "Business Case", "Feature Engineering", "Data Exploration", "Modelling", "App Prototype"]

# Create a radio button for page navigation in the sidebar
page = st.sidebar.radio("Go to", pages)


# Main page 
if page == pages[0] : 
# Set the title of the main page
    st.title("Pet Expenses Management")    
    st.write("### Introduction")
    st.dataframe(df.head(10))
    st.write(df.shape)
    st.dataframe(df.describe())
    
    if st.checkbox("Show NA") :
        st.dataframe(df.isna().sum())

if page == pages[1] : 
# Set the title of the main page
    st.title("Business Case")    
    st.write(
        """
        Since the pandemic, pet ownership has skyrocketed and all segments of the pet industry 
        (from retail to pet services and emerging technologies) are currently booming in the United States. 
        Europe is following closely behind, with the UK, Germany, and France as the biggest and fastest growing markets. 
        Germany is the EU’s largest economy but has been hit hard by rising costs stemming from energy prices, inflation, 
        and financial side effects from ongoing regional wars. Two steep increases in the national veterinary tariffs 
        within the last three years mean pet owners (47% of Germany’s population) are under financial pressure.
        """
    )

if page == pages[2] : 
        st.write("Feature Engineering")

 
elif page == "Data Exploration":
    st.header("Data Exploration")
    st.write(
        """
        In this section, we will explore the data related to dog expenses.
             
        Below is an overview of the final dataset created.
        """
    )
    #display dataframe
    st.dataframe(head(df)) #check if it is right
    #display chart of proportion of most common dog breeds
    image1 = Image.open('p6.jpg') #add correct name of the saved images
    st.image(image1, caption='Proportion of Most Common Dog Breeds')
    #display some text between images
    st.write(
        """
        The plot above shows the proportion of the most common dog breeds in Germany.
        """
    )
    #Load and display the second image
    image2 = Image.open("p7.jpg")  
    st.image(image2, caption="Food Cost Year (avg) by Breed", use_column_width=True)

    # Additional text or analysis can go here
    st.write(
        """
        The second plot provides further insights into average food cost per year for certain breeds.
        """
    ) # check if it is correct the description
  # Load and display the third image
    image3 = Image.open("p8-2.jpg")  
    st.image(image2, caption="Tendency to Bark or Howl by Size", use_column_width=True)
  # Additional text or analysis can go here
    st.write(
        """
        The third plot shows the tendency of dogs to bark or howl based on their size category.
        This can be correlated with different temperaments, since behaviour-related variables are thus important to understand 
        when it comes to the potential lifetime costs of owning a dog.
        """
    ) # check if it is correct

elif page == "Modelling":
    st.header("Modelling")
    
    


# DataViz page 
elif page == pages[4] : 
        st.write("### Presentation of data")
    
        fig = plt.figure()
        sns.countplot(x = 'Survived', data = df)
        st.pyplot(fig)

        gig = plt.figure()
        sns.countplot(x = 'Sex', data = df)
        plt.title("Distribution of the passengers gender")
        st.pyplot(fig)

        fig = plt.figure()
        sns.countplot(x = 'Pclass', data = df)
        plt.title("Distribution of the passengers class")
        st.pyplot(fig)

        fig = sns.displot(x = 'Age', data = df)
        plt.title("Distribution of the passengers age")
        st.pyplot(fig)
    
        fig = plt.figure()
        sns.countplot(x = 'Survived', hue='Sex', data = df)
        st.pyplot(fig)

        fig = sns.catplot(x='Pclass', y='Survived', data=df, kind='point')
        st.pyplot(fig)

        fig = sns.lmplot(x='Age', y='Survived', hue="Pclass", data=df)
        st.pyplot(fig)

        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), ax=ax)
        st.write(fig)


# Modelling page 
if page == pages[2] : 
    st.write("### Modelling of data")
    
# Train model
    y = df['Survived']
    X_cat = df[['Pclass', 'Sex',  'Embarked']]
# Drop unnecessary variables
    X_num = df[['Age', 'Fare', 'SibSp', 'Parch']]
# Encode 
    for col in X_cat.columns:
      X_cat[col] = X_cat[col].fillna(X_cat[col].mode()[0])
    for col in X_num.columns:
      X_num[col] = X_num[col].fillna(X_num[col].median())
    X_cat_scaled = pd.get_dummies(X_cat, columns=X_cat.columns)
    X = pd.concat([X_cat_scaled, X_num], axis = 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    scaler = StandardScaler()
    X_train[X_num.columns] = scaler.fit_transform(X_train[X_num.columns])
    X_test[X_num.columns] = scaler.transform(X_test[X_num.columns])

    def prediction(classifier):
        if classifier == 'Random Forest':
            clf = RandomForestClassifier()
        elif classifier == 'SVC':
            clf = SVC()
        elif classifier == 'Logistic Regression':
            clf = LogisticRegression()
        clf.fit(X_train, y_train)
        return clf

    def scores(clf, choice):
        if choice == 'Accuracy':
            return clf.score(X_test, y_test)
        elif choice == 'Confusion matrix':
            return confusion_matrix(y_test, clf.predict(X_test))


    choice = ['Random Forest', 'SVC', 'Logistic Regression']
    option = st.selectbox('Choice of the model', choice)
    st.write('The chosen model is :', option)

    clf = prediction(option)
    display = st.radio('What do you want to show ?', ('Accuracy', 'Confusion matrix'))
    if display == 'Accuracy':
        st.write(scores(clf, display))
    elif display == 'Confusion matrix':
        st.dataframe(scores(clf, display))

elif page == "App Prototype":
    st.header("Conclusion")
    st.write("Concluding remarks...")
    st.header("Data Concept")
    st.write(
        """ WRITE TEXT HERE
        """
        )
    image3 = Image.open('/Users/natashaaa/ds/may24_bds_int_pet_expense/reports/figures/wfinput.jpg') #add correct name of the saved images
    st.image(image3, caption='Expense Risk Estimator')
    st.write(
        """ WRITE TEXT HERE
        """
        )
    image4 = Image.open('/Users/natashaaa/ds/may24_bds_int_pet_expense/reports/figures/wfresult.jpg') #add correct name of the saved images
    st.image(image4, caption='Expense Risk Result')

#cache memory
st.cache_data