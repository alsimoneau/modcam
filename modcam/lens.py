#!/usr/bin/env python3

import numpy as np

lens_types = dict(
    rectilinear=lambda x, f: np.arctan2(x, f),
    stereographic=lambda x, f: 2 * np.arctan2(x, 2 * f),
    equidistant=lambda x, f: x / f,
    equisolid=lambda x, f: 2 * np.arcsin(np.where(x / 2 >= f, 1, x / 2 / f)),
    orthographic=lambda x, f: np.arcsin(np.where(x >= f, 1, x / f)),
)

aliases = (
    ("standard", "rectilinear"),
    ("fisheye", "quidistant"),
)
for alias, base in aliases:
    lens_types[alias] = lens_types[base]
