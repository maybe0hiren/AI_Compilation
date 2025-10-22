import pandas as pd
import re
import emoji
from contractions import fix

## Filtering Dataset1 - hate.csv
# df = pd.read_csv("hate.csv")
# df = df.drop(columns=["serial"])
# df.to_csv("finalDataset.csv", index=False)


## Filtering Dataset2 - synthetic_social_media_data.csv
# df = pd.read_csv("synthetic_social_media_data.csv")
# df = df.drop(columns=["Post ID", "Number of Likes", "Number of Shares", "Number of Comments", "User Follower Count","Post Date and Time", "Post Type", "Language"])
# df.to_csv("finalDataset.csv", mode="a", header=False, index=False)



## Filtering Dataset3 - YoutubeCommentsDataSet.csv
# df = pd.read_csv("YoutubeCommentsDataSet.csv")
# df.to_csv("finalDataset.csv", mode="a", header=False, index=False)


## Formatting Variables
# df = pd.read_csv("finalDataset.csv")
# sentimentColumn = df.columns[1]
# def map_sentiment(value):
#     if isinstance(value, str):
#         v = value.strip().lower()
#         if v in ["negative", "n", "-1"]:
#             return -1
#         elif v in ["positive", "p", "1"]:
#             return 1
#         elif v in ["neutral", "neutal", "0"]:
#             return 0
#     return value 
# df[sentimentColumn] = df[sentimentColumn].apply(map_sentiment)
# df.to_csv("finalDataset.csv", index=False)





# # Shuffeling rows
# df = pd.read_csv("finalDataset.csv")
# df = df.sample(frac=1).reset_index(drop=True)
# df.to_csv("finalDataset.csv", index=False)

# # Text Cleaning
# df = pd.read_csv("finalDataset.csv")
# commentsColumn = "comment"
# emoji_dict = {
#     "😍": "love",
#     "👍": "thumbs_up",
#     "😢": "sad",
#     "😂": "laugh",
#     "🔥": "fire",
#     "🤬": "angry"
# }
# def clean_text(text):
#     if not isinstance(text, str):
#         return text
#     text = fix(text)
#     text = text.lower()
#     text = re.sub(r"http\S+|www\S+", "<URL>", text)
#     text = re.sub(r"@\w+", "<MENTION>", text)
#     text = re.sub(r"#\w+", "<HASHTAG>", text)
#     text = "".join(emoji_dict.get(char, char) for char in text)
#     text = re.sub(r"(.)\1{2,}", r"\1\1", text)
#     text = re.sub(r"([!?.,])\1+", r"\1", text)
#     text = re.sub(r"\s+", " ", text).strip()
#     return text
# df[commentsColumn] = df[commentsColumn].apply(clean_text)
# df.to_csv("finalDataset.csv", index=False)
# print("Text cleaning complete!")




# # Splitting the Dataset
# df = pd.read_csv("finalDataset.csv")
# df = df.sample(frac=1, random_state=42).reset_index(drop=True)
# trainingDatasetSize = int(0.8 * len(df))
# testingDatasetSize = int(0.1 * len(df))
# valDatasetSize = len(df) - trainingDatasetSize - testingDatasetSize
# train_df = df.iloc[:trainingDatasetSize]
# test_df = df.iloc[trainingDatasetSize:trainingDatasetSize + testingDatasetSize]
# val_df = df.iloc[trainingDatasetSize + testingDatasetSize:]
# train_df.to_csv("datasets/training.csv", index=False)
# test_df.to_csv("datasets/testing.csv", index=False)
# val_df.to_csv("datasets/validating.csv", index=False)
# print("Split complete:")
# print(f"Training: {len(train_df)} rows")
# print(f"Testing:  {len(test_df)} rows")
# print(f"Validation: {len(val_df)} rows")

