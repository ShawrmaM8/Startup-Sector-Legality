import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from slaw_config import DATA_PATH, MODEL_PATH, SECTORS

def train_classifier():
    """Train and save a sector classifier."""
    # Load dataset
    df = pd.read_csv(DATA_PATH)
    X = df["description"]
    y = df["sector"]
    
    # Create pipeline: TF-IDF + Logistic Regression
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=1000)),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    
    # Train model
    pipeline.fit(X, y)
    
    # Save model
    joblib.dump(pipeline, MODEL_PATH)
    return pipeline

def load_classifier():
    """Load the trained classifier."""
    return joblib.load(MODEL_PATH)

def predict_sector(text):
    """Predict sector for a given text."""
    classifier = load_classifier()
    return classifier.predict([text])[0]