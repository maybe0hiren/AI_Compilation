import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib


data = pd.read_csv('resources/datasets/cleanedDataset.csv') 
data['clean_text'] = data['clean_text'].fillna('')
data = data.dropna(subset=['clean_text', 'category'])
X = data['clean_text']
y = data['category']

vectorizer = TfidfVectorizer(
    max_features=15000,
    ngram_range=(1,3),
    stop_words='english',
    min_df=2,
    max_df=0.95,
    sublinear_tf=True
)
X_vect = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

model = LogisticRegression(
    max_iter=15000,
    class_weight='balanced',
    C=2.5,
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

joblib.dump(model, 'sentimentAnalyzer.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')
