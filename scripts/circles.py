#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sklearn.datasets
import matplotlib.pyplot as plt


def main():
    X, y = sklearn.datasets.make_circles(n_samples=1000, factor=.3, noise=.05)

    plt.scatter(X[y == 1, 0], X[y == 1, 1], c="red",
                s=20, edgecolor='k')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c="blue",
                s=20, edgecolor='k')
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.show()


if __name__ == '__main__':
    main()
