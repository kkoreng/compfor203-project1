#!/bin/bash
#SBATCH --job-name=compfor203-p1
#SBATCH --account=compfor203f26s001_class
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:10:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

set -e

cd "$SLURM_SUBMIT_DIR"

module load mamba/py3.12

export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1

eval "$(mamba shell hook --shell bash)"
mamba activate ~/mamba-envs/compfor203-project1-v2

python -m pytest -v
python main.py
