import matplotlib.pyplot as plt 
import numpy as np 


def graph_percentages(percentages_dict, title=''):
	for key in percentages_dict:
		plt.plot(percentages_dict[key])
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