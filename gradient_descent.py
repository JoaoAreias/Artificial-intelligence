""" Just some code to solve
the gradient descent exercises
from brilliant.org
"""
import numpy as np

def Q(w):
	"""Function to be
	minimized"""
	_w = w**2
	return 0.5*np.sum(w)

def d_Q(w):
	"""In this case the derivative
	is simply the parameters itself
	"""
	return w

def minimize(x_0, diff, nu, epochs):
	"""Gradient descent"""
	x = x_0
	for epoch in range(epochs):
		x = x - nu*diff(x)
	return x


w_0 = np.array([1, 0])
print(f"w_0 = {w_0}\nQ(w_0) = {Q(w_0)}\n")

w = minimize(w_0, d_Q, 0.01, 100)
print(f"w = {w}\nQ(w) = {Q(w)}\n")
