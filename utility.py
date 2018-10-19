
class Utility:
	def __init__(self, r_payoff, discount):
		self.discount = discount
		self.r_payoff = r_payoff
		
	def of(self, row_player, col_player):
		pairings = [self.all_a_all_a, self.all_a_all_b, self.all_a_tft, self.all_a_not_tft,
					self.all_b_all_a, self.all_b_all_b, self.all_b_tft, self.all_b_not_tft,
					self.tft_all_a, self.tft_all_b, self.tft_tft, self.tft_not_tft,
					self.not_tft_all_a, self.not_tft_all_b, self.not_tft_tft, self.not_tft_not_tft]

		players = ['all_a', 'all_b', 'tft', 'not_tft']

		assert row_player in players
		assert col_player in players

		return pairings[players.index(row_player) * 4 + players.index(col_player)]()

	def all_a_all_a(self):
		return self.r_payoff[0][0] / (1. - self.discount)

	def all_a_all_b(self):
		return self.r_payoff[0][1] / (1. - self.discount)

	def all_a_tft(self):
		return self.r_payoff[0][0] / (1. - self.discount)

	def all_a_not_tft(self):
		return self.r_payoff[0][1] / (1. - self.discount)

	def all_b_all_a(self):
		return self.r_payoff[1][0] / (1. - self.discount)

	def all_b_all_b(self):
		return self.r_payoff[1][1] / (1. - self.discount)

	def all_b_tft(self):
		return self.r_payoff[1][1] * self.discount / (1. - self.discount) + self.r_payoff[1][0]

	def all_b_not_tft(self):
		return self.r_payoff[1][0] * self.discount / (1. - self.discount) + self.r_payoff[1][1]

	def tft_all_a(self):
		return self.r_payoff[0][0] / (1. - self.discount)

	def tft_all_b(self):
		return self.r_payoff[1][1] * self.discount / (1. - self.discount) + self.r_payoff[0][1]

	def tft_tft(self):
		return self.r_payoff[0][0] / (1. - self.discount)

	def tft_not_tft(self):
		return self.r_payoff[0][1] / (1. - self.discount ** 4) + \
			   self.r_payoff[1][1] * self.discount / (1. - self.discount ** 4) + \
			   self.r_payoff[1][0] * self.discount ** 2 / (1. - self.discount ** 4) + \
			   self.r_payoff[0][0] * self.discount ** 3 / (1. - self.discount ** 4)

	def not_tft_all_a(self):
		return self.r_payoff[1][0] / (1. - self.discount)

	def not_tft_all_b(self):
		return self.r_payoff[0][1] * self.discount / (1. - self.discount) + self.r_payoff[1][1]

	def not_tft_tft(self):
		return self.r_payoff[1][0] / (1. - self.discount ** 4) + \
			   self.r_payoff[1][1] * self.discount / (1. - self.discount ** 4) + \
			   self.r_payoff[0][1] * self.discount ** 2 / (1. - self.discount ** 4) + \
			   self.r_payoff[0][0] * self.discount ** 3 / (1. - self.discount ** 4)

	def not_tft_not_tft(self):
		return self.r_payoff[1][1] / (1. - self.discount ** 2) + \
			   self.r_payoff[0][0] * self.discount / (1. - self.discount ** 2)

