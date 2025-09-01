from flask import Flask, request, jsonify
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

app = Flask(__name__)

#  Load model and tokenizer
model = load_model('D:/Projects/review-rating-system/ml_model/deep_models/bilstm_model_imbalanced.h5')
tokenizer = joblib.load('D:/Projects/review-rating-system/ml_model/deep_models/tokenizer_bilstm.pkl')

# Text cleaning
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('review', '')

    review_clean = clean_text(review)
    sequence = tokenizer.texts_to_sequences([review_clean])
    padded = pad_sequences(sequence, maxlen=200, padding='post', truncating='post')

    prediction = model.predict(padded)
    predicted_class = int(np.argmax(prediction)) + 1  # Ratings are 1–5

    return jsonify({'predicted_rating': predicted_class})

# Startup log
if __name__ == '__main__':
    print(" BiLSTM model and tokenizer loaded. API is running at http://127.0.0.1:5000")
    app.run(debug=True)