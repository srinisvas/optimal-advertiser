from numpy.ma.extras import average

def evaluate_all(results_dict):
    print("\n=========================== Evaluation Summary ===========================")
    for method, result_list in results_dict.items():
        data = result_list[0]
        execution_time = data['execution_time']
        average_score = float(data['average_score'])
        ad_coverage = data['ad_coverage']
        user_count = data['user_count']
        ad_count = data['ad_count']

        print("\nApproach: " f"{method} \n")
        print(f"    Execution time = {execution_time:.4f} sec")
        print(f"    Total number of users = {user_count:.2f}")
        print(f"    Total number of assigned advertisements = {ad_count:.2f}")
        print(f"    Average Match Score = {average_score:.2f}")
        print(f"    Ad Coverage Percentage = {ad_coverage:.2f}")

