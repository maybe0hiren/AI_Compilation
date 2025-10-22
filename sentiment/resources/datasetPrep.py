import pandas as pd
import re
import emoji
from contractions import fix

## Filtering Dataset1 - hate.csv
# df = pd.read_csv("raw/hate.csv")
# df = df.drop(columns=["serial"])
# df.to_csv("raw/finalDataset.csv", index=False)


## Filtering Dataset2 - synthetic_social_media_data.csv
# df = pd.read_csv("raw/synthetic_social_media_data.csv")
# df = df.drop(columns=["Post ID", "Number of Likes", "Number of Shares", "Number of Comments", "User Follower Count","Post Date and Time", "Post Type", "Language"])
# df.to_csv("rawfinalDataset.csv", mode="a", header=False, index=False)



## Filtering Dataset3 - YoutubeCommentsDataSet.csv
# df = pd.read_csv("raw/YoutubeCommentsDataSet.csv")
# df.to_csv("raw/finalDataset.csv", mode="a", header=False, index=False)


## Formatting Variables
# df = pd.read_csv("raw/finalDataset.csv")
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
# df.to_csv("raw/finalDataset.csv", index=False)





# # Shuffeling rows
# df = pd.read_csv("raw/finalDataset.csv")
# df = df.sample(frac=1).reset_index(drop=True)
# df.to_csv("raw/finalDataset.csv", index=False)

# # Text Cleaning
# df = pd.read_csv("raw/finalDataset.csv")
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
# df.to_csv("raw/finalDataset.csv", index=False)
# print("Text cleaning complete!")



