import time


def match_ads(users, ads, matrix):
    start = time.time()
    results = []
    matched_ads = set()

    for user_index, scores in enumerate(matrix):
        unmatched_scores = []
        for ad_index, score in enumerate(scores):
            if ad_index not in matched_ads:
                unmatched_scores.append((ad_index, score))
        ranked = sorted(unmatched_scores, key=lambda x: x[1], reverse=True)

        if ranked:
            best_ad_idx, score = ranked[0]
            matched_ads.add(best_ad_idx)
            results.append((users[user_index]["user_id"], ads[best_ad_idx]["ad_id"], score))
    end = time.time()

    print(f"{"Approach: Greedy"} | Execution time: {end - start:6.4f} sec")
    return results