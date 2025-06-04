def evaluate_all(results_dict):
    print("\n=== Evaluation Summary ===")
    for method, result in results_dict.items():
        total_score = sum([r[2] for r in result])
        print(f"{method}: Total Match Score = {total_score:.2f}")