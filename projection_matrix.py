import numpy as np


def projection_matrix(fov, ratio, near, far):
    n = near
    f = far
    t = np.tan(fov / 2) * near
    b = -t
    r = t * ratio
    l = -r
    return np.array(
        [
            [(2 * n) / (r - l), 0, 0, 0],
            [0, (2 * n) / (t - b), (t + b) / (t - b), 0],
            [0, 0, -(f + n) / (f - n), -1],
            [0, 0, -2 * f * n / (f - n), 0],
        ]
    )


for row in projection_matrix(90, 1, 0.1, 100):
    print(",".join(f"{x:.5f}" for x in row))
