import streamlit as st
import pickle

# Load saved pipeline
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page setup
st.set_page_config(page_title="SMS Spam Detector", layout="centered")

st.title("SMS Spam Detector")
st.write("Enter a message below and click Predict.")

user_input = st.text_area("Message")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([user_input])[0]

        if prediction == 1:
            st.error("This message is SPAM.")
        else:
            st.success("This message is HAM.")