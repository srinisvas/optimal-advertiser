import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_all_datasets():
    data = {
        "dataset1": pd.read_csv(os.path.join(BASE_DIR, "datasets", "ad_click_dataset.csv")),
        "dataset2": pd.read_csv(os.path.join(BASE_DIR, "datasets", "advertising_dataset.csv")),
        "dataset3": pd.read_csv(os.path.join(BASE_DIR, "datasets", "Advertising_dataset_with_character_target.csv")),
        "dataset4": pd.read_csv(os.path.join(BASE_DIR, "datasets", "socialmedia.csv")),
        "dataset5": pd.read_csv(os.path.join(BASE_DIR, "datasets", "SocialMediaUsersDataset.csv")),
    }
    return data

def build_user_profiles(data):

    user_profiles = []
    for _, row in data["dataset5"].iterrows():
        user_profiles.append({
            "user_id": row["UserID"],
            "gender": row["Gender"],
            "interests": eval(row["Interests"]),
            "location": row["City"],
            "age_group": "55+" if int(row["DOB"].split("-")[0]) < 1970 else "18-54"
        })
    return user_profiles

def build_ad_profiles(data):
    ad_profiles = []
    for _, row in data["dataset2"].iterrows():
        ad_profiles.append({
            "ad_id": row["ad_id"],
            "topic": row["ad_topic"],
            "target_age_group": row["age_group"],
            "gender": row["gender"],
            "click_through_rate": row["click_through_rate"],
            "conversion_rate": row["conversion_rate"]
        })
    return ad_profiles

"""
data = load_all_datasets()
userProfiles = build_user_profiles(data)
adProfiles = build_ad_profiles(data)

print(data)
print(userProfiles)
print(adProfiles)
"""