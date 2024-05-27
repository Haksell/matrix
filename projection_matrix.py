from src import Matrix
import math


def projection_matrix(fov, ratio, near, far):
    assert 0 < fov < math.pi
    assert ratio > 0
    assert 0 < near < far
    scale = 1 / math.tan(fov * 0.5)
    nf = 1 / (near - far)
    return Matrix(
        [
            [scale / ratio, 0, 0, 0],
            [0, scale, 0, 0],
            [0, 0, (far + near) * nf, -1],
            [0, 0, far * near * nf, 0],
        ]
    )


if __name__ == "__main__":
    for row in projection_matrix(math.radians(80), 1, 0.1, 100):
        print(",".join(f"{x:g}" for x in row))
