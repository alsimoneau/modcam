#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

from .lens import lens_types
from .rotation import rot_alt, rot_az, square_pts


class Camera:
    def __init__(self, focal_length, lens_type, sensor_width, sensor_height):
        if lens_type not in lens_types:
            raise ValueError("Not a known lens type.")

        w = sensor_width / 2
        h = sensor_height / 2

        x, y = square_pts(1000)
        x *= w
        y *= h

        self.a = np.arctan2(y, x)
        self.r = lens_types[lens_type](np.sqrt(x * x + y * y), focal_length)

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
