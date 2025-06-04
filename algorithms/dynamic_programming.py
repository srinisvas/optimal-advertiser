def match_ads(users, ads, matrix):
    from functools import lru_cache

    n = len(users)
    m = len(ads)

    @lru_cache(None)
    def dp(i, used):
        if i == n:
            return 0
        best = 0
        for j in range(m):
            if not (used & (1 << j)):
                score = matrix[i][j] + dp(i + 1, used | (1 << j))
                best = max(best, score)
        return best

    dp(0, 0)

    return [(users[i]["user_id"], "AD_UNKNOWN", 0) for i in range(n)]