import numpy as np

class NeuralNet:
	"""A toy neural network for Brilliant.org
	Neural net course"""
	def __init__(self):
		self.w = np.array([0, 0])
		self.b = 0

	def _hinge_loss(x, y):
		return max(0, 1 - y*(np.matmul(self.w, x) + b))

	def fit(self, data, epochs):
		""" Receive a (x, y) data array and the number of
		epochs, trains until convergencd or until number of
		epochs has been reached"""
		for epoch in range(epochs):
			loss = 0
			for x, y in data:
				_y = np.matmul(self.w, x) + self.b
				if y*_y <= 0:
					loss += 1
					self.w = self.w + y*x
					self.b = self.b + y
			print(f"Epoch {epoch}    Loss:{loss}")
			if loss == 0:
				break


model =  NeuralNet()
data = np.array([
	(np.array([-1, 1]), 1),
	(np.array([ 0,-1]),-1),
	(np.array([10, 1]), 1),
])
model.fit(data=data, epochs=100)
print(model.w)
print(model.b)