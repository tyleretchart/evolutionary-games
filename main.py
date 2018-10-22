from population import Population
from utility import Utility

# cardinals
T = 5
R = 3
P = 2
S = 1

# players
PLAYERS = ['all_a', 'all_b', 'tft', 'not_tft', 'exploit']

# games
PRISONERS_DILEMMA = [[R, S], [T, P]]
STAG_HUNT = [[4, 3], [0, 3]]
BATTLE_OF_THE_SEXES = [[0, 2], [1, 0]]

# discount
DISCOUNT = .95

u = Utility(PRISONERS_DILEMMA, DISCOUNT, PLAYERS)

initial_player_percentages = [0, .8, .2, 0, 0]

pop = Population(
    players=PLAYERS,
    player_percentages=initial_player_percentages,
    u=u,
    row_size=5,
    col_size=5)

# r = pop.random_utility_lattice()
# print(r)

# r = pop.neighborhood_utility_lattice()
# print(r)

new_pop = pop.imitator_dynamics(pop.neighborhood_utility_lattice())
print(pop.population)
print("===========================")
print(new_pop)

# new_pop = pop.replicator_dynamics(pop.random_utility_lattice(),
#                                   initial_player_percentages)
# print(pop.population)
# print("===========================")
# print(new_pop)
