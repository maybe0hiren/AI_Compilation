import pandas as pd
import re
import emoji

dataset = pd.read_csv("raw/dataset.csv")
commentsColumn = "clean_text"
def clean_text(text):
    if not isinstance(text, str):
        return text
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return text
dataset[commentsColumn] = dataset[commentsColumn].apply(clean_text)
dataset.to_csv("raw/cleanDataset.csv", index=False)