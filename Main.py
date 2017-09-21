# main program entrance
from __future__ import division, print_function
import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt
from random import seed
from random import randrange
import Functions as fn

if __name__ == "__main__":
    a = 0.1
    b = 0.08
    r0 = 0.03
    sigma = 0.1
    #for i in range(10):
    #    path = fn.Vasicek_simulation(a, b, r0, sigma)
    #    plt.plot(path)
    #plt.show()
    alpha = 8

    path = fn.Vasicek_simulation(a, b, r0, sigma)
    bonds = fn.bond_price(path, alpha)

    plt.plot(path)
    plt.show()
    plt.plot(bonds)
    plt.show()