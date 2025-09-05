import numpy as np
import pandas as pd
import pickle
import streamlit as st


st.title("📩Spam Email Classification App")

st.write("""This app classifies emails as Spam or Not Spam using a pre-trained model. 
It uses a Logistic Regression model trained on a dataset of emails.""")
# -----> load the model and vectorizer
# If You Used a CountVectorizer or TfidfVectorizer Before Training:
# You must transform the new input using the same vectorizer before passing it to the model.
# save model
with open("Logistic_model.pkl", "wb") as f:
    pickle.dump(model, f)

# save vectorizer
with open("cv_model.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
    
# load model
with open("Logistic_model.pkl", "rb") as file:
    loaded_model = pkl.load(file)

# load vectorizer
with open("cv_model.pkl", "rb") as file:
    vectorizer = pkl.load(file)


# Sample input (ensure it's string)
user_input = str(st.text_area("__Enter email text here__"))

# Transform before prediction
if st.button("Predict"):
    st.write("Processing your input...")
    if user_input.strip() != "":
        input_transformed = vectorizer.transform([user_input])  # now numeric format
        prediction = loaded_model.predict(input_transformed)[0]

        if prediction == 1:
            st.error("🚨 This is a Spam message!")
        else:
            st.success("✅ This is Not Spam.")
    else:
        st.warning("Please enter some text.")

# Get the current date
current_year = pd.to_datetime("today").year
st.write(f"© {current_year} Spam Email Classification App")
st.divider()
# Display the current year in the footer

st.markdown("_Made with ❤️ by Ebunlicious_")






