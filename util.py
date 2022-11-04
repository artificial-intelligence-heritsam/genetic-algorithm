import numpy as np

POP_SIZE = 10
P_C = 0.7
P_M = 0.1


def heuristic(x, y):
    x0 = np.power(np.cos(np.radians(x)) + np.sin(np.radians(y)), 2)
    x1 = np.power(x, 2) + np.power(y, 2)
    return x0 / (x1 + 0.000001)


def binary_to_decimal(binary):
    decimal = 0

    for i, bit in enumerate(binary):
        decimal += int(bit) * (2 ** (len(binary) - i - 1))

    return decimal

def random_genes(length):
    return ''.join(str(np.random.randint(0, 10)) for _ in range(length))
