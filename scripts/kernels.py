#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    X = np.linspace(-10, 10, 10000)
    plt.plot(X, 3 * np.tanh(X), c='g', label='gamma=3, c=0')
    plt.plot(X, .5 * np.tanh(X + 2), c='r', label='gamma=1/2, c=2')
    plt.plot(X, np.tanh(X + 1), c='b', label='gamma=1, c = 1')
    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
