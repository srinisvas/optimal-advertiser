import time

from algorithms import brute_force, greedy, dynamic_programming, backtracking
from utils import data_prep, match_score, evaluator
from utils.match_score import compute_match_score

data = data_prep.load_all_datasets()

user_profiles = data_prep.build_user_profiles(data)
ad_profiles = data_prep.build_ad_profiles(data)

"""
print(data)
print(user_profiles)
print(ad_profiles)
print(user_profiles[0])
print(ad_profiles[0])
print(compute_match_score(user_profiles[0],ad_profiles[0]))
"""

match_matrix = match_score.compute_match_matrix(user_profiles, ad_profiles)

print(match_matrix)

"""
results = {
    "Brute Force": brute_force.match_ads(user_profiles, ad_profiles, match_matrix),
    "Greedy": greedy.match_ads(user_profiles, ad_profiles, match_matrix),
    "Dynamic Programming": dynamic_programming.match_ads(user_profiles, ad_profiles, match_matrix),
    "Backtracking": backtracking.match_ads(user_profiles, ad_profiles, match_matrix),
}

evaluator.evaluate_all(results)
"""