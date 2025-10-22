import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from scipy import sparse

df = pd.read_csv("raw/finalDataset.csv")
commentsColumn = "comment"
labelsColumn = "label"

df[commentsColumn] = df[commentsColumn].fillna("")

vec = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2),
    stop_words='english'
)

comments = vec.fit_transform(df[commentsColumn])
labels = df[labelsColumn].values

X_train, X_temp, y_train, y_temp = train_test_split(
    comments, labels, test_size=0.3, random_state=42
)
X_test, X_val, y_test, y_val = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

sparse.save_npz("datasets/comments_train.npz", X_train)
sparse.save_npz("datasets/comments_test.npz", X_test)
sparse.save_npz("datasets/comments_val.npz", X_val)
pd.DataFrame(y_train, columns=[labelsColumn]).to_csv("datasets/labels_train.csv", index=False)
pd.DataFrame(y_test, columns=[labelsColumn]).to_csv("datasets/labels_test.csv", index=False)
pd.DataFrame(y_val, columns=[labelsColumn]).to_csv("datasets/labels_val.csv", index=False)


print("✅ Sparse TF-IDF dataset ready for training!")
print(f"Training shape: {X_train.shape}, Testing shape: {X_test.shape}, Validation shape: {X_val.shape}")