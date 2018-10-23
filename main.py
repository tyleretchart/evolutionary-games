import collections

import grapher
from population import Population
from utility import Utility

# players
PLAYERS = ['all_a', 'all_b', 'tft', 'not_tft']

# games
PRISONERS_DILEMMA = [[3, 1], [5, 2]]
STAG_HUNT = [[4, 3], [0, 3]]
BATTLE_OF_THE_SEXES = [[0, 2], [1, 0]]

DISCOUNT = .95
DISCOUNT = .97
# DISCOUNT = .99

u = Utility(PRISONERS_DILEMMA, DISCOUNT, PLAYERS)

initial_player_percentages = [.25, .25, .25, .25]

pop = Population(
    players=PLAYERS,
    player_percentages=initial_player_percentages,
    u=u,
    row_size=300,
    col_size=300)

results = {k: [] for k in PLAYERS}
maxlen = 10
histories = {k: collections.deque(range(maxlen), maxlen) for k in PLAYERS}
while True:
    for player, percent in pop.player_percentages.items():
        results[player].append(percent)
        histories[player].append(percent)

    should_continue = False
    for history in histories.values():
        if len(set(round(h, 6) for h in history)) > 1:
            should_continue = True
            break

    if not should_continue:
        break

    pop.step_with_replicator_dynamics(lr=.001)

grapher.graph_percentages(results)
