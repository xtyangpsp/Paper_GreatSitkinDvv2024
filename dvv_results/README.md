The list of files in this folder:

* YangETAL_GreatSitkinFWANT_Vs2023.nc               -> Shear-wave velocity model from Yang et al. (2023)
* GreatSitkin_stations.csv                          -> CSV file containing station information
* data_greatsitkin                                  -> folder containing the dv/v results and the coda window test results.


* compute_lateral_sensitivity.py                    -> compute the lateral sensitivity of dv/v measurements using Fresnel zone and wavelengths.
* compute_sensitivity_kernel_1d.py                  -> compute depth sensitivity of dv/v measurements for Rayleigh and Love waves.
* compute_single_station_dvv_redo2024.ipynb         -> compute single station dv/v for the final analysis.
* compute_single_station_dvv_winlentests.ipynb      -> compute the dv/v with increasing coda window lengths. This is the notebook to test the influence of coda window on dv/v results.


* dvv_plotting_final.ipynb                          -> plot all dv/v related figures, including the figure overlaying on the shear-wave velocities.
* dvv_plotting_windowlength.ipynb                   -> plot coda window length test results.
* plot_synthetic_dispersioncurves.py                -> plot synthetic dispersion curves using the same model as in computing the depth sensitivities.
* GS_Map_Plots.ipynb                                -> plot map view figures, including geological settings and map view seismicity. 

REFERENCES:
* Yang, X., Roman, D. C., Haney, M., & Kupres, C. A. (2023). Double Reservoirs Imaged Below Great Sitkin Volcano, Alaska, Explain the Migration of Volcanic Seismicity. Geophysical Research Letters, 50(11). https://doi.org/10.1029/2022GL102438

