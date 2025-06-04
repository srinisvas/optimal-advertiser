def match_ads(users, ads, matrix):
    results = []
    for user_idx, scores in enumerate(matrix):
        best_ad_idx = max(range(len(scores)), key=lambda i: scores[i])
        results.append((users[user_idx]["user_id"], ads[best_ad_idx]["ad_id"], scores[best_ad_idx]))
    return results