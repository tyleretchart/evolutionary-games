import numpy as np


class Population:
    def __init__(self,
                 players,
                 player_percentages,
                 u,
                 row_size=30,
                 col_size=30):
        self.players = players
        self.u = u
        self.row_size = row_size
        self.col_size = col_size

        self.population = self.__sample_new_population(player_percentages)

        self.index_mat = np.array(
            [[(r, c) for c in range(5)] for r in range(5)])
        self.west_index_mat = np.roll(self.index_mat, 1, axis=0)
        self.east_index_mat = np.roll(self.index_mat, -1, axis=0)
        self.north_index_mat = np.roll(self.index_mat, 1, axis=1)
        self.south_index_mat = np.roll(self.index_mat, -1, axis=1)
        self.north_east_index_mat = np.roll(self.north_index_mat, -1, axis=0)
        self.north_west_index_mat = np.roll(self.north_index_mat, 1, axis=0)
        self.south_east_index_mat = np.roll(self.south_index_mat, -1, axis=0)
        self.south_west_index_mat = np.roll(self.south_index_mat, 1, axis=0)

    def random_utility_lattice(self):
        player_utility = {}
        for p in self.players:
            player_utility[p] = 0
            for opponent in self.players:
                player_utility[p] += self.u.of(
                    p, opponent) * self.player_percentages[opponent]

        population_utility = np.copy(self.population)
        for p in player_utility.keys():
            population_utility[population_utility == p] = player_utility[p]
        return population_utility.astype(np.float64)

    def neighborhood_utility_lattice(self):
        population_utility = np.copy(self.population)
        for row_index in range(self.index_mat.shape[0]):
            for col_index in range(self.index_mat.shape[1]):
                player = self.__strategy_at_index(self.index_mat, row_index,
                                                  col_index)
                other_players = [
                    self.__strategy_at_index(self.west_index_mat, row_index,
                                             col_index),
                    self.__strategy_at_index(self.east_index_mat, row_index,
                                             col_index),
                    self.__strategy_at_index(self.north_index_mat, row_index,
                                             col_index),
                    self.__strategy_at_index(self.south_index_mat, row_index,
                                             col_index),
                    self.__strategy_at_index(self.north_east_index_mat,
                                             row_index, col_index),
                    self.__strategy_at_index(self.north_west_index_mat,
                                             row_index, col_index),
                    self.__strategy_at_index(self.south_east_index_mat,
                                             row_index, col_index),
                    self.__strategy_at_index(self.south_west_index_mat,
                                             row_index, col_index),
                ]
                population_utility[row_index][col_index] = np.mean(
                    [self.u.of(player, op) for op in other_players])
        return population_utility.astype(np.float64)

    def imitator_dynamics(self, utility_mat):
        new_population = np.copy(self.population)

        for row_index in range(self.index_mat.shape[0]):
            for col_index in range(self.index_mat.shape[1]):
                best_neighbor_index = np.argmax([
                    self.__score_at_index(self.index_mat, utility_mat,
                                          row_index, col_index),
                    self.__score_at_index(self.west_index_mat, utility_mat,
                                          row_index, col_index),
                    self.__score_at_index(self.east_index_mat, utility_mat,
                                          row_index, col_index),
                    self.__score_at_index(self.north_index_mat, utility_mat,
                                          row_index, col_index),
                    self.__score_at_index(self.south_index_mat, utility_mat,
                                          row_index, col_index),
                    self.__score_at_index(self.north_east_index_mat,
                                          utility_mat, row_index, col_index),
                    self.__score_at_index(self.north_west_index_mat,
                                          utility_mat, row_index, col_index),
                    self.__score_at_index(self.south_east_index_mat,
                                          utility_mat, row_index, col_index),
                    self.__score_at_index(self.south_west_index_mat,
                                          utility_mat, row_index, col_index),
                ])

                best_neighbor_mat = [
                    self.index_mat,
                    self.west_index_mat,
                    self.east_index_mat,
                    self.north_index_mat,
                    self.south_index_mat,
                    self.north_east_index_mat,
                    self.north_west_index_mat,
                    self.south_east_index_mat,
                    self.south_west_index_mat,
                ][best_neighbor_index]

                new_population[row_index][
                    col_index] = self.__strategy_at_index(
                        best_neighbor_mat, row_index, col_index)
        return new_population

    def replicator_dynamics(self, utility_mat, player_percentages):
        pop_utility_means = {
            k: np.mean(utility_mat[self.population == k]) if np.any(
                self.population == k) else 0.
            for k in self.player_percentages.keys()
        }

        u_star = np.sum([
            mean * self.player_percentages[k]
            for k, mean in pop_utility_means.items()
        ])

        pop_utilities_delta = {
            k: v * (pop_utility_means[k] - u_star)
            for k, v in self.player_percentages.items()
        }

        for i, player in enumerate(self.players):
            player_percentages[i] += pop_utilities_delta[player]

        return self.__sample_new_population(player_percentages)

    def __sample_new_population(self, player_percentages):
        num_players = self.row_size * self.col_size
        num_strat = [
            int(num_players * percent) for percent in player_percentages
        ]

        population = []
        for i, p in enumerate(self.players):
            population.extend([p] * num_strat[i])

        # TODO: be more flexible
        assert len(population) == num_players

        population = np.array(population)
        np.random.shuffle(population)
        return population.reshape((self.row_size, self.col_size))

    @property
    def player_percentages(self):
        return {
            p: np.sum(p == self.population) / np.size(self.population)
            for p in self.players
        }

    def __strategy_at_index(self, mat, row_index, col_index):
        index = mat[row_index][col_index]
        return self.population[index[0]][index[1]]

    def __score_at_index(self, mat, utility_mat, row_index, col_index):
        index = mat[row_index][col_index]
        return utility_mat[index[0]][index[1]]
