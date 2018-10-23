from population import Population
from utility import Utility
import grapher

# cardinals
T = 5
R = 3
P = 2
S = 1

# players
PLAYERS = ['all_a', 'all_b', 'tft', 'not_tft']

# games
PRISONERS_DILEMMA = [[R, S], [T, P]]
STAG_HUNT = [[4, 3], [0, 3]]
BATTLE_OF_THE_SEXES = [[0, 2], [1, 0]]

# discount
DISCOUNT = .95

u = Utility(PRISONERS_DILEMMA, DISCOUNT, PLAYERS)

initial_player_percentages = [.25, .25, .25, .25]

pop = Population(
    players=PLAYERS,
    player_percentages=initial_player_percentages,
    u=u,
    row_size=30,
    col_size=30)

# r = pop.random_utility_lattice()
# print(r)

# r = pop.neighborhood_utility_lattice()
# print(r)

results = {k: [] for k in PLAYERS}
for i in range(50):
    for player, percent in pop.player_percentages.items():
        results[player].append(percent)
    pop.step_with_imitator_dynamics()

grapher.graph_percentages(results, "test")
# new_pop = pop.replicator_dynamics(pop.random_utility_lattice(),
#                                   initial_player_percentages)
# print(pop.population)
# print("===========================")
# print(new_pop)
