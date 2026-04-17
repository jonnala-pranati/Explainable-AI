"""
Real ML Model Training with IMDB Dataset
Trains Logistic Regression model for sentiment analysis
"""
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Configuration
MAX_FEATURES = 5000
MODEL_PATH = "model/model.pkl"
VECTORIZER_PATH = "model/vectorizer.pkl"
RANDOM_STATE = 42


def load_imdb_dataset(csv_path="IMDB Dataset.csv"):
    """Load IMDB dataset from CSV file"""
    print("📊 Loading IMDB dataset from CSV...")

    # Try to load from CSV file
    try:
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            print(f"✅ Loaded {len(df)} samples from {csv_path}")

            # Map sentiment to labels
            if 'sentiment' in df.columns:
                df['label'] = df['sentiment'].map({'positive': 1, 'negative': 0})
            elif 'label' not in df.columns:
                raise ValueError("CSV must have 'sentiment' or 'label' column")

            # Use correct text column
            text_col = 'review' if 'review' in df.columns else 'text'
            if text_col not in df.columns:
                raise ValueError("CSV must have 'review' or 'text' column")

            df = df.rename(columns={text_col: 'text'})

            print(f"   Positive: {sum(df['label'])}")
            print(f"   Negative: {len(df) - sum(df['label'])}")

            # Check if we have both classes
            if len(df['label'].unique()) < 2:
                print("⚠️  Dataset has only one class, using sample data instead")
                return create_sample_data()

            return df
        else:
            print(f"⚠️  CSV file not found: {csv_path}")
            print("Using sample data instead")
            return create_sample_data()
    except Exception as e:
        print(f"⚠️  Failed to load CSV dataset: {e}")
        print("Using sample data instead")
        return create_sample_data()


def create_sample_data():
    """Create sample training data as fallback"""
    print("📊 Creating sample training data...")
    
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
    df = pd.DataFrame(data)
    print(f"✅ Created {len(df)} samples")
    print(f"   Positive: {sum(df['label'])}")
    print(f"   Negative: {len(df) - sum(df['label'])}")
    return df


def preprocess_text(text):
    """Basic text preprocessing"""
    text = text.lower()
    # Keep it simple - let TF-IDF handle the rest
    return text


def train_model():
    """Train sentiment analysis model"""
    print("\n" + "="*60)
    print("🎬 Starting ML Model Training")
    print("="*60)
    
    # Load dataset
    df = load_imdb_dataset()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df['text'],
        df['label'],
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=df['label']
    )
    
    print(f"\n📊 Train size: {len(X_train)}, Test size: {len(X_test)}")
    
    # Create and fit vectorizer
    print("\n🔧 Creating TF-IDF vectorizer...")
    vectorizer = TfidfVectorizer(
        max_features=MAX_FEATURES,
        ngram_range=(1, 2),
        stop_words='english',
        min_df=3,
        max_df=0.85
    )
    
    print("🔄 Fitting vectorizer on training data...")
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    print(f"✅ Vectorizer fitted with {len(vectorizer.get_feature_names_out())} features")
    
    # Train model
    print("\n🤖 Training Logistic Regression model...")
    model = LogisticRegression(
        C=1.0,
        max_iter=1000,
        random_state=RANDOM_STATE,
        class_weight='balanced',
        n_jobs=-1
    )
    
    model.fit(X_train_vec, y_train)
    print("✅ Model training complete")
    
    # Evaluate
    print("\n📈 Evaluating model...")
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nAccuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))
    
    # Save model and vectorizer
    print("\n💾 Saving model and vectorizer...")
    os.makedirs("model", exist_ok=True)
    
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    
    print(f"✅ Model saved to: {MODEL_PATH}")
    print(f"✅ Vectorizer saved to: {VECTORIZER_PATH}")
    
    # Test predictions
    print("\n🧪 Testing predictions...")
    test_texts = [
        "This movie is absolutely amazing and wonderful",
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
    
    print("\n" + "="*60)
    print("✅ Training Complete!")
    print("="*60)
    
    return accuracy


if __name__ == "__main__":
    train_model()
