Steps to run the scripts (SeisGo package is required):

1. seisgo_download_MPI.py: download the continous waveforms with the option of using multiple processors.
2. seisgo_xcorr_MPI.py: compute the cross-correlations or autocorrelations with the option of using multiple processors.
3. seisgo_merger_MPI.py: merge short-term cross-correlations or autocorrelations across the whole observation time period.

There are three shell scripts that are used to submit these jobs on HPC clusters as batch jobs. Depending on the scheduler environment, some lines may need to be modified.


