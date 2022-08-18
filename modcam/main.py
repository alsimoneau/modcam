#!/usr/bin/env python3

import click
import matplotlib.pyplot as plt
import modcam
import numpy as np
from matplotlib.widgets import Slider


def parse_line(line):
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
    return f, lt, w, h, alt, az, theta


@click.command()
@click.argument("filename", type=click.File("r"))
@click.option(
    "-n",
    default=1000,
    show_default=True,
    help="Computation resolution.",
)
@click.option("-h", "--horizon", is_flag=True, help="Draws the horizon.")
@click.option("-s", "--slider", is_flag=True, help="Adds a radius slider.")
@click.option(
    "-f",
    "--opacity",
    default=0.0,
    show_default=True,
    help="Fill area opacity.",
)
def main(filename, n, horizon, opacity, slider):
    plot(filename, n, horizon, opacity, slider)


def plot(filename, n=1000, horizon=False, opacity=0.0, slider=False):
    if type(filename) == str:
        with open(filename) as f:
            filename = f.readlines()

    fig = plt.figure()
    ax = fig.add_subplot(projection="polar")
    if horizon:
        ax.plot(np.linspace(0, 2 * np.pi, n), np.ones(n) * 90, "k--")

    for i, line in enumerate(filename):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue

        f, lt, w, h, alt, az, theta = parse_line(line)

        (
            modcam.Camera(f, lt, w, h, n=n)
            .rotate(alt, az, theta)
            .plot(ax, fill=opacity)
        )

    if slider:
        rmin, rmax = plt.ylim()
        slider_ax = fig.add_axes([0.12, 0.1, 0.02, 0.8])
        rad = Slider(
            ax=slider_ax,
            label="radius",
            valmin=1,
            valmax=rmax,
            valinit=rmax,
            orientation="vertical",
        )

        def update(val):
            ax.set_ylim([0, rad.val])

        rad.on_changed(update)

    plt.show()
