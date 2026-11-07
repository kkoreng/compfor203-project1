
import csv
import statistics
import time
from pathlib import Path

from calculations import sum_squares_loop, sum_squares_numpy


SIZES = [1000, 10000, 100000, 1000000]
TRIALS = 5


def measure_time(function, n):
    times = []

    for _ in range(TRIALS):
        start = time.perf_counter()
        function(n)
        end = time.perf_counter()

        times.append(end - start)

    return statistics.median(times)


def main():
    results = []

    for n in SIZES:
        loop_result = sum_squares_loop(n)
        numpy_result = sum_squares_numpy(n)

        if loop_result != numpy_result:
            raise ValueError("Results do not match")

        loop_time = measure_time(sum_squares_loop, n)
        numpy_time = measure_time(sum_squares_numpy, n)

        speedup = loop_time / numpy_time

        results.append([n, loop_time, numpy_time, speedup])

        print(f"n = {n}")
        print(f"  Loop:  {loop_time:.6f} seconds")
        print(f"  NumPy: {numpy_time:.6f} seconds")
        print(f"  Speedup: {speedup:.2f}x")
        print()

    output = Path("results")
    output.mkdir(exist_ok=True)

    with open(output / "benchmark.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "n",
            "loop_seconds",
            "numpy_seconds",
            "speedup"
        ])

        writer.writerows(results)


if __name__ == "__main__":
    main()
