from classes import Matrix
import math


def projection_matrix(fov, ratio, near, far):
    assert 0 < fov < math.pi
    assert ratio > 0
    assert 0 < near < far
    n = near
    f = far
    t = math.tan(fov / 2) * near
    b = -t
    r = t * ratio
    l = -r
    return Matrix(
        [
            [(2 * n) / (r - l), 0, 0, 0],
            [0, (2 * n) / (t - b), (t + b) / (t - b), 0],
            [0, 0, -(f + n) / (f - n), -1],
            [0, 0, -2 * f * n / (f - n), 0],
        ]
    )


if __name__ == "__main__":
    """
    0.5625,0,0,0
    0,1,0,0
    0,0,-1.002,-1
    0,0,-0.2002,0
    """
    # python ../projection_matrix.py | tee proj && ./display
    for row in projection_matrix(math.radians(90), 16 / 9, 0.1, 100):
        print(",".join(f"{x:g}" for x in row))
