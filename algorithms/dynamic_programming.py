import time
import heapq
from collections import defaultdict

from numpy.ma.extras import average


def match_ads(users, ads, scores, max_per_ad=10, beam_width=100):
    start = time.time()
    result_set = []
    num_users = len(users)
    num_ads = len(ads)

    initial_caps = (max_per_ad,) * num_ads
    initial_state = (0, 0, initial_caps, [])

    beam = [initial_state]
    memo = dict()

    for user_id in range(num_users):
        next_beam = []

        for total_score, _, ad_caps, assignments in beam:
            for ad_id in range(num_ads):
                if ad_caps[ad_id] > 0:
                    new_caps = list(ad_caps)
                    new_caps[ad_id] -= 1
                    new_caps_tuple = tuple(new_caps)
                    new_assignments = assignments + [ad_id]
                    new_score = total_score + scores[user_id][ad_id]

                    key = (user_id + 1, new_caps_tuple)
                    if key not in memo or memo[key] < new_score:
                        memo[key] = new_score
                        state = (new_score, user_id + 1, new_caps_tuple, new_assignments)
                        next_beam.append(state)

        beam = heapq.nlargest(beam_width, next_beam, key=lambda x: x[0])

    best_score, _, final_caps, best_assignment = max(beam, key=lambda x: x[0])

    ad_usage = defaultdict(int)
    for ad_id in best_assignment:
        ad_usage[ad_id] += 1

    result = []
    for user_index, ad_index in enumerate(best_assignment):
        result.append((
            users[user_index]["user_id"],
            ads[ad_index]["ad_id"],
            scores[user_index][ad_index]
        ))

    end = time.time()
    result_set.append({"execution_time" : end - start, "average_score" : average([r[2] for r in result]),
                       "ad_coverage" : (len(set([r[1] for r in result]))/200) * 100, "user_count" : len([r[0] for r in result]),
                       "ad_count" : len(set([r[1] for r in result])) })
    print(f"{'Approach: Dynamic Programming'} | Execution time: {end - start:6.4f} sec")

    return result_set