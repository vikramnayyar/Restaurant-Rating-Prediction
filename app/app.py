"""
Created on Wed Sep  8 16:09:06 2021

@author: matsya
"""
import pandas as pd
import streamlit as st
import pickle as pkl
import numpy as np


def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset

data_link = '../data/clean_data.csv'
# data_link = 'zomato_renamed.csv'
df = load_dataset(data_link)

st.title("Rating Prediction for a Bangalore Restaurant")
st.write("This app is based on 6 inputs; that accurately predict the Rating of a Bangalore Restaurant. \n\n Using this app, a restaurant easiliy identifies the features improving the restaurant's rating. Subsequently, a large customer volumes are attracted. \n\n Please use the following form to get started!")     

# st.write("The model is designed on dataset related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.")   

# st.write("")
# st.write('https://archive.ics.uci.edu/ml/datasets/Bank+Marketing')
st.markdown("""
<style>
.big-font {
    font-size:15px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">(NOTE: By default usual values are selected in the form. For convinience, user can select few fields and leave other fields with general inputs.)</p>', unsafe_allow_html=True)



# selecting online order status
st.subheader("Does restaurant provides online orders?")
selected_order = st.radio(" ", df['online_order'].unique(), index = 1)
st.write("Selected Response:", selected_order)


## Encode the job entered by user
### Declaring function for encoding
def encode_order(selected_item):
    dict_order = {'Yes.':0, 'No':1}
    return dict_order.get(selected_item, 'No info available')

### Using function for encoding
selected_order = encode_order(selected_order)  




# selecting booking status
st.subheader("Does restaurant provide booking?")
selected_book = st.radio("", df['book_table'].unique(), index = 1)
st.write("Selected Response:", selected_book)


## Encode the job entered by user
### Declaring function for encoding
def encode_book(selected_item):
    dict_book= {'Yes.':0, 'No':1}
    return dict_book.get(selected_item, 'No info available')

### Using function for encoding
selected_book = encode_book(selected_book)  



# selecting votes
st.subheader("How many votes have restaurant received?")
selected_votes = st.slider('', min_value = df['votes'].min(), 
                            max_value = df['votes'].max(), step = 1, 
                            value = 283)
st.write("Selected Votes:", selected_votes)



# selecting cost
st.subheader("What is approximate cost of Restaurant?")
selected_cost = st.slider('', min_value = 500,
          max_value = 10000, step = 1, value = 2000)
st.write("Selected Cost:", selected_cost)



# selecting location
st.subheader("What is Restaurant's location?")

# file = open('../dict/locations_dict.pkl', 'rb')
# locations = pkl.load(file)

locations = df.location.unique()
selected_location = st.selectbox("", locations)



# Encode the location entered by user
def encode_location(selected_item):
    
    file = open('../dict/locations_dict.pkl', 'rb')
    dict_loc = pkl.load(file) 
    
    return dict_loc.get(selected_item, 'No info available')

selected_location = encode_location(selected_location)

    


# selecting restaurant type
st.subheader("What is Restaurant type?")

# file = open('../dict/rest_type.pkl', 'rb')
# rest_types = pkl.load(file)

rest_types = df.rest_type.unique()

selected_type = st.selectbox("", rest_types)
st.write("Selected Type:", selected_type)


# Encode the location entered by user
def encode_type(selected_item):
    
    file = open('../dict/rest_type_dict.pkl', 'rb')
    dict_type = pkl.load(file) 
    
    return dict_type.get(selected_item, 'No info available')

selected_type = encode_type(selected_type)




pickle_in = open("../model/model.pkl","rb")
regressor = pkl.load(pickle_in)


prediction = regressor.predict([[selected_order, selected_book, selected_votes, selected_location, selected_type, selected_cost]])



# Adding Predict Button
predict_button = st.button('Predict')
# st.write(predict_button)

if predict_button:
    st.success(f"The predicted rating is: {prediction}")

# if predict_button:
#     if(prediction == 1):
#         st.success('This customer segment will Deposit')
#     else:
#         st.success('This customer segment will NOT Deposit')    




# References:
#     1. https://www.youtube.com/watch?v=JwSS70SZdyM&ab_channel=freeCodeCamp.org
#     2. https://towardsdatascience.com/build-your-first-interactive-data-science-web-app-with-streamlit-d4892cbe4792
#     3. https://www.kaggle.com/amlanmohanty1/build-web-app-for-heart-disease-with-streamlit#Let's-save-our-model-using-pickle
#     4. https://medium.com/swlh/3-alternatives-to-if-statements-to-make-your-python-code-more-readable-91a9991fb353
#     5. https://stackoverflow.com/questions/51102205/how-to-know-the-labels-assigned-by-astypecategory-cat-codes
