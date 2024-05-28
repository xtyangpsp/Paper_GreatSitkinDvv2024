#compute lateral sensitivity

import numpy as np
import matplotlib.pyplot as plt

def fresnel_zone(v, t0, T):
    """
    Defined following Donaldson et al., 2019. For zero-offset data, the Fresnel zone radius is given by:

    R=0.5*v*sqrt(t0*T), where R is the radius of the Fresnel zone, v is the group velocity, 
    t0 is the two-way travel time time window of the data, and T is the period of the signal.

    For autocorrelation data, the two-way travel time window is the arrival time of the scattered wave, after the direct arrival. 
    This can be estimated from FTAN of the autocorrelation function. 
    
    """

    R=0.5*v*np.sqrt(t0*T)

    return R

#
figdir='Figures'
freqlst = [0.4, 1, 2, 3]

velocity_RU=[0.46, 0.45, 0.45, 0.46 ] #Rayleigh group velocity for each frequency, estimated from the synthetic dispersion curves.
velocity_LU=[0.52,0.51,0.5,0.49] #Love group velocity for each frequency, estimated from the synthetic dispersion curves.

velocity_RC=[0.52,0.51,0.5,0.49] #Rayleigh phase velocity for each frequency, estimated from the synthetic dispersion curves.
velocity_LC=[0.65, 0.51, 0.48, 0.47 ] #Love phase velocity for each frequency, estimated from the synthetic dispersion curves.

t0_min = 2
t0_max = 8 #range estimate based on 1-2 Hz AV.GSSP cross-component correlations. This is the first peak of the coda window.

R_min_RU=[] #list to store the minimum Fresnel zone radius for each frequency
R_max_RU=[] #list to store the maximum Fresnel zone radius for each frequency
R_min_LU=[] #list to store the minimum Love Fresnel zone radius for each frequency
R_max_LU=[] #list to store the maximum Love Fresnel zone radius for each frequency

R_min_RC=[] #list to store the minimum Fresnel zone radius for each frequency computed using phase velocity
R_max_RC=[] #list to store the maximum Fresnel zone radius for each frequency computed using phase velocity
R_min_LC=[] #list to store the minimum Love Fresnel zone radius for each frequency computed using phase velocity
R_max_LC=[] #list to store the maximum Love Fresnel zone radius for each frequency computed using phase velocity

for i in range(len(freqlst)):
    T=1.0/freqlst[i]
    R_min_RU.append(fresnel_zone(velocity_RU[i], t0_min, T))
    R_max_RU.append(fresnel_zone(velocity_RU[i], t0_max, T))

    R_min_LU.append(fresnel_zone(velocity_LU[i], t0_min, T))
    R_max_LU.append(fresnel_zone(velocity_LU[i], t0_max, T))

    #use phase velocity
    R_min_RC.append(fresnel_zone(velocity_RC[i], t0_min, T))
    R_max_RC.append(fresnel_zone(velocity_RC[i], t0_max, T))
    R_min_LC.append(fresnel_zone(velocity_LC[i], t0_min, T))
    R_max_LC.append(fresnel_zone(velocity_LC[i], t0_max, T))

print('Rayleigh Fresnel zone radii:')
print(R_min_RU)
print(R_max_RU)
print(R_min_RC)
print(R_max_RC)

print('Love Fresnel zone radii:')
print(R_min_LU)
print(R_max_LU)
print(R_min_LC)
print(R_max_LC)

wavelength_RU=np.divide(velocity_RU,freqlst) #list to store the Rayleigh wavelength for each frequency
wavelength_LU=np.divide(velocity_LU,freqlst) #list to store the Love wavelength for each frequency
wavelength_RC=np.divide(velocity_RC,freqlst) #list to store the Rayleigh wavelength for each frequency
wavelength_LC=np.divide(velocity_LC,freqlst) #list to store the Love wavelength for each frequency

print('Rayleigh wavelength:')
print(wavelength_RU)
print('Love wavelength:')
print(wavelength_LU)

#plot the Fresnel zone radii
fig, ax = plt.subplots()
ax.plot(freqlst, R_min_RU, marker='o',c='tab:red', linestyle='None',markerfacecolor='None',label='R min (U)')
ax.plot(freqlst, R_max_RU, marker='s',c='tab:red', linestyle='None',markerfacecolor='None',label='R max (U)')
ax.plot(freqlst, R_min_RC, marker='^',c='tab:red', linestyle='None',markerfacecolor='None',label='R min (C)')
ax.plot(freqlst, R_max_RC, marker='d',c='tab:red', linestyle='None',markerfacecolor='None',label='R max (C)')

ax.plot(freqlst, R_min_LU, marker='o',c='tab:blue', linestyle='None',markerfacecolor='None',label='L min (U)')
ax.plot(freqlst, R_max_LU, marker='s',c='tab:blue', linestyle='None',markerfacecolor='None',label='L max (U)')
ax.plot(freqlst, R_min_LC, marker='^',c='tab:blue', linestyle='None',markerfacecolor='None',label='L min (C)')
ax.plot(freqlst, R_max_LC, marker='d',c='tab:blue', linestyle='None',markerfacecolor='None',label='L max (C)')

ax.plot(freqlst, wavelength_RU, c='tab:red', linestyle='None',markerfacecolor='None',label='$\lambda _R$ (U)',marker='+')
ax.plot(freqlst, wavelength_RC, c='tab:red', linestyle='None',markerfacecolor='None',label='$\lambda _R$ (C)',marker='*')
ax.plot(freqlst, wavelength_LU, c='tab:blue', linestyle='None',markerfacecolor='None',label='$\lambda _L$ (U)',marker='+')
ax.plot(freqlst, wavelength_LC, c='tab:blue', linestyle='None',markerfacecolor='None',label='$\lambda _L$ (C)',marker='*')

ax.grid(lw=0.5,ls=':')
ax.set_xlabel('Frequency (Hz)',fontsize=12)
ax.set_ylabel('Fresnel zone radius (km)',fontsize=12)
ax.set_yticks(np.arange(0.1, 1.8, 0.1))
ax.legend(ncol=3,loc='upper right',fontsize=10)
ax.set_title('Fresnel zone radii for Rayleigh (R) and Love (L) waves',fontsize=12)
plt.savefig(figdir+'/Fresnel_zone_radii.pdf',format='pdf',dpi=300,bbox_inches='tight')
plt.show()
