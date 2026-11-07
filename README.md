# COMPFOR 203 - Project 1

## Overview

This project compares the execution time of a Python loop and NumPy vectorization for calculating the sum of squares.

The program runs on the Great Lakes HPC cluster using SLURM.

## Environment

Python 3.12, NumPy, and pytest are managed using Mamba and `environment.yml`.

## How to Run

Create the environment:

```bash
mamba env create -f environment.yml
mamba activate compfor203-project1
```

Run tests:

```bash
python -m pytest
```

Run the benchmark:

```bash
python main.py
```

On Great Lakes, after setting up the Mamba environment specified in `run_job.sh`:

```bash
sbatch run_job.sh
```

## Testing

- 13 pytest tests passed on Great Lakes.
- GitHub Actions is configured to run tests on push and pull requests.

## Results

The benchmark results are saved in `results/benchmark.csv`.

NumPy was faster than the Python loop for all tested input sizes.

**Great Lakes SLURM Job ID:** 65599332