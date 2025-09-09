Intelligent Email Classifier: Streamlit-based app that detects spam in real time using natural language processing and machine learning.
Explore the deployed web app here: Intelligent Email Classifier Project

**Intelligent Email Classifier** is a simple web application built with streamlit that detects whether a message is spam or not. 
It uses natural languge processing (NLP) and machine learning techniques to classify text messages in real-time.

**Features**  

Real-time Dectection = Receives any text message and instantly determine the category (spam or not spam)  
ML Powered = It is trained with scikit-learn using TF-IDF vectorization.  
Interactive Web App = Built wit streamlit for a clean and responsive interface.  
Model Persistence = Uses joblib library to save and load the trained mdel efficiently.  
Deployment = Deploy on Streamlit Cloud for global access.  

**Tech Stack**  
Python  
Streamlit  
Scikit-learn  
NLTK  
Pandas   
Numpy  
  
**Installation & Setup Guide**  

Clone this repository  

"git clone https://github.com/ebytt/intelligent_email_classifier.git
cd spamshield""  


Create and activate a virtual environment (recommended)  

python -m venv venv  
source venv/bin/activate   # On Linux/Mac  
venv\Scripts\activate      # On Windows  


Install dependencies  

pip install -r requirements.txt  


Run the app  

streamlit run app.py  


Open the link in your browser (usually http://localhost:8501).  

Project Structure  
📂 Intelligent Email Classifier  
 ├── spam_app.py          # Streamlit app script  
 ├── logistic_model.pkl   # Trained ML model  
 ├── cv_model.pkl         # TD-IDF vectorizer
 ├── requirements.txt     # Dependencies  
 └── README.md            # Project documentation

**Usage Example**

__Input__: “Congratulations! You’ve won a free ticket. Call now!”

__Output__: Spam 🚫

__Input__: “Let’s meet tomorrow at 5pm.”

__Output__: Not Spam (Ham) ✅

**Future Improvements**

-Add deep learning support with LSTMs or Transformers.

-Expand dataset for better accuracy.
