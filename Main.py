# main program entrance
from __future__ import division, print_function
import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt
from random import seed
from random import randrange
import Functions as fn

if __name__ == "__main__":

    np.random.seed(123)
    a = 0.08
    b = 0.08
    r0 = 0.06
    sigma = 0.2
    #for i in range(10):
    #    path = fn.Vasicek_simulation(a, b, r0, sigma)
    #    plt.plot(path)
    #plt.show()
    alpha = 8
    noise = np.ones(1001) * 0.1
    path = fn.Vasicek_simulation(a, b, r0, sigma)
    bonds = fn.bond_price(path, alpha)
    bonds_real = fn.bond_price_real(path, alpha, noise)

    plt.plot(bonds, label = "theoretical bond price")
    plt.plot(bonds_real, label = 'real bond price')
    plt.legend()
    plt.show()

    # Using the rolling window approximation for a duration

    window = 120
    return_bond = (bonds_real[1:] - bonds_real[:-1]) / bonds_real[1:]
    trancate_rate = path[1:] - path[:-1]
    D = []
    for t in range(len(trancate_rate) - window):
        y = return_bond[t : t+window]
        x = trancate_rate[t : t+window]
        model = sm.OLS(y, x)
        result = model.fit()
        # print(result.summary())
        D.append(- result.params[0])

    theory_duration = fn.bond_duration(path, alpha)
    trancated_D = theory_duration[1:]

    plt.plot(trancated_D[window:], label="Theory duration")
    plt.plot(D, label = "Emprical duration")
    plt.legend()
    plt.show()