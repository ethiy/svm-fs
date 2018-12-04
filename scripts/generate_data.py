#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def pgflist(x, y, color):
    for x_, y_ in zip(x,y):
        print('(' + str(x_) + ',' + str(y_) + ') [' + color + ']')


def generate_guassian(mean, covar, samples, color, label, marker):
    x, y = np.random.multivariate_normal(mean, covar, samples).T
    pgflist(x, y, color)
    plt.scatter(x, y, c=color, marker=marker, label=label)


def main():
    generate_guassian(
        [75, 1.75],
        [[1.6, 1], [1, 1.6]],
        100,
        'blue',
        '+1',
        ','
    )
    generate_guassian(
        [84, 1.78],
        [[1.6, 1], [1, 1.6]],
        100,
        'red',
        '-1',
        '^'
    )
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
