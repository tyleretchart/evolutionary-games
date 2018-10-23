import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def graph_percentages(percentages_dict, title=None):
    fig, ax = plt.subplots()
    for key in percentages_dict:
        ax.plot(percentages_dict[key])
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    if title:
        plt.title(title)
    plt.xlabel('Iterations')
    plt.ylabel('Population Percentage')
    plt.legend(percentages_dict)
    plt.show()


"""
test = {
  'all_a': [0.1, 0.15, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'all_b': [0.12, 0.12, 0.15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'exploit': [0.1, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'not_tft': [0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'tft': [0.58, 0.58, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
}
graph_percentages(test)
"""
