EMAIL SPAM DETECTION — MACHINE LEARNING INTERNSHIP PROJECT 01

HexSoftwares Pvt. Ltd. | Internship Domain: Machine Learning
Developed by: Mirza Bilal Hussain

A complete, working spam classifier with a clean, attractive web GUI,
built to match the internship's Project 01 requirements:

- Python + Machine Learning (TF-IDF + Naive Bayes)
- Trained on a labeled spam/ham message dataset
- TF-IDF used for text feature extraction
- Naive Bayes model predicts spam vs. not spam
- Flask web interface (user-friendly GUI)
- Automatically filters/flags unwanted messages

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

spam_detector/
├── app.py                 Flask web app (GUI backend)
├── generate_dataset.py    Creates the training dataset (dataset.csv)
├── train_model.py         Trains TF-IDF + Naive Bayes model
├── dataset.csv            Labeled dataset (spam / ham messages)
├── requirements.txt       Python dependencies
├── model/
│   ├── spam_model.pkl     Trained Naive Bayes model
│   └── vectorizer.pkl     Fitted TF-IDF vectorizer
├── templates/
│   └── index.html         Web GUI (HTML/CSS/JS)
└── static/                (reserved for extra assets)

--------------------------------------------------
HOW IT WORKS
--------------------------------------------------

1. Dataset
   generate_dataset.py builds a labeled dataset of spam and normal (ham)
   messages, covering common real-world spam patterns (prize scams,
   phishing links, fake loans, account alerts, etc.) alongside everyday
   conversational messages.

2. Feature Extraction
   train_model.py converts message text into numeric features using
   TF-IDF (unigrams + bigrams, English stop words removed).

3. Model
   A Multinomial Naive Bayes classifier is trained on the TF-IDF
   features. On the held-out test set it reaches about 99% accuracy.

4. Web App
   app.py loads the saved model and serves a Flask web page
   (templates/index.html) where a user pastes a message and gets an
   instant Spam / Not Spam verdict with a confidence score.

--------------------------------------------------
HOW TO RUN
--------------------------------------------------

1. Install dependencies:
   pip install -r requirements.txt

2. (Already done, but if you want to regenerate)
   python generate_dataset.py     creates dataset.csv
   python train_model.py          trains model, saves to /model

3. Start the web app:
   python app.py

Then open your browser at: http://127.0.0.1:5000

--------------------------------------------------
USING THE APP
--------------------------------------------------

1. Paste any email/SMS text into the message box (or click one of the
   sample chips to try a quick example).
2. Click "Check Message".
3. The result panel shows:
   - SPAM DETECTED or NOT SPAM
   - A spam probability meter
   - The model's overall confidence percentage

--------------------------------------------------
RETRAINING ON YOUR OWN DATA
--------------------------------------------------

If you'd like to train on the actual Kaggle SMS Spam Collection dataset
instead of the bundled synthetic one:

1. Download the dataset from Kaggle and save it as dataset.csv with two
   columns: label (spam/ham) and message.
2. Run "python train_model.py" again, it will pick up the new file
   automatically.

--------------------------------------------------
TECH STACK
--------------------------------------------------

Language            Python 3
ML / Feature Eng.    scikit-learn (TF-IDF, MultinomialNB)
Model persistence    joblib
Web framework        Flask
Frontend             HTML / CSS / JavaScript

--------------------------------------------------

Built for the Machine Learning Internship at HexSoftwares Pvt. Ltd.

