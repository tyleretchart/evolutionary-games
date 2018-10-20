class Utility:
	# r_payoff is a 2-by-2 matrix need to be in row-major order
	def __init__(self, r_payoff, discount):
		assert discount >= 0. and discount < 1.
		self.discount = discount
		self.r_payoff = r_payoff
		
	# Calculates the total discounted utility of playing row_player against col_player.
	# row_player : string from this list --> ['all_a', 'all_b', 'tft', 'not_tft']
	# col_player : string from this list --> ['all_a', 'all_b', 'tft', 'not_tft']
	def of(self, row_player, col_player):
		pairings = [self._all_a_all_a, self._all_a_all_b, self._all_a_tft,
					self._all_a_not_tft, self._all_a_exploit, self._all_b_all_a,
					self._all_b_all_b, self._all_b_tft, self._all_b_not_tft,
					self._all_b_exploit, self._tft_all_a, self._tft_all_b,
					self._tft_tft, self._tft_not_tft, self._tft_exploit,
					self._not_tft_all_a, self._not_tft_all_b, self._not_tft_tft,
					self._not_tft_not_tft, self._not_tft_exploit, self._exploit_all_a,
					self._exploit_all_b, self._exploit_tft,
					self._exploit_not_tft, self._exploit_exploit]

		players = ['all_a', 'all_b', 'tft', 'not_tft', 'exploit']

		assert row_player in players
		assert col_player in players

		return pairings[players.index(row_player) * 5 + players.index(col_player)]()

	def _all_a_all_a(self):
		return self.r_payoff[0][0] / (1. - self.discount)

	def _all_a_all_b(self):
		return self.r_payoff[0][1] / (1. - self.discount)

	def _all_a_tft(self):
		return self.r_payoff[0][0] / (1. - self.discount)

	def _all_a_not_tft(self):
		return self.r_payoff[0][1] / (1. - self.discount)

	def _all_a_exploit(self):
		return self.r_payoff[0][1] / (1. - self.discount)

	def _all_b_all_a(self):
		return self.r_payoff[1][0] / (1. - self.discount)

	def _all_b_all_b(self):
		return self.r_payoff[1][1] / (1. - self.discount)

	def _all_b_tft(self):
		return self.r_payoff[1][1] * self.discount / \
			(1. - self.discount) + self.r_payoff[1][0]

	def _all_b_not_tft(self):
		return self.r_payoff[1][0] * self.discount / \
			(1. - self.discount) + self.r_payoff[1][1]

	def _all_b_exploit(self):
		return self.r_payoff[1][1] * self.discount ** 2 / (1. - self.discount) + \
			   self.r_payoff[1][1] + self.r_payoff[1][0] * self.discount

	def _tft_all_a(self):
		return self.r_payoff[0][0] / (1. - self.discount)

	def _tft_all_b(self):
		return self.r_payoff[1][1] * self.discount / \
			(1. - self.discount) + self.r_payoff[0][1]

	def _tft_tft(self):
		return self.r_payoff[0][0] / (1. - self.discount)

	def _tft_not_tft(self):
		return self.r_payoff[0][1] / (1. - self.discount ** 4) + \
			   self.r_payoff[1][1] * self.discount / (1. - self.discount ** 4) + \
			   self.r_payoff[1][0] * self.discount ** 2 / (1. - self.discount ** 4) + \
			   self.r_payoff[0][0] * self.discount ** 3 / (1. - self.discount ** 4)

	def _tft_exploit(self):
		return self.r_payoff[0][1] / (1. - self.discount ** 3) + \
			   self.r_payoff[1][1] * self.discount / (1. - self.discount ** 3) + \
			   self.r_payoff[1][0] * self.discount ** 2 / (1. - self.discount ** 3)

	def _not_tft_all_a(self):
		return self.r_payoff[1][0] / (1. - self.discount)

	def _not_tft_all_b(self):
		return self.r_payoff[0][1] * self.discount / \
			(1. - self.discount) + self.r_payoff[1][1]

	def _not_tft_tft(self):
		return self.r_payoff[1][0] / (1. - self.discount ** 4) + \
			   self.r_payoff[1][1] * self.discount / (1. - self.discount ** 4) + \
			   self.r_payoff[0][1] * self.discount ** 2 / (1. - self.discount ** 4) + \
			   self.r_payoff[0][0] * self.discount ** 3 / (1. - self.discount ** 4)

	def _not_tft_not_tft(self):
		return self.r_payoff[1][1] / (1. - self.discount ** 2) + \
			   self.r_payoff[0][0] * self.discount / (1. - self.discount ** 2)

	def _not_tft_exploit(self):
		return self.r_payoff[0][1] * self.discount ** 3 / (1. - self.discount) + \
			   self.r_payoff[1][1] + self.r_payoff[0][0] * self.discount + \
			   self.r_payoff[1][1] * self.discount **2

	def _exploit_all_a(self):
		return self.r_payoff[1][0] / (1. - self.discount)

	def _exploit_all_b(self):
		return self.r_payoff[1][1] * self.discount ** 2 / (1. - self.discount) + \
			   self.r_payoff[1][1] + self.r_payoff[0][1] * self.discount

	def _exploit_tft(self):
		return self.r_payoff[1][0] / (1. - self.discount ** 3) + \
			   self.r_payoff[1][1] * self.discount / (1. - self.discount ** 3) + \
			   self.r_payoff[0][1] * self.discount ** 2 / (1. - self.discount ** 3)

	def _exploit_not_tft(self):
		return self.r_payoff[1][0] * self.discount ** 3 / (1. - self.discount) + \
			   self.r_payoff[1][1] + self.r_payoff[0][0] * self.discount + \
			   self.r_payoff[1][1] * self.discount **2

	def _exploit_exploit(self):
		return self.r_payoff[1][1] * self.discount ** 2 / (1. - self.discount) + \
			   self.r_payoff[1][1] + self.r_payoff[0][0] * self.discount

