#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import sklearn.datasets
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from generate_data import pgflist


def main():
    X, y = sklearn.datasets.make_circles(n_samples=1000, factor=.3, noise=.05)

    pgflist(X[y == 1, 0], X[y == 1, 1], 'red')
    pgflist(X[y == 0, 0], X[y == 0, 1], 'blue')

    plt.scatter(pow(X[y == 1, 0], 2) + pow(X[y == 1, 1], 2), np.arctan2(X[y == 1, 0],X[y == 1, 1]), c="red",
                s=20, edgecolor='k')
    plt.scatter(pow(X[y == 0, 0], 2) + pow(X[y == 0, 1], 2), np.arctan2(X[y == 0, 0],X[y == 0, 1]), c="blue",
                s=20, edgecolor='k')

    YY = np.linspace(-4, 4, 1000)
    plt.plot(.5 * np.ones_like(YY), YY, c='m')
    plt.show()


if __name__ == '__main__':
    main()
