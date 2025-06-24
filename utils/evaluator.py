from numpy.ma.extras import average


def evaluate_all(results_dict):
    print("\n=========================== Evaluation Summary ===========================")
    for method, result in results_dict.items():
        average_score = average([r[2] for r in result])
        ad_coverage = (len(set([r[1] for r in result]))/200) * 100
        user_count = len([r[0] for r in result])
        ad_count = len(set([r[1] for r in result]))
        print("\nApproach: " f"{method} \n")
        print(f"    Total number of users = {user_count:.2f}")
        print(f"    Total number of assigned advertisements = {ad_count:.2f}")
        print(f"    Average Match Score = {average_score:.2f}")
        print(f"    Ad Coverage Percentage = {ad_coverage:.2f}")