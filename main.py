from algorithms import brute_force, greedy, dynamic_programming, backtracking, iterative_improvement
from utils import data_prep, match_score, evaluator


data = data_prep.load_all_datasets()

user_profiles = data_prep.build_user_profiles(data)
ad_profiles = data_prep.build_ad_profiles(data)

match_matrix = match_score.compute_match_matrix(user_profiles, ad_profiles)

print("\n=========================== Execution Summary ===========================\n")

results = {
    "Brute Force": brute_force.match_ads(user_profiles, ad_profiles, match_matrix),
    "Greedy": greedy.match_ads(user_profiles, ad_profiles, match_matrix),
    #"Dynamic Programming": dynamic_programming.match_ads(user_profiles, ad_profiles, match_matrix),
    #"Backtracking": backtracking.match_ads(user_profiles, ad_profiles, match_matrix),
    "Iterative Improvement": iterative_improvement.match_ads(user_profiles, ad_profiles, match_matrix)
}

evaluator.evaluate_all(results)


