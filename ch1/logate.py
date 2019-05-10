# coding: utf-8

# 与逻辑
def gate_and(x, y):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1 * x + w2 * y
    if tmp > theta:
        return 1
    else:
        return 0
print(gate_and(1, 1))

# 或逻辑

def gate_or(x, y):
    w1, w2, theta = 0.5, 0.5, 0.4
    tmp = w1 *x + w2 * y
    if tmp > theta:
        return 1
    else:
        return 0

print(gate_or(1, 0))
print(gate_or(0, 0))

# 与非

def gate_nand(x, y):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1 * x + w2 * y
    if tmp < theta:
        return 1
    else:
        return 0

print(gate_nand(1, 1))
print(gate_nand(1, 0))

# 异或
def gate_xor(x, y):
    m = gate_nand(x, y)
    n = gate_or(x, y)
    return gate_and(m, n)
    
print(gate_xor(1, 0))
print(gate_xor(1,1))
