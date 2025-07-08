import time

from numpy.ma.extras import average


def match_ads(users, ads, matrix):
    result_set = []
    results = []
    start = time.time()
    for user_index, scores in enumerate(matrix):
        highest_score = -float('inf')
        best_ad_index = -1

        for ad_index, score in enumerate(scores):
            if score > highest_score:
                highest_score = score
                best_ad_index = ad_index

        results.append((users[user_index]["user_id"], ads[best_ad_index]["ad_id"], highest_score))
    end = time.time()
    result_set.append({"execution_time" : end - start, "average_score" : average([r[2] for r in results]),
                       "ad_coverage" : (len(set([r[1] for r in results]))/200) * 100, "user_count" : len([r[0] for r in results]),
                       "ad_count" : len(set([r[1] for r in results])) })
    print(f"{"Approach: Brute Force"} | Execution time: {end - start:6.4f} sec")
    return result_set