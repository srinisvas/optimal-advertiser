import time
from collections import defaultdict

from numpy.ma.extras import average


def match_ads(users, ads, scores, max_per_ad=10):
    start = time.time()
    result_set = []
    num_of_users = len(users)
    num_of_ads = len(ads)
    ad_usage = defaultdict(int)

    assignments = [-1] * num_of_users
    for user_index in range(num_of_users):
        sorted_ads = sorted(
            range(num_of_ads),
            key=lambda j: scores[user_index][j],
            reverse=True
        )
        for ad_index in sorted_ads:
            if ad_usage[ad_index] < max_per_ad:
                assignments[user_index] = ad_index
                ad_usage[ad_index] += 1
                break
    ad_coverage_before_iteration = (len(set(assignments))/len(ads))*100

    unused_ads = [ad_id for ad_id in range(num_of_ads) if ad_usage[ad_id] == 0]

    for unused_ad in unused_ads:
        swap_candidate = None
        best_improvement = float('-inf')

        for user_id in range(num_of_users):
            current_ad = assignments[user_id]
            current_score = scores[user_id][current_ad]
            new_score = scores[user_id][unused_ad]

            if ad_usage[current_ad] > 1 and new_score > current_score:
                improvement = new_score - current_score
                if improvement > best_improvement:
                    swap_candidate = user_id
                    best_improvement = improvement

        if swap_candidate is not None:
            old_ad = assignments[swap_candidate]
            ad_usage[old_ad] -= 1
            assignments[swap_candidate] = unused_ad
            ad_usage[unused_ad] += 1
        else:
            for user_id in range(num_of_users):
                old_ad = assignments[user_id]
                if ad_usage[old_ad] > 1:
                    ad_usage[old_ad] -= 1
                    assignments[user_id] = unused_ad
                    ad_usage[unused_ad] += 1
                    break

    improved = True
    while improved:
        improved = False

        for user_id in range(num_of_users):
            current_ad = assignments[user_id]
            current_score = scores[user_id][current_ad]

            for alt_ad in range(num_of_ads):
                if alt_ad == current_ad or ad_usage[alt_ad] >= max_per_ad:
                    continue

                alt_score = scores[user_id][alt_ad]
                if alt_score > current_score:
                    assignments[user_id] = alt_ad
                    ad_usage[alt_ad] += 1
                    ad_usage[current_ad] -= 1
                    improved = True
                    break

    result = []

    for user_index, ad_index in enumerate(assignments):
        result.append((
            users[user_index]["user_id"],
            ads[ad_index]["ad_id"],
            scores[user_index][ad_index]
        ))
    end = time.time()
    result_set.append({"execution_time" : end - start, "average_score" : average([r[2] for r in result]),
                       "ad_coverage" : (len(set([r[1] for r in result]))/200) * 100, "user_count" : len([r[0] for r in result]),
                       "ad_count" : len(set([r[1] for r in result])) })

    print(f"{"Approach: Iterative Improvement"} | Execution time: {end - start:6.4f} sec | Ad Coverage before Iterations: {ad_coverage_before_iteration}")

    return result_set
