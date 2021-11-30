import numpy as np
import matplotlib.pyplot as plt
from Lagrange import *

if __name__ == "__main__":
    # x = [-1, -0.2, 1.8, 2.7, 4]
    # y = [5, 4.6, 5.7, 5.02, 4.3]
    # x_i = 2
    x = [0, 0.25, 1.25, 2.12, 3.25]
    y = [2, 1.6, 2.32, 2.02, 2.83]
    x_i = 1.2
    res = lagrange(x, y, True, x_i, True)
    print(f"Result (x = {x_i}): {res[0]}")
    print(f"y = {res[1]}")
