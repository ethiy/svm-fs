#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import sklearn.datasets
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    X, y = sklearn.datasets.make_circles(n_samples=1000, factor=.3, noise=.05)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(pow(X[y == 1, 0], 2), pow(X[y == 1, 1], 2), math.sqrt(2)*X[y == 1, 0]*X[y == 1, 1], c="red",
                s=20, edgecolor='k')
    ax.scatter(pow(X[y == 0, 0], 2), pow(X[y == 0, 1], 2), math.sqrt(2)*X[y == 0, 0]*X[y == 0, 1], c="blue",
                s=20, edgecolor='k')

    XX, ZZ = np.meshgrid(np.arange(-.9, .9, .01), np.arange(-1.5, 1.5, .01))
    YY = .5 * np.ones_like(XX) - XX
    ax.plot_surface(XX, YY, ZZ, cmap='viridis', linewidth=0, antialiased=False, alpha=.5)
    plt.show()


if __name__ == '__main__':
    main()
