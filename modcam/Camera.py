#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

from .lens import lens_types
from .rotation import rot_alt, rot_az, square_pts


def radial(x, *c):
    return sum((ci * x**i for i, ci in enumerate(c[1:], 2)), c[0] * x)


class Camera:
    def __init__(self, focal_length, lens_type, sensor_width, sensor_height):
        if type(lens_type) is str and lens_type not in lens_types:
            raise ValueError("Not a known lens type.")

        w = sensor_width / 2
        h = sensor_height / 2

        x, y = square_pts(1000)
        x *= w
        y *= h

        self.a = np.arctan2(y, x)

        coefs = [1]
        if type(lens_type) is map:
            coefs = lens_type
            lens_type = "rectilinear"

        self.r = lens_types[lens_type](np.sqrt(x * x + y * y), focal_length)
        self.r = radial(self.r, *coefs)

    def rotate(self, alt, az, theta):
        """
        alt: from center
        az: camera position
        theta: camera rotation
        """
        self.r, self.a = rot_az(self.r, self.a, np.deg2rad(theta))
        self.r, self.a = rot_alt(self.r, self.a, np.deg2rad(alt))
        self.r, self.a = rot_az(self.r, self.a, np.deg2rad(az))

    def plot(self, fig=None):
        ax = plt.axes(projection="polar") if fig is None else fig
        ax.plot(self.a, np.rad2deg(self.r))
        if fig is None:
            plt.show()
