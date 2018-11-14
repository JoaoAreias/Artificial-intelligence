"""A toy LSTM to solve 
brilliant.org's challanges

[INCOMPLETE]
"""
from scipy.special import expit
import numpy as np

class LSTM(object):
	def __init__(self):
		self.C  = None
		self.h  = None

	def _forget_gate(self):
		"""Models the output of a forget gate"""
		ft = np.array([1, 0, 0.5])
		return self.C*ft

	def _input_gate(self, X):
		"""Models the output of an input gate"""
		Wi = None
		X = np.concatenate(self.h, X)
		b = None
		return expit(np.matmul(Wi, X) + b)

	def _tanh_gate(self, X):
		"""Creates possible new additions to the cell
		state"""
		Wc = None
		X = np.concatenate(self.h, X)
		b = None
		return np.tanh(np.matmul(Wc, X) + b)

	def _update_cell_state(self, X):
		self.C = self._forget_gate() + self._input_gate(X)* self._tanh_gate(X)

	