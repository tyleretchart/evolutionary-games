import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


def graph_percentages(percentages_list_of_dicts,
                      filename,
                      title=None,
                      alpha=.4):
    average_dict = combine_dicts(percentages_list_of_dicts, np.average)
    std_dict = combine_dicts(percentages_list_of_dicts, np.std)

    fig, ax = plt.subplots()
    for key in average_dict:
        plotable = np.array(average_dict[key])
        ax.plot(plotable)
        ax.fill_between(
            np.linspace(0, plotable.shape[0] - 1, plotable.shape[0]),
            plotable + np.array(std_dict[key]),
            plotable - np.array(std_dict[key]),
            alpha=alpha)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    if title:
        plt.title(title)
    plt.xlabel('Iterations')
    plt.ylabel('Population Percentage')
    plt.legend(average_dict)

    plt.savefig(filename)


def combine_dicts(list_of_dicts, f):
    result = {}
    iterations = len(list_of_dicts[0][next(iter(list_of_dicts[0]))])
    for key in list_of_dicts[0]:
        result[key] = []
        for i in range(iterations):
            values = []
            for j in range(len(list_of_dicts)):
                if len(list_of_dicts[j][key]) > i:
                    values.append(list_of_dicts[j][key][i])
            result[key].append(f(values))
    return result


if __name__ == '__main__':
    test = [{
        'all_a': [0.1, 0.15, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.3],
        'all_b': [
            0.15, 0.15, 0.15, 0.5, 0.5, 0.5, 0.5, 1.0, 0.5, 0.5, 0.3, 0.3
        ],
        'exploit': [
            0.1, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.3
        ],
        'not_tft': [
            0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.3
        ],
        'tft': [0.58, 0.58, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 0.3]
    },
            {
                'all_a': [
                    0.1, 0.15, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3
                ],
                'all_b': [
                    0.16, 0.16, 0.16, 0.6, 0.6, 0.6, 0.6, 1.0, 0.6, 0.6, 3.0
                ],
                'exploit': [
                    0.1, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0
                ],
                'not_tft': [
                    0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0
                ],
                'tft': [
                    0.58, 0.58, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.0
                ]
            },
            {
                'all_a': [0.1, 0.15, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'all_b': [0.14, 0.14, 0.14, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
                'exploit': [
                    0.1, 0.2, 0.15, 0.1, 0.15, 0.0, 0.0, 0.0, 0.0, 0.0
                ],
                'not_tft': [0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'tft': [0.58, 0.58, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            },
            {
                'all_a': [0.1, 0.15, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'all_b': [0.12, 0.12, 0.15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'exploit': [0.1, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'not_tft': [0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'tft': [0.58, 0.58, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            },
            {
                'all_a': [0.1, 0.15, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'all_b': [0.14, 0.14, 0.14, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
                'exploit': [0.1, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'not_tft': [0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'tft': [0.58, 0.58, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            }]
    test = [{
        'all_a': [0.1, 0.15, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'all_b': [0.14, 0.14, 0.14, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
        'exploit': [0.1, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'not_tft': [0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'tft': [0.58, 0.58, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    }]
    # graph_imitator_percentages(test)

    graph_percentages(test)
