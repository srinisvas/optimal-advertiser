Algorithm MatchAdsGreedy(users, ads, matrix):
Input:
    users: list of user profiles
    ads: list of ad profiles
    matirx: 2D list where matrix[i][j] = score for user i and j
Output:
    list of (user_id, ad_id, score) assignments

results <- empty list
matched_ads <- empty set

For each user_index from 0 to number of users - 1:
    best_ad_idx <- -1
    max_score <- -1

    For each ad_index from 0 to number of ads - 1:
        If ad_index not in matched_ads and score > max_score:
            max_score <- score
            best_ad_idx <- ad_index
    
    If best_ad_idx != -1:
        Add best_ad_idx to matched_ads
        Append (user_id, ad_id, max_score) to results
    
Return result