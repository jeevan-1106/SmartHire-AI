from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

class TFIDFVectorizer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=5000,
            ngram_range=(1, 2)
        )

    def fit_transform(self, documents):
        return self.vectorizer.fit_transform(documents)

    def transform(self, documents):
        return self.vectorizer.transform(documents)

    def save(self, path):
        joblib.dump(self.vectorizer, path)

    def load(self, path):
        self.vectorizer = joblib.load(path)
        