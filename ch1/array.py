# coding: utf-8

import numpy as np

a = np.array([1, 2, 3])

print(a)
print(np.ndim(a))
print(np.shape(a))

b = np.array([[1, 2], [3, 4], [5, 6]])

print(b)
print(np.ndim(b))
print(np.shape(b))

print(np.dot(a, b))

