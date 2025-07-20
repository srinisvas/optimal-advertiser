from algorithms import brute_force, greedy, dynamic_programming, iterative_improvement
from utils import data_prep, match_score, evaluator


data = data_prep.load_all_datasets()

user_profiles = data_prep.build_user_profiles(data)
ad_profiles = data_prep.build_ad_profiles(data)

match_matrix = match_score.compute_match_matrix(user_profiles, ad_profiles)

print("\n=========================== Execution Summary ===========================\n")

results = {
    "Brute Force": brute_force.match_ads(user_profiles, ad_profiles, match_matrix),
    "Greedy": greedy.match_ads(user_profiles, ad_profiles, match_matrix),
    #"DP with Beam-width(100)": dynamic_programming.match_ads(user_profiles, ad_profiles, match_matrix, 10, 100),
    "DP with Beam-width(50)": dynamic_programming.match_ads(user_profiles, ad_profiles, match_matrix, 10, 50 ),
    "DP with Beam-width(10)": dynamic_programming.match_ads(user_profiles, ad_profiles, match_matrix, 10, 10),
    "DP with Beam-width(5)": dynamic_programming.match_ads(user_profiles, ad_profiles, match_matrix, 10, 5),
    "Iterative Improvement": iterative_improvement.match_ads(user_profiles, ad_profiles, match_matrix)
}

evaluator.evaluate_all(results)
evaluator.plot_results(results)