def match_ads(users, ads, matrix):
    best_score = 0
    best_assignment = []
    n, m = len(users), len(ads)

    def backtrack(i, used, current_score, current_assignment):
        nonlocal best_score, best_assignment
        if i == n:
            if current_score > best_score:
                best_score = current_score
                best_assignment = list(current_assignment)
            return
        for j in range(m):
            if j not in used:
                used.add(j)
                current_assignment.append((users[i]["user_id"], ads[j]["ad_id"], matrix[i][j]))
                backtrack(i + 1, used, current_score + matrix[i][j], current_assignment)
                current_assignment.pop()
                used.remove(j)

    backtrack(0, set(), 0, [])
    return best_assignment