#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def generate_guassian(mean, covar, samples, color, label, marker):
    x, y = np.random.multivariate_normal(mean, covar, samples).T
    plt.scatter(x, y, c=color, marker=marker, label=label)


def main():
    generate_guassian(
        [175, 80],
        [[25, 30], [15, 12]],
        500,
        'blue',
        'Men',
        ','
    )
    generate_guassian(
        [169, 69],
        [[20, 30], [15, 10]],
        500,
        'red',
        'Women',
        '^'
    )
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (Kg)')
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
