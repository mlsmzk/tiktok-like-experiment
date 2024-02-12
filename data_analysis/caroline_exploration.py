# to run: python data_analysis/caroline_exploration.py
import pandas as pd
from matplotlib import pyplot as plt

    
## IMPORTING DATA FILES -------------------------------------------------------------------------
runs = pd.DataFrame(
    [{"run": 1, "user": "control", "videos": "all", "path": "data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_all_videos.csv"},
     {"run": 1, "user": "control", "videos": "liked", "path": "data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_liked_videos.csv"}
    ]
)

# creating df names for each csv
dfs = {}
for row in range(runs.shape[0]):
    var_name = "r{}_{}_{}".format(runs.iloc[row]["run"], runs.iloc[row]["user"], runs.iloc[row]["videos"])
    dfs[var_name] = pd.read_csv(runs.iloc[row]["path"])
#print(dfs["r1_control_all"].shape[0]) #row count
#print(dfs["r1_control_all"].columns) #same column names


## ANALYZING COMMENTS (quantitative) -------------------------------------------------------------

# histogram (for one run)
r1_control_all_comments = dfs["r1_control_all"].comments.to_numpy()
plt.hist(r1_control_all_comments)
plt.xlabel("Number of Comments")
plt.ylabel("Counts")
plt.title("Comments of videos seen")
#plt.show()

#line chart(for multiple runs)



# ------------------------------------------------------------------------------------------
#val = control_all[control_all.batch==1] ##note: R syntax works the same here
#print(val)


## ANALYZING HASHTAGS -----------------------------------------------------------------------------
#common hashtags to ignore
common_hash = ["fyp", "viral", "foryou", "foryoupage", "tiktok", "fy", "fypage", "fypchallenge"]
full = dfs["r1_control_all"].hashtag.tolist() #full hashtags

def clean_hashtags(df):
    noNA_hash = []
    for row in range(df.shape[0]): #for each post
        #Note: NaN values are not string types (i.e. they are float types)
        if type(df.hashtag.iloc[row])==type(""):
            #print("STRING")
            list_of_hash = df.hashtag.iloc[row].split(",") #list of words
            noNA_hash.append([hash.strip() for hash in list_of_hash])
        #else:
            #print("NOT STRING") #don't do anything

    return list(set([a for b in noNA_hash for a in b])) #put all the strings into one list


clean_hashtags(dfs["r1_control_all"])


#also count frequencies of these hashtags

#JACCARD INDEX
