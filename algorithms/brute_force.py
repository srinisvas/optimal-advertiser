import time

def match_ads(users, ads, matrix):
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
    print(f"{"Approach: Brute Force"} | Execution time: {end - start:6.4f} sec")
    return results