import argparse
import collections
import json

import numpy as np

import grapher
from population import Population
from utility import Utility

GAMES = {
    'prisoners_dilemma': [[3, 1], [5, 2]],
    'stag_hunt': [[4, 3], [0, 3]],
    'battle_of_the_sexes': [[0, 2], [1, 0]],
}


def run(dynamic='replicator',
        game='prisoners_dilemma',
        percents=[.25, .25, .25, .25],
        agents=['all_a', 'all_b', 'tft', 'not_tft'],
        trials=50,
        beta=.99,
        window=10,
        round_to=5,
        lr=.001,
        row_size=30,
        col_size=30,
        random=False):
    if random:
        percents = np.random.uniform(size=len(agents))
        percents /= np.sum(percents)
    params = locals()

    results = []
    for _ in range(trials):
        result = {k: [] for k in agents}
        histories = {
            k: collections.deque(range(window), maxlen=window)
            for k in agents
        }

        u = Utility(GAMES[game], beta, agents)

        pop = Population(
            players=agents,
            player_percentages=percents,
            u=u,
            row_size=row_size,
            col_size=col_size)

        while True:
            for player, percent in pop.player_percentages.items():
                result[player].append(percent)
                histories[player].append(percent)

            should_continue = False
            for history in histories.values():
                if len(set(round(h, round_to) for h in history)) > 1:
                    should_continue = True
                    break

            if not should_continue:
                break

            getattr(pop, f'step_with_{dynamic}_dynamics')(lr=lr)

        results.append(result)

    params_to_save = {
        k: v
        for k, v in params.items() if k not in ('row_size', 'col_size', 'lr',
                                                'round_to', 'window', 'random')
    }
    # to shorten the filename...
    params_to_save['percents'] = np.round(
        params_to_save['percents'], decimals=2).tolist()
    grapher.graph_percentages(results,
                              f'results/{json.dumps(params_to_save)}.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--dynamic', type=str)
    parser.add_argument('-g', '--game', type=str)
    parser.add_argument('-p', '--percents', type=float, nargs='+')
    parser.add_argument('-a', '--agents', type=str, nargs='+')
    parser.add_argument('-t', '--trials', type=int)
    parser.add_argument('-b', '--beta', type=float)
    parser.add_argument('-w', '--window', type=int)
    parser.add_argument('--round-to', type=int)
    parser.add_argument('-l', '--lr', type=float)
    parser.add_argument('-r', '--row-size', type=float)
    parser.add_argument('-c', '--col-size', type=float)
    parser.add_argument('--random', action='store_true')

    args = parser.parse_args()
    run(**{k: v for k, v in dict(vars(args)).items() if v is not None})
