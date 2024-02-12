# to run: python data_analysis/analysis.py
#control_all[control_all.batch==1] ##note: R syntax works the same here
import pandas as pd
from matplotlib import pyplot as plt

    
## IMPORTING DATA FILES -------------------------------------------------------------------------
runs = pd.DataFrame(
    [{"run": 1, "user": "control", "videos": "all", "path": "data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_all_videos.csv"},
     {"run": 1, "user": "control", "videos": "liked", "path": "data/-1_Sec02Gr2Sc1Cntrl_JL_02-11-13-17_like_by_hashtag_data_liked_videos.csv"}
    ])

# creating df names for each csv
dfs = {}
for row in range(runs.shape[0]):
    var_name = "r{}_{}_{}".format(runs.iloc[row]["run"], runs.iloc[row]["user"], runs.iloc[row]["videos"])
    dfs[var_name] = pd.read_csv(runs.iloc[row]["path"])
print(dfs["r1_control_all"].columns)

# combine runs into one dataset
# TODO

## ANALYZING COMMENTS/LIKES/SHARES/SAVES (quantitative, time series) ----------------------------------

# histogram (for one run)
r1_control_all_comments = dfs["r1_control_all"].comments.to_numpy()
plt.hist(r1_control_all_comments)
plt.xlabel("Number of Comments")
plt.ylabel("Counts")
plt.title("Comments of videos seen")
#plt.show()

# line chart(for multiple runs)
# TODO




## ANALYZING HASHTAGS -----------------------------------------------------------------------------
# data cleaning
hash_to_ignore = ["fyp", "viral", "foryou", "foryoupage", "tiktok", "fy", "fypage", "fypchallenge"]
def clean_hashtags(df):
    noNA_hash = []
    for row in range(df.shape[0]): #for each post
        if type(df.hashtag.iloc[row])==type(""): #if not NaN types
            list_of_hash = df.hashtag.iloc[row].split(",")
            noNA_hash.append([hash.strip() for hash in list_of_hash])
    full_list = list(set([a for b in noNA_hash for a in b]))
    return list(filter(lambda x: x not in hash_to_ignore, full_list))

# frequency table
freq = pd.Series(clean_hashtags(dfs["r1_control_all"])).value_counts()
print(freq[freq>1]) #no explicit repetition

# Jaccard index
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

# a) comparison 1: control vs active feeds (analyzing possible feed divergence)
scen1_control_all = set(dfs["r1_control_all"])
#scen1_active_all = set()

# b) comparison 2: predefined hashtags to like vs actually liked posts (to compare similarities between other hashtags that were not predefined but still appeared for similar posts)
#scen1_predefined_hash = set()
#scen1_active_like = set()

# an example for how to run this:
set_a = set(["cookies", "baking", "food", "recipe"])
set_b = set(["oven", "baking", "cook", "bread"])
similarity = jaccard_similarity(set_a, set_b)
print("Jaccard Similarity:", similarity)

## ANALYZING MUSIC ----------------------------------------------------------------------------------
mus = dfs["r1_control_all"].music.value_counts()
print(mus)




## ANALYZING AUTHOR ---------------------------------------------------------------------------------
aut = dfs["r1_control_all"].author.value_counts()
print(aut)