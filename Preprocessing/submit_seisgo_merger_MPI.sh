#!/bin/bash
#SBATCH -J merg       #job name to remember
#SBATCH -n 32	#number of CPU cores you request for the job
#SBATCH -N 1 	#number of computing nodes, jobs could run across nodes,
              #but not recommended if not have to.
#SBATCH -A xtyang  #queue to submit the job, our lab queue.
#SBATCH --mem-per-cpu 3600 	#requested memory per CPU
#SBATCH -t 3-0:00			#requested time day-hour:minute
#SBATCH -o /home/ckupres/volcanodvv/%x.out  #path and name to save the output file.
#SBATCH -e /home/ckupres/volcanodvv/%x.err 	#path to save the error file.

module purge			#clean up the modules
module load rcac		#reload rcac modules.
module use /depot/xtyang/etc/modules
module load conda-env/seisgo-py3.7.6

mpirun -n $SLURM_NTASKS python seisgo_merger_MPI.py
 					#run line, change file name
