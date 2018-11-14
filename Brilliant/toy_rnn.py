"""A toy Recurent Neural net
to solve brilliant.org's
challanges
"""
import numpy as np

class RNN(object):
	def __init__(self):
		self.Whh = np.array([[0.5, 1],[1, 2]])
		self.Whx = np.array([[1, 0],[-1, 0]])
		self.Why = np.array([[-1, 1],[1, 2]])
		self.H = np.array([1, 1])

	def predict(self, X):
		"""Gets an input vector X
		and returns the prediction
		for it"""
		self.H = np.tanh(np.matmul(self.Whh, self.H) + np.matmul(self.Whx, X))
		return np.matmul(self.Why, self.H)


model = RNN()
print(model.predict(np.array([4, 4])))