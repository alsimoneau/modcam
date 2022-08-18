#!/usr/bin/env python3

import click
import matplotlib.pyplot as plt
import modcam
import numpy as np


@click.command()
@click.argument("filename", type=click.File("r"))
@click.argument(
    "n",
    required=False,
    default=1000,
    help="Computation resolution [default:1000]",
)
@click.option("-h", "--horizon", is_flag=True, help="Draws the horizon")
def main(filename, n, horizon):
    ax = plt.axes(projection="polar")
    if horizon:
        plt.plot(np.linspace(0, 2 * np.pi, n), np.ones(n) * 90, "k--")

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
            match theta:
                case "H":
                    theta = 0
                case "V":
                    theta = 90
                case "h":
                    theta = -az
                case "v":
                    theta = 90 - az
                case _:
                    theta = float(theta)

        except ValueError:
            raise ValueError(f"Badly formed line {i} in input")

        modcam.Camera(f, lt, w, h, n=n).rotate(alt, az, theta).plot(ax)
    plt.show()
