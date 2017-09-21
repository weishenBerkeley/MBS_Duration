# All the functions here
from __future__ import division, print_function

import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt
from random import seed
from random import randrange

def Vasicek_simulation(a, b, r0, sigma, n = 1000):
    rate_path = [r0]
    dt = 1 / 252
    for i in range(n):
        rand = np.random.normal()
        dr = a * (b - rate_path[-1]) * dt + sigma * np.sqrt(dt * rate_path[-1]) * rand
        rate_path.append(rate_path[-1] + dr)
    return np.array(rate_path)

def bond_price(r, alpha, beta = 100):
    """
    This function assume the bond price follow the function form
    P = beta * exp(-alpha * r**2)
    :param alpha:
    :param beta:
    :return:
    """
    return beta * np.exp(- alpha * r ** 2)

def bond_duration(r, alpha, beta = 100):
    """
    Since the functional form of bond price is certain, then the duration is also certain
    :param r:
    :param alpha:
    :param beta:
    :return:
    """
    return alpha * np.multiply(r, bond_price(r, alpha, beta))

