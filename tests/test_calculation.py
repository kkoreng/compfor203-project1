import pytest

from calculations import sum_squares_loop, sum_squares_numpy


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (3, 14),
    (5, 55),
    (10, 385),
])
def test_known_answers(n, expected):
    assert sum_squares_loop(n) == expected
    assert sum_squares_numpy(n) == expected


@pytest.mark.parametrize("n", [0, 1, 10, 100, 1000])
def test_same_results(n):
    assert sum_squares_loop(n) == sum_squares_numpy(n)


@pytest.mark.parametrize("n", [-1, -5, -100])
def test_negative_input(n):
    with pytest.raises(ValueError):
        sum_squares_loop(n)

    with pytest.raises(ValueError):
        sum_squares_numpy(n)
