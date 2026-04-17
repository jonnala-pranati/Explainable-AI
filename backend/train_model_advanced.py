"""
Advanced ML Model Training with Real Dataset
Supports IMDB dataset and custom datasets
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib
import os
import argparse

def load_imdb_dataset(csv_path=None):
    """
    Load IMDB dataset from CSV file.
    Expected format: CSV with 'review' and 'sentiment' columns
    Sentiment should be 'positive' or 'negative'
    """
    if csv_path and os.path.exists(csv_path):
        print(f"📊 Loading dataset from {csv_path}...")
        df = pd.read_csv(csv_path)
        
        # Map sentiment to numbers
        if 'sentiment' in df.columns:
            df['label'] = df['sentiment'].map({'positive': 1, 'negative': 0})
        elif 'label' not in df.columns:
            raise ValueError("CSV must have 'sentiment' column")
        
        # Use 'review' or 'text' column
        text_col = 'review' if 'review' in df.columns else 'text'
        if text_col not in df.columns:
            raise ValueError("CSV must have 'review' or 'text' column")
        
        df = df.rename(columns={text_col: 'text'})
        return df[['text', 'label']]
    else:
        print("⚠️  No dataset file found, using sample data")
        return create_sample_data()

def create_sample_data():
    """Create sample training data"""
    data = {
        'text': [
            # Positive reviews (more diverse)
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
            "The movie was great, I really enjoyed it",
            "Wonderful film with great performances",
            "Excellent movie, highly entertaining",
            "Amazing story and great characters",
            "Love this movie, watch it now",
            "Incredible film, masterpiece",
            "Beautiful movie, touching story",
            "Great entertainment, fun to watch",
            "Spectacular visuals, great direction",
            "Fantastic screenplay, loved it",
            
            # Negative reviews (more diverse)
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
            "The movie was bad, I didn't like it",
            "Terrible film with poor acting",
            "Boring movie, waste of time",
            "Awful story, don't watch it",
            "Hate this movie, avoid it",
            "Disaster of a film, terrible",
            "Poor quality, not recommended",
            "Dull and boring, fell asleep",
            "Worst acting ever seen",
            "Complete waste, don't bother"
        ],
        'label': [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
    }
    return pd.DataFrame(data)

def train_model(dataset_path=None, use_grid_search=False):
    """Train sentiment analysis model"""
    print("🎬 Starting ML Model Training...")
    
    # Load data
    df = load_imdb_dataset(dataset_path)
    print(f"Dataset size: {len(df)} samples")
    print(f"Positive samples: {sum(df['label'])}")
    print(f"Negative samples: {len(df) - sum(df['label'])}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], 
        df['label'], 
        test_size=0.2, 
        random_state=42,
        stratify=df['label']
    )
    
    # Create vectorizer
    print("🔧 Creating vectorizer...")
    vectorizer = TfidfVectorizer(
        max_features=10000,
        ngram_range=(1, 2),
        stop_words='english',
        min_df=3,
        max_df=0.85
    )
    
    # Fit and transform
    print("🔄 Vectorizing text...")
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Train model
    print("🤖 Training Logistic Regression model...")
    
    if use_grid_search:
        print("🔍 Using Grid Search for hyperparameter tuning...")
        param_grid = {
            'C': [0.1, 1.0, 10.0],
            'max_iter': [1000, 2000],
            'class_weight': ['balanced', None]
        }
        model = GridSearchCV(
            LogisticRegression(random_state=42),
            param_grid,
            cv=5,
            scoring='accuracy',
            n_jobs=-1
        )
        model.fit(X_train_vec, y_train)
        print(f"Best parameters: {model.best_params_}")
        model = model.best_estimator_
    else:
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
    
    # Confusion matrix
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Save model and vectorizer
    print("💾 Saving model and vectorizer...")
    os.makedirs("model", exist_ok=True)
    
    joblib.dump(model, "model/model.pkl")
    joblib.dump(vectorizer, "model/vectorizer.pkl")
    
    print("✅ Model training complete!")
    print("📁 Model saved to: model/model.pkl")
    print("📁 Vectorizer saved to: model/vectorizer.pkl")
    
    # Test predictions
    print("\n🧪 Testing predictions...")
    test_texts = [
        "This movie is amazing and wonderful",
        "This film is terrible and awful",
        "Great acting and plot",
        "Bad script and direction",
        "I absolutely loved this film",
        "Complete waste of time"
    ]
    
    for text in test_texts:
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]
        sentiment = "POSITIVE" if pred == 1 else "NEGATIVE"
        confidence = max(prob)
        print(f"'{text}' -> {sentiment} ({confidence:.2%})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train sentiment analysis model')
    parser.add_argument('--dataset', type=str, help='Path to dataset CSV file')
    parser.add_argument('--grid-search', action='store_true', help='Use grid search for hyperparameter tuning')
    
    args = parser.parse_args()
    train_model(args.dataset, args.grid_search)
