#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    X = np.linspace(-25, 25, 10000)
    plt.plot(X, np.exp(- 10 * pow(X, 2)), c='g', label='gamma=10')
    plt.plot(X, np.exp(- .5 * pow(X, 2)), c='r', label='gamma=1/2')
    plt.plot(X, np.exp(- .01 * pow(X, 2)), c='b', label='gamma=1/100')
    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
