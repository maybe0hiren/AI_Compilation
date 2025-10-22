import pandas as pd



# df = pd.read_csv("hate.csv")
# df = df.drop(columns=["serial"])
# df.to_csv("finalDataset.csv", index=False)



# df = pd.read_csv("synthetic_social_media_data.csv")
# df = df.drop(columns=["Post ID", "Number of Likes", "Number of Shares", "Number of Comments", "User Follower Count","Post Date and Time", "Post Type", "Language"])
# df.to_csv("finalDataset.csv", mode="a", header=False, index=False)




# df = pd.read_csv("YoutubeCommentsDataSet.csv")
# df.to_csv("finalDataset.csv", mode="a", header=False, index=False)



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
