import numpy as np


# functie care sa translateze [0, 1] -> [a, b]
def random(a, b, n):
    return (a + np.random.rand(n) * (b - a))