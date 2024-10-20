import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.pipeline.predict_pipeline import CustomData, Pipeline
from src.utils import show_error

# Title of the Streamlit web app
st.title("Spam Mail Classifier")

# Instructions for the user
st.write("Enter a message in the box below, and the app will classify it as either Spam or Not Spam.")

# Input text area for the user to enter their message
message = st.text_area("Message:", placeholder="Type your message here...")

# When the user clicks the 'Classify' button, we perform prediction
if st.button("Classify"):
    if message:
        try:
            # Preparing the input for prediction
            data = CustomData(message)
            list_message = data.get_data_as_list()
            predict_pipeline = Pipeline()
            result = predict_pipeline.predict_spam_or_not(list_message)

            # Interpreting the result (assuming 0 = Spam, 1 = Not Spam)
            if result[0] == 0:
                st.error("This message is classified as: Spam")
            else:
                st.success("This message is classified as: Not Spam")
        except Exception as e:
            show_error(e, sys)
            st.error("An error occurred during the prediction.")
    else:
        st.warning("Please enter a message to classify.")
