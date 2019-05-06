# coding: utf-8

import numpy as np

# array

arr = np.array([1, 4, 5, 9])

print(arr,type(arr))

# sum

arr2 = np.array([4, 6, 0, 4])
print(arr2)

print(arr + arr2)

#martrix

mar = np.array([[1, 2], [4, 5]])
print(mar)

print(mar.shape)

print(type(mar))

mar2 = np.array([[4, 5], [8, 9]])

print(mar * mar2)

print(mar * 10)