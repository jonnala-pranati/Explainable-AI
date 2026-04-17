"""
Real ML Model Training Script for Sentiment Analysis
Trains a Logistic Regression model on IMDB-style reviews
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Create sample training data (you can replace with real dataset)
def create_sample_data():
    """Create sample training data for demonstration"""
    data = {
        'text': [
            # Positive reviews
            "This movie is absolutely amazing and wonderful",
            "I loved this film, great acting and plot",
            "Fantastic movie, best I've seen this year",
            "Excellent performance, highly recommended",
            "Great story, wonderful characters",
            "Amazing cinematography and direction",
            "Brilliant acting, loved every moment",
            "Outstanding movie, must watch",
            "Superb film, exceeded expectations",
            "Perfect movie, couldn't be better",
            
            # Negative reviews
            "This movie is terrible and awful",
            "I hated this film, bad script and acting",
            "Worst movie ever, complete waste of time",
            "Terrible plot, boring and predictable",
            "Awful acting, don't waste your money",
            "Horrible movie, very disappointing",
            "Disappointing film, not worth watching",
            "Bad direction, poor execution",
            "Waste of time, boring story",
            "Terrible experience, avoid this movie",
            
            # More positive
            "The movie was great, I really enjoyed it",
            "Wonderful film with great performances",
            "Excellent movie, highly entertaining",
            "Amazing story and great characters",
            "Love this movie, watch it now",
            
            # More negative
            "The movie was bad, I didn't like it",
            "Terrible film with poor acting",
            "Boring movie, waste of time",
            "Awful story, don't watch it",
            "Hate this movie, avoid it"
        ],
        'sentiment': [
            # 1 = Positive, 0 = Negative
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1,
            0, 0, 0, 0, 0
        ]
    }
    return pd.DataFrame(data)

def train_model():
    """Train sentiment analysis model"""
    print("🎬 Starting ML Model Training...")
    
    # Load data
    print("📊 Loading training data...")
    df = create_sample_data()
    
    # For real project, load from CSV:
    # df = pd.read_csv('imdb_dataset.csv')
    # df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})
    
    print(f"Dataset size: {len(df)} samples")
    print(f"Positive samples: {sum(df['sentiment'])}")
    print(f"Negative samples: {len(df) - sum(df['sentiment'])}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], 
        df['sentiment'], 
        test_size=0.2, 
        random_state=42,
        stratify=df['sentiment']
    )
    
    # Create vectorizer
    print("🔧 Creating vectorizer...")
    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),  # Unigrams and bigrams
        stop_words='english',
        min_df=2,
        max_df=0.95
    )
    
    # Fit and transform
    print("🔄 Vectorizing text...")
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Train model
    print("🤖 Training Logistic Regression model...")
    model = LogisticRegression(
        C=1.0,
        max_iter=1000,
        random_state=42,
        class_weight='balanced'
    )
    model.fit(X_train_vec, y_train)
    
    # Evaluate
    print("📈 Evaluating model...")
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))
    
    # Save model and vectorizer
    print("💾 Saving model and vectorizer...")
    os.makedirs("model", exist_ok=True)
    
    joblib.dump(model, "model/model.pkl")
    joblib.dump(vectorizer, "model/vectorizer.pkl")
    
    print("✅ Model training complete!")
    print("📁 Model saved to: model/model.pkl")
    print("📁 Vectorizer saved to: model/vectorizer.pkl")
    
    # Test prediction
    print("\n🧪 Testing predictions...")
    test_texts = [
        "This movie is amazing and wonderful",
        "This film is terrible and awful",
        "Great acting and plot",
        "Bad script and direction"
    ]
    
    for text in test_texts:
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]
        sentiment = "POSITIVE" if pred == 1 else "NEGATIVE"
        confidence = max(prob)
        print(f"'{text}' -> {sentiment} ({confidence:.2%})")

if __name__ == "__main__":
    train_model()
