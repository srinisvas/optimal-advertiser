def compute_match_score(user, ad):
    score = 0

    if ad.get("topic", "").lower() in [i.lower() for i in user.get("interested_topics", [])]:
        score += 25
    if ad.get("target_audience", "").lower() in [i.lower() for i in user.get("target_group", [])]:
        score += 15
    if user.get("age_group") == ad.get("target_age_group"):
        score += 10
    if user.get("gender") == ad.get("gender"):
        score += 10
    if user.get("ad_click_flag"):
        score += 10
    if str(user.get("browsing_history","")).lower == "shopping":
        score += 10
    if ad.get("in_trend_topic"):
        score += 5
    if ad.get("engagement_level"):
        score += 5

    score += round((float(ad.get("click_through_rate", 0)) + float(ad.get("conversion_rate", 0)) + float(ad.get("roi", 0))) / 3 * 10, 2)

    return score

def compute_match_matrix(users, ads):
    match_matrix = []
    for user in users:
        row = [compute_match_score(user, ad) for ad in ads]
        match_matrix.append(row)
    return match_matrix