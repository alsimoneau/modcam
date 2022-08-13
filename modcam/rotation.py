#!/usr/bin/env python3

import numpy as np


def square_pts(n):
    x = np.concatenate(
        [
            np.linspace(-1, 1, n + 2),
            np.ones(n) * 1,
            np.linspace(1, -1, n + 2),
            np.ones(n + 1) * -1,
        ]
    )

    y = np.concatenate(
        [
            np.ones(n + 1) * 1,
            np.linspace(1, -1, n + 2),
            np.ones(n) * -1,
            np.linspace(-1, 1, n + 2),
        ]
    )

    return x, y


def rot_az(alt, az, theta):
    az = az + theta
    return alt, az


def rot_alt(alt, az, theta):
    a = np.array(
        [
            np.sin(alt) * np.cos(az),
            np.sin(alt) * np.sin(az),
            np.cos(alt),
        ]
    )
    k = np.array([-1, 0, 0])
    b = (
        np.cos(theta) * a
        + np.sin(theta) * np.cross(k, a.T).T
        + np.dot(k, a) * (1 - np.cos(theta)) * k[:, None]
    )

    alt2 = np.arctan2(np.sqrt(b[0] ** 2 + b[1] ** 2), b[2])
    az2 = np.arctan2(b[1], b[0]) % (2 * np.pi)

    return alt2, az2
