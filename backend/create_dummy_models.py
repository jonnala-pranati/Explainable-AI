"""
Script to create dummy model files for testing the FastAPI backend.
This creates placeholder model.pkl and vectorizer.pkl files.
"""
import joblib
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

# Create model directory
os.makedirs("model", exist_ok=True)

# Create a simple dummy vectorizer
print("Creating dummy vectorizer...")
vectorizer = CountVectorizer(max_features=1000)
# Fit on some sample data
sample_texts = [
    "This movie is amazing and wonderful",
    "This film is terrible and awful",
    "Great acting and plot",
    "Bad script and direction",
    "I loved this movie",
    "I hated this film"
]
vectorizer.fit(sample_texts)

# Create a simple dummy model
print("Creating dummy model...")
model = LogisticRegression()
X = vectorizer.transform(sample_texts)
y = np.array([1, 0, 1, 0, 1, 0])  # 1 for positive, 0 for negative
model.fit(X, y)

# Save the models
print("Saving models...")
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Dummy models created successfully!")
print("You can now start the FastAPI server.")
