from math import pi
import numpy as np


def projection_matrix(fov, ratio, near, far):
    f = 1.0 / np.tan(fov / 2 * pi / 180)
    return np.array(
        [
            [f, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, -far / (far - near), -1],
            [0, 0, -(far * near) / (far - near), 0],
        ]
    )


for row in projection_matrix(90, 16 / 9, 0.1, 100):
    print(",".join(f"{x:.5f}" for x in row))

"""
.1, 0., 0., 0.
0., .1, 0., 0.
0., 0., 1., 0.
0., 0., 0., 1.
"""
