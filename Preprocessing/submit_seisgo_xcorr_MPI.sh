#!/bin/bash
#SBATCH -J xc  #job name to remember
#SBATCH -n 48  #number of CPU cores you request for the job
#SBATCH -N 3   #number of computing nodes, jobs could run across nodes,
               #but not recommend if not have to.
#SBATCH -A xtyang  #queue to submit the job
#SBATCH --mem-per-cpu 7200  #requested memory per CPU
#SBATCH -t 7-0:00   #requested time day-hour:minute
#SBATCH -o /home/ckupres/volcanodvv/%x.out  #path and name to save the output file
#SBATCH -e /home/ckupres/volcanodvv/%x.err  #path to save the error file
#module --force purge

module load rcac
module use /depot/xtyang/etc/modules
module load conda-env/seisgo-py3.7.6

mpirun -n $SLURM_NTASKS python ck_seisgo_xcorr_MPI.py
