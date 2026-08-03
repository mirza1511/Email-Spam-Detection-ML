"""
train_model.py
---------------
Trains a Naive Bayes spam classifier using TF-IDF text features.

Steps:
 1. Load dataset.csv (label, message)
 2. Split into train/test sets
 3. Vectorize text using TF-IDF
 4. Train a Multinomial Naive Bayes model
 5. Evaluate accuracy / precision / recall
 6. Save the trained model + vectorizer to /model for use in the Flask app
"""

import csv
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA_PATH = "dataset.csv"
MODEL_PATH = "model/spam_model.pkl"
VECTORIZER_PATH = "model/vectorizer.pkl"


def load_data(path):
    messages, labels = [], []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            messages.append(row["message"])
            labels.append(1 if row["label"].strip().lower() == "spam" else 0)
    return messages, labels


def main():
    print("Loading dataset...")
    messages, labels = load_data(DATA_PATH)
    print(f"Total messages: {len(messages)}")

    X_train, X_test, y_train, y_test = train_test_split(
        messages, labels, test_size=0.2, random_state=42, stratify=labels
    )

    print("Vectorizing text using TF-IDF...")
    vectorizer = TfidfVectorizer(
        stop_words="english",
        lowercase=True,
        max_features=3000,
        ngram_range=(1, 2),
    )
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    print("Training Naive Bayes model...")
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    print("Evaluating model...")
    y_pred = model.predict(X_test_tfidf)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {acc * 100:.2f}%\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nSaving model and vectorizer...")
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print(f"Model saved to {MODEL_PATH}")
    print(f"Vectorizer saved to {VECTORIZER_PATH}")


if __name__ == "__main__":
    main()
