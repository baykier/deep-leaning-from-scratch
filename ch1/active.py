# coding: utf-8

import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

print(sigmoid(5))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)


plt.plot(x, y)
plt.ylim(-0.1, 1.1) # 指定y轴的范围
plt.show()

# relu 

def relu(x):
    return np.maximum(0, x)
    
i = np.array([0.5, 1, 2, -1])
m = np.arange(-5,5.0,0.1)
z = relu(m)


plt.plot(m, z)
plt.ylim(-5, 5.0)
plt.show()

def identity_function(x):
    return x


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y