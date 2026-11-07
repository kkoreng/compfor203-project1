# COMPFOR 203 - Project 1

## Overview

This project compares the speed of a Python loop and NumPy when calculating the sum of squares.

## How to Run

Create the mamba environment using environment.yml

Run tests with python -m pytest

Run the program with python main.py

On Great Lakes, configure the mamba environment in run_job.sh

Submit the job using sbatch run_job.sh

## Results

NumPy was about 5–40 times faster than the Python loop, depending on the input size.

Results are saved in `results/benchmark.csv`.

SLURM Job ID: `65599332`

## AI Assistance

ChatGPT was used to assist with writing Python code, troubleshooting errors, and checking project progress.
