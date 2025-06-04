def compute_match_score(user, ad):
    score = 0
    if user.get("age_group") == ad.get("target_age_group"):
        score += 2
    if user.get("gender") == ad.get("gender"):
        score += 1
    if ad.get("topic", "").lower() in [i.lower() for i in user.get("interests", [])]:
        score += 3
    score += float(ad.get("click_through_rate", 0)) * 5
    score += float(ad.get("conversion_rate", 0)) * 5
    return score

def compute_match_matrix(users, ads):
    matrix = []
    for user in users:
        row = [compute_match_score(user, ad) for ad in ads]
        matrix.append(row)
    return matrix