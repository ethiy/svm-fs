#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def generate_guassian(mean, covar, samples, color, label, marker):
    x, y = np.random.multivariate_normal(mean, covar, samples).T
    plt.scatter(x, y, c=color, marker=marker, label=label)


def main():
    generate_guassian(
        [200, 80],
        [[25, 30], [15, 12]],
        50,
        'blue',
        '+1',
        ','
    )
    generate_guassian(
        [170, 69],
        [[20, 30], [15, 10]],
        50,
        'red',
        '-1',
        '^'
    )

    # plt.plot([180, 190], [40, 100], 'g--')
    # plt.plot([190, 185], [40, 100], 'c--')
    # plt.plot([185, 185], [40, 100], 'm--')
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
