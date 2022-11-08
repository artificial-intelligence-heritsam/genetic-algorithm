import numpy as np

# Genetic Algorithm Design
POP_SIZE = 10
CHROMOSOME_SIZE = 20
P_C = 0.7
P_M = 0.1


def heuristic(x, y):
    """Heuristic function to be minimized"""
    x0 = np.power(np.cos(np.radians(x)) + np.sin(np.radians(y)), 2)
    x1 = np.power(x, 2) + np.power(y, 2)
    return x0 / (x1 + 0.000001)


def binary_to_decimal(binary):
    """Converts a binary string to a decimal number"""
    decimal = 0

    for i, bit in enumerate(binary):
        decimal += int(bit) * (2 ** (len(binary) - i - 1))

    return decimal

def random_genes():
    """Generates a random chromosome"""
    return ''.join(str(np.random.randint(0, 10)) for _ in range(CHROMOSOME_SIZE))
