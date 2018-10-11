"""A toy Recurent Neural net
to solve brilliant.org's
challanges
"""
import numpy as np

class RNN(object):
	Whh = np.array([[0.5, 1],[1, 2]])
	Whx = np.array([[1, 0],[-1, 0]])
	Why = np.array([[-1, 1],[ 1, 2]])
	H = np.array([1, 1])

	def predict(self, X):
		"""Gets an input vector X
		and returns the prediction
		for it"""
		H = np.tanh(np.matmul(Whh, H) + np.matmul(Whx, X))
		return np.matmul(Why, H)


model = RNN()
print(model.predict(np.array([4, 4])))