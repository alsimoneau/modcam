#!/usr/bin/env python3

import click
import matplotlib.pyplot as plt

import modcam


@click.command()
@click.argument("filename", type=click.File("r"))
def main(filename):
    ax = plt.axes(projection="polar")

    for i, line in enumerate(filename):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue

        try:
            f, lt, w, h, alt, az, theta = line.split()

            f = float(f)
            if lt not in modcam.lens_types:
                lt = map(float, lt.split(","))
            w = float(w)
            h = float(h)
            alt = float(alt)
            az = float(az)
            if theta == "H":
                theta = 0
            elif theta == "V":
                theta = 90
            else:
                theta = float(theta)

        except ValueError:
            raise ValueError(f"Badly formed line {i} in input")

        cam = modcam.Camera(f, lt, w, h)
        cam.rotate(alt, az, theta)
        cam.plot(ax)
    plt.show()
