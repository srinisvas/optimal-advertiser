import time
from collections import defaultdict


def match_ads(users, ads, scores, max_per_ad=10):
    start = time.time()

    num_users = len(users)
    num_ads = len(ads)
    ad_usage = defaultdict(int)

    assignments = [-1] * num_users
    for user_idx in range(num_users):
        sorted_ads = sorted(
            range(num_ads),
            key=lambda j: scores[user_idx][j],
            reverse=True
        )
        for ad_idx in sorted_ads:
            if ad_usage[ad_idx] < max_per_ad:
                assignments[user_idx] = ad_idx
                ad_usage[ad_idx] += 1
                break

    unused_ads = [i for i in range(num_ads) if ad_usage[i] == 0]
    for ad_idx in unused_ads:
        best_swap = None
        for user_idx in range(num_users):
            current = assignments[user_idx]
            if ad_usage[current] > 1 and scores[user_idx][ad_idx] > scores[user_idx][current]:
                score_delta = scores[user_idx][ad_idx] - scores[user_idx][current]
                best_swap = (score_delta, user_idx)
        if best_swap:
            _, user_idx = best_swap
            ad_usage[assignments[user_idx]] -= 1
            assignments[user_idx] = ad_idx
            ad_usage[ad_idx] += 1
        else:
            for user_idx in range(num_users):
                current = assignments[user_idx]
                if ad_usage[current] > 1:
                    ad_usage[current] -= 1
                    assignments[user_idx] = ad_idx
                    ad_usage[ad_idx] += 1
                    break

    improved = True
    while improved:
        improved = False
        for user_idx in range(num_users):
            current_ad = assignments[user_idx]
            for alt_ad in range(num_ads):
                if alt_ad == current_ad or ad_usage[alt_ad] >= max_per_ad:
                    continue
                gain = scores[user_idx][alt_ad] - scores[user_idx][current_ad]
                if gain > 0:
                    assignments[user_idx] = alt_ad
                    ad_usage[alt_ad] += 1
                    ad_usage[current_ad] -= 1
                    improved = True
                    break

    result = []
    for user_idx, ad_idx in enumerate(assignments):
        result.append((
            users[user_idx]["user_id"],
            ads[ad_idx]["ad_id"],
            scores[user_idx][ad_idx]
        ))
    end = time.time()
    print(f"{"Iterative Improvement"} | Time: {end - start:6.4f} sec")

    return result