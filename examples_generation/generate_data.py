#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def pgflist(x, y, color):
    for x_, y_ in zip(x,y):
        print('(' + str(x_) + ',' + str(y_) + ') [' + color + ']')


def generate_guassian(mean, covar, samples, **kwargs):
    x, y = np.random.multivariate_normal(mean, covar, samples).T
    pgflist(x, y, kwargs['color'])
    plt.scatter(x, y, **kwargs)


def main():
    generate_guassian(
        [79, 1.75],
        [[2, 1], [1, 2]],
        100,
        color='blue',
        label='+1',
        marker=','
    )
    generate_guassian(
        [84, 3],
        [[.75, 0], [0, .75]],
        100,
        color='red',
        label='-1',
        marker='^'
    )
    generate_guassian(
        [83, 1],
        [[.75, 0], [0, .75]],
        100,
        color='red',
        marker='^'
    )
    generate_guassian(
        [80, -2],
        [[.75, 0], [0, .75]],
        100,
        color='red',
        marker='^'
    )
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
