# SMS Spam Detector

A beginner-friendly machine learning project that classifies SMS messages as spam or ham using Python, scikit-learn, and Streamlit.

## Features
- Classifies SMS text as spam or ham
- Uses TF-IDF for text vectorization
- Uses Naive Bayes for prediction
- Includes a simple Streamlit front end

## Files
- `app.py` - Streamlit app
- `spam.ipynb` - Jupyter notebook for training and experimentation
- `spam_model.pkl` - Saved trained model
- `spam.csv` - Dataset
- `requirements.txt` - Python dependencies

## Technologies Used
- Python
- pandas
- scikit-learn
- Streamlit

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

## Dataset
This project uses the SMS Spam Collection dataset.

## Project Goal
The goal of this project is to build a simple end-to-end NLP application that takes a message as input and predicts whether it is spam or ham.