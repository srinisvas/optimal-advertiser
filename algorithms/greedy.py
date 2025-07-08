import time

from numpy.ma.extras import average

def match_ads(users, ads, matrix):
    start = time.time()
    result_set = []
    results = []
    matched_ads = set()

    for user_index, scores in enumerate(matrix):
        best_ad_idx = -1
        max_score = -1

        for ad_index, score in enumerate(scores):
            if ad_index not in matched_ads and score > max_score:
                max_score = score
                best_ad_idx = ad_index

        if best_ad_idx != -1:
            matched_ads.add(best_ad_idx)
            results.append((users[user_index]["user_id"], ads[best_ad_idx]["ad_id"], max_score))

    end = time.time()
    print(f"Approach: Greedy | Execution time: {end - start:.4f} sec")
    result_set.append({"execution_time" : end - start, "average_score" : average([r[2] for r in results]),
                       "ad_coverage" : (len(set([r[1] for r in results]))/200) * 100, "user_count" : len([r[0] for r in results]),
                       "ad_count" : len(set([r[1] for r in results])) })
    return result_set