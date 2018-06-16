"""Estimate pi using a Monte Carlo Method

Simulates rain drops falling onto a square with an inscribed circle drawn in
the sand. The proportion of raindrops that fall into the circle as compared to
just the square approximates pi/4.

Different implementations illustrate the advantages and disadvantages of
using numpy.
"""


import random
import math

import numpy as np


def std_pi(drops):
    drops_in_circle_segment = 0

    # simulate *drops* rain drops inside a square of a unit area and
    # count how many of them fall inside an inscribed circle segment
    for i in range(drops):
        drop_distance_from_origin = math.hypot(
            random.random(), random.random()
            )
        if drop_distance_from_origin < 1:
            drops_in_circle_segment += 1
    # ratio of drops in circle segment to total drops is ~ pi/4
    return 4*drops_in_circle_segment/drops


def std_pi_compact(drops):
    # same as std_pi, but expressed in most compact form
    return 4 * sum(
        1 for i in range(drops)
        if math.hypot(random.random(), random.random()) < 1
        ) / drops


def np_pi(drops):
    # Note how this numpy-dependent function eliminates the
    # for loop by handling arrays of the complete data at once
    
    # calculate *drops* x and y coordinates
    x = np.random.rand(drops)
    y = np.random.rand(drops)
    # caculate the distances from the origin for all drops
    d = np.hypot(x, y)
    drops_in_circle_segment = np.sum(d < 1)
    return 4*drops_in_circle_segment/drops


def np_pi_compact(drops):
    # same as np_pi, but expressed in most compact form
    return 4 * np.sum(
        np.hypot(np.random.rand(drops), np.random.rand(drops)) < 1
        ) / drops
