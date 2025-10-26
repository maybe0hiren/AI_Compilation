import joblib
import re

model = joblib.load('sentimentAnalyzer.joblib')
vectorizer = joblib.load('vectorizer.joblib')

def commentProcessor(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return text.strip()
mapper = {
    -1: "Negative",
    0: "Neutral",
    1: "Positive"
}
while True:
    comment = input("Enter a social media comment (or 'exit' to quit): ")
    if comment.lower() == 'exit':
        break
    comment = commentProcessor(comment)
    comment = vectorizer.transform([comment])
    result = model.predict(comment)
    category = mapper.get(int(result), "Unknown")
    print("Predicted category:", category)
