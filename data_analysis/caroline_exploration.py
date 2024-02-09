# to run: python3 data_analysis/caroline_exploration.py
import pandas as pd
import requests
import io
    
# Downloading the csv file from your GitHub account

all_url = "https://raw.githubusercontent.com/mlsmzk/tiktok-like-experiment/main/data/10-31-02-08_like_by_hashtag_data_all_videos.csv.csv"
all_download = requests.get(all_url).content
all = pd.read_csv(io.StringIO(all_download.decode('utf-8')))

liked_url = "https://raw.githubusercontent.com/mlsmzk/tiktok-like-experiment/main/data/10-31-02-08_like_by_hashtag_data_liked_videos.csv.csv"
liked_download = requests.get(liked_url).content
liked = pd.read_csv(io.StringIO(liked_download.decode('utf-8')))


#print(all.head(5), liked.head(5))
print(all.shape[0], liked.shape[0]) #row count
print(all.columns, liked.columns) #same column names

val = liked.hashtag.to_numpy()
print(val)
