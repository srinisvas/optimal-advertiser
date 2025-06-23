import time

def match_ads(users, ads, matrix):
    results = []
    start = time.time()
    for user_idx, scores in enumerate(matrix):
        best_ad_idx = max(range(len(scores)), key=lambda i: scores[i])
        results.append((users[user_idx]["user_id"], ads[best_ad_idx]["ad_id"], scores[best_ad_idx]))
    end = time.time()
    print(f"{"Brute Force"} | Time: {end - start:6.4f} sec")
    return results