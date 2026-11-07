import numpy as np


def sum_squares_loop(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    total = 0

    for i in range(1, n + 1):
        total += i * i

    return total


def sum_squares_numpy(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    values = np.arange(1, n + 1, dtype=np.int64)
    result = np.sum(values * values)

    return int(result)
