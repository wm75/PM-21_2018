"""Estimate pi using a Monte Carlo Method

Simulates rain drops falling onto a square with an inscribed circle drawn in
the sand. The proportion of raindrops that fall into the circle as compared to
just the square approximates pi/4.
"""


import random
import math


drops_in_circle_segment = 0
drops_in_square = 0

while True:
    drops_in_square += 1
    drop_distance_from_origin = math.hypot(random.random(), random.random())
    if drop_distance_from_origin < 1:
        drops_in_circle_segment += 1

    if drops_in_square % 10000 == 0:
        print(
            'pi-estimate after {0} raindrops: {1}'
            .format(drops_in_square, 4*drops_in_circle_segment/drops_in_square)
            )
        
