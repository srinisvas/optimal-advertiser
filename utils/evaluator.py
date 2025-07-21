import matplotlib.pyplot as plt
import matplotlib.ticker as tk

legend = {
    'BF': 'Brute Force Approach',
    'Greedy': 'Greedy Assignment Approach',
    'DP(100)': 'Dynamic Programming with Beam search (beam-width 100)',
    'DP(50)': 'Dynamic Programming with Beam search (beam-width 50)',
    'DP(10)': 'Dynamic Programming with Beam search (beam-width 10)',
    'DP(5)': 'Dynamic Programming with Beam search (beam-width 5)',
    'II': 'Iterative Improvement Approach',
}

def evaluate_all(results_dict):
    print("\n=========================== Evaluation Summary ===========================")
    for method, result_list in results_dict.items():
        data = result_list[0]
        execution_time = data['execution_time']
        average_score = float(data['average_score'])
        ad_coverage = data['ad_coverage']
        user_count = data['user_count']
        ad_count = data['ad_count']

        print("\nApproach: " f"{legend.get(method)} \n")
        print(f"    Execution time = {execution_time:.4f} sec")
        print(f"    Total number of users = {user_count:.2f}")
        print(f"    Total number of assigned advertisements = {ad_count:.2f}")
        print(f"    Average Match Score = {average_score:.2f}")
        print(f"    Ad Coverage Percentage = {ad_coverage:.2f}")


def plot_results(results):
    algorithms = list(results.keys())
    execution_times = []
    match_scores = []
    ad_coverages = []
    for algo in algorithms:
        result_dict = results[algo][0]
        execution_times.append(result_dict['execution_time'])
        match_scores.append(result_dict['average_score'])
        ad_coverages.append(result_dict['ad_coverage'] / 100.0)

    plt.style.use('seaborn-v0_8-whitegrid')
    __, axs = plt.subplots(2, 3, figsize=(20, 6), gridspec_kw={'height_ratios': [3, 1]})

    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'navy', '#d62728']
    bar_width = 0.3

    title_font_size = 12
    label_font_size = 10
    text_font_size = 9
    tick_font_size = 9

    # Plot 1: Execution Time
    axs[0, 0].bar(algorithms, execution_times, color=colors[:len(algorithms)], width=bar_width)
    axs[0, 0].set_title('Execution Time', fontsize=title_font_size)
    axs[0, 0].set_ylabel('Time (seconds)', fontsize=label_font_size)
    axs[0, 0].set_yscale('log')
    axs[0, 0].tick_params(axis='x', rotation=30, labelsize=tick_font_size)
    axs[0, 0].tick_params(axis='y', labelsize=tick_font_size)
    for i, time_val in enumerate(execution_times):
        axs[0, 0].text(i, time_val, f'{time_val:.2f}s', ha='center', va='bottom', fontsize=text_font_size)

    # Plot 2: Average Match Score
    axs[0, 1].bar(algorithms, match_scores, color=colors[:len(algorithms)], width=bar_width)
    axs[0, 1].set_title('Average Match Score', fontsize=title_font_size)
    axs[0, 1].set_ylabel('Avg. Score', fontsize=label_font_size)
    axs[0, 1].tick_params(axis='x', rotation=30, labelsize=tick_font_size)
    axs[0, 1].tick_params(axis='y', labelsize=tick_font_size)
    axs[0, 1].set_ylim(0, max(match_scores) * 1.2)
    for i, score in enumerate(match_scores):
        axs[0, 1].text(i, score, f'{score:.2f}', ha='center', va='bottom', fontsize=text_font_size)

    # Plot 3: Ad Coverage
    axs[0, 2].bar(algorithms, ad_coverages, color=colors[:len(algorithms)], width=bar_width)
    axs[0, 2].set_title('Ad Coverage', fontsize=title_font_size)
    axs[0, 2].set_ylabel('Coverage', fontsize=label_font_size)
    axs[0, 2].tick_params(axis='x', rotation=30, labelsize=tick_font_size)
    axs[0, 2].tick_params(axis='y', labelsize=tick_font_size)
    axs[0, 2].set_ylim(0, 1.1)
    axs[0, 2].yaxis.set_major_formatter(tk.PercentFormatter(xmax=1.0, decimals=0))
    for i, coverage in enumerate(ad_coverages):
        axs[0, 2].text(i, coverage, f'{coverage:.1%}', ha='center', va='bottom', fontsize=text_font_size)

    for ax in axs[1]:
        ax.axis('off')

    table_data = [[k, v] for k, v in legend.items()]
    col_labels = ["Legend", "Method Description"]

    table_ax = axs[1, 1]
    table = table_ax.table(
        cellText=table_data,
        colLabels=col_labels,
        colWidths=[0.3, 1.5],
        cellLoc='center',
        loc='center'
    )

    table.auto_set_font_size(False)
    table.set_fontsize(9.5)
    table.scale(1.2, 1.5)
    table_ax.axis('off')

    plt.tight_layout(rect=[0.02, 0.02, 0.97, 0.97])
    plt.suptitle("Performance Comparison of Ad Assignment Algorithms", fontsize=14, fontweight='bold')
    plt.show()

