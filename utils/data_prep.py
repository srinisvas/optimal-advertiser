import os
from datetime import datetime

import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_all_datasets():
    analytics_data = {
        "ad_click_behavior_analytics": pd.read_csv(os.path.join(BASE_DIR, "datasets", "ad_click_behavior_analytics.csv")),
        "ad_performance_analytics": pd.read_csv(os.path.join(BASE_DIR, "datasets", "ad_performance_analytics.csv")),
        "social_media_influencer_analytics": pd.read_csv(os.path.join(BASE_DIR, "datasets", "social_media_influencer_analytics.csv")),
        "user_interests_demographic_analytics": pd.read_csv(os.path.join(BASE_DIR, "datasets", "user_interests_demographic_analytics.csv")),
        "ad_info_analytics": pd.read_csv(os.path.join(BASE_DIR, "datasets", "ad_info_analytics.csv"))
    }
    return analytics_data

def build_user_profiles(analytics_data):
    ad_click_behavior_dict = analytics_data["ad_click_behavior_analytics"].set_index("id").to_dict(orient="index")

    user_profiles = []
    for _, row in analytics_data["user_interests_demographic_analytics"].iterrows():

        raw_interests = eval(row["Interests"])

        if isinstance(raw_interests, str):
            raw_interests = [raw_interests]

        user_profile = {
            "user_id": row["UserID"],
            "gender": row["Gender"],
            "target_group": list({ lookup_target.get(i.lower(), i) for i in raw_interests }),
            "interested_topics": list({lookup_topic.get(i.lower(), i) for i in raw_interests}),
            "age_group": populate_age_group(row["DOB"])
        }

        if row["UserID"] in ad_click_behavior_dict:
            behavior = ad_click_behavior_dict[row["UserID"]]
            user_profile["browsing_history"] = behavior.get("browsing_history")
            user_profile["ad_click_flag"] = behavior.get("click", 0) > 0

        user_profiles.append(user_profile)

    return user_profiles

def build_ad_profiles(analytics_data):

    ad_performance_dict = analytics_data["ad_performance_analytics"].set_index("ad_id").to_dict(orient="index")

    ad_profiles = []
    for _, row in analytics_data["ad_info_analytics"].iterrows():
        user_engagement = 0
        user_interactions = 0

        ad_profile = {
            "id": row["ad_id"],
            "topic": row["ad_topic"],
            "target_age_group": row["age_group"],
            "target_gender": row["target_gender"],
            "cost_per_click": row["cost_per_click"],
            "target_audience": row["ad_target_audience"]
        }

        if row["ad_id"] in ad_performance_dict:
            behavior = ad_performance_dict[row["ad_id"]]
            engagement = behavior.get("engagement_level")
            ad_profile["click_through_rate"] = behavior.get("click_through_rate")
            ad_profile["conversion_rate"] = behavior.get("conversion_rate")
            ad_profile["engagement_level"] = bool(engagement and str(engagement).strip().lower() != "ignored")
            ad_profile["roi"] = behavior.get("ROI")

        for _, social_row in analytics_data["social_media_influencer_analytics"].iterrows():
            post_text = str(social_row["Post Text"])
            if row["ad_topic"].lower() in post_text.lower():
                user_engagement = user_engagement + int(social_row.get("User Engagement"))
                user_interactions = user_interactions + int(social_row.get("User Interactions"))

        if user_engagement or user_interactions > 0:
            ad_profile["in_trend_topic"] = True
        else:
            ad_profile["in_trend_topic"] = False

        ad_profiles.append(ad_profile)

    return ad_profiles

def populate_age_group(dob_str):
    birth_year = int(str(dob_str).split("/")[2])
    birth_month = int(str(dob_str).split("/")[0])
    birth_day = int(str(dob_str).split("/")[1])
    today = datetime.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

    if age < 25:
        return "18-24"
    elif age < 35:
        return "25-34"
    elif age < 55:
        return "35-54"
    else:
        return "55+"

interests_target_grouping = {

"young adults" : {"gaming", "music", "business and entrepreneurship", "finance and investments", "fashion", "beauty"},
"family oriented" : {"gardening", "social causes and activism", "art", "history", "movies", "cooking", "pets", "parenting and family", "politics", "art", "diy and crafts"},
"travel lovers" : {"photography", "travel", "food and dining"},
"fitness lovers" : {"outdoor activities", "health and wellness", "nature", "sports", "fitness"},
"tech enthusiasts" : {"education and learning", "technology", "books", "science", "cars and automobiles"}

}

lookup_target = {
    interest.lower(): group
    for group, interests in interests_target_grouping.items()
    for interest in interests
}

interests_topic_grouping = {

"travel" : {"photography", "travel", "food and dining", "books"},
"fashion" : {"fashion", "beauty", "art"},
"electronics" : {"gaming", "music", "movies"},
"health" : {"outdoor activities", "health and wellness", "nature", "sports", "fitness"},
"automotive" : {"technology", "science", "cars and automobiles"}

}

lookup_topic = {
    interest.lower(): group
    for group, interests in interests_topic_grouping.items()
    for interest in interests
}

"""
data = load_all_datasets()
userProfiles = build_user_profiles(data)
adProfiles = build_ad_profiles(data)

print(userProfiles)
print(adProfiles)
"""