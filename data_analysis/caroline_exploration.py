# to run: python data_analysis/caroline_exploration.py
import pandas as pd
import requests
import io

from matplotlib import pyplot as plt
import seaborn
    
# Downloading the csv file from GitHub
def url_to_df(url):
    download = requests.get(url).content
    df = pd.read_csv(io.StringIO(download.decode('utf-8')))
    return df

all = pd.read_csv("data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_all_videos.csv")
like = pd.read_csv("data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_liked_videos.csv")
print(all)

runs = pd.DataFrame(
    [{"run": 1, "user": "control", "videos": "all", "url": "https://raw.githubusercontent.com/mlsmzk/tiktok-like-experiment/main/data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_all_videos.csv"},
     {"run": 1, "user": "control", "videos": "liked", "url": "https://raw.githubusercontent.com/mlsmzk/tiktok-like-experiment/main/data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_liked_videos.csv"}
    ]
)

#run1_control_all_url = "https://raw.githubusercontent.com/mlsmzk/tiktok-like-experiment/main/data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_all_videos.csv"
#run1_control_liked_url = "https://raw.githubusercontent.com/mlsmzk/tiktok-like-experiment/main/data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_liked_videos.csv"
#control liked has no data


#new column

# for row in range(2):
#     var_name = "run{}_{}_{}".format(runs.iloc[row]["run"], runs.iloc[row]["user"], runs.iloc[row]["videos"])
#     print(var_name)
#     var_val = url_to_df(runs.iloc[row]["url"])
#     print(var_val)
#     exec(f"{var_name}={var_val}") #creating variable dynamically
#print(run1_control_all)


#url_names = ["run1_control_all_url", "run1_control_liked_url"]
#print(url_names[0])



#df_names = [run1_control_all, run1_control_liked]


#run1_control_all = url_to_df(run1_control_all_url)
#run1_control_liked = url_to_df(run1_control_liked_url)


#print(control_all.shape[0]) #row count
#print(control_all.columns) #same column names



## ANALYZING COMMENTS (quantitative)

#histogram (for one run)
# val = run1_control_all.comments.to_numpy()
# plt.hist(val)
# plt.xlabel("Number of Comments")
# plt.ylabel("Counts")
# plt.title("Comments of videos seen")
# plt.show()

#line chart(for multiple runs)



#val = control_all[control_all.batch==1] ##note: R syntax works the same here
#print(val)


## ANALYZING HASHTAGS (J)
#common hashtags to ignore
#common_hash = ["fyp", "viral", "foryou", "foryoupage", "tiktok", "fy", "fypage","fypchallenge"]
#control_all_fullhashtags = run1_control_all.hashtag.to_numpy()

#also count frequencies of these hashtags

#JACCARD INDEX
