#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def generate_guassian(mean, covar, samples, color, label, marker):
    x, y = np.random.multivariate_normal(mean, covar, samples).T
    plt.scatter(x, y, c=color, marker=marker, label=label)


def main():
    generate_guassian(
        [9, 0],
        [[25, 30], [15, 0]],
        100,
        'blue',
        '+1',
        ','
    )
    generate_guassian(
        [-10, 0],
        [[20, 30], [15, 0]],
        100,
        'red',
        '-1',
        '^'
    )
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
