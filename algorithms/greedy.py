def match_ads(users, ads, matrix):
    results = []
    used_ads = set()
    for user_idx, scores in enumerate(matrix):
        ranked = sorted([(i, s) for i, s in enumerate(scores) if i not in used_ads], key=lambda x: x[1], reverse=True)
        if ranked:
            best_ad_idx, score = ranked[0]
            used_ads.add(best_ad_idx)
            results.append((users[user_idx]["user_id"], ads[best_ad_idx]["ad_id"], score))
    return results