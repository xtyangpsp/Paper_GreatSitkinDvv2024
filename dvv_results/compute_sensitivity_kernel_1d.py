import numpy as np
import matplotlib.pyplot as plt
import sys
from srfpython.depthdisp.depthmodels import depthmodel_from_arrays,depthmodel_from_mod96
from srfpython.sensitivitykernels.sker17 import sker17_1
from srfpython.depthdisp.dispcurves import freqspace
from srfpython.standalone.display import logtick
from srfpython.Herrmann.Herrmann import HerrmannCaller, Curve

import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rc('font',family='Helvetica')
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=sys.maxsize)

"""
python script to compute depth sensitivity kernels
To run this script:
1. Follow the instruction on github for srfpython: https://github.com/obsmax/srfpython, to create the python environment.
2. Run this script: python compute_sensitivity_kernel_1d.py.

"""


# ================== build a 1d velocity model
ztop = np.arange(0., 6., 0.1)  # top layer array, sorted, in km, 1st at 0.0
vs = np.linspace(0.5, 3, len(ztop))  # Vs in each layer from top to half space, km/s
vp = 1.73 * vs   # Vp in each layer, km/s
rh = 2.3 * np.ones_like(vs)  # Density in each layer g/cm3
figdir='Figures'
# ================== compute sensitivity kernels for one wave type (RC0)
norm = True      # !!! recommended for non uniform layer model (try irregular ztop to see the difference) !!!
generator = sker17_1(ztop, vp, vs, rh,
    Waves=["R"],         # R=rayleigh
    Types=["C"],         # C=phase velocity
    Modes=[0],           # 0=fundamental mode
    Freqs=[[0.4, 1, 2,3]],  # frequencies at which to compute 1d kernels, in Hz
    norm=norm)

#depth model object
dmref=depthmodel_from_arrays(ztop, vp, vs, rh)
dmref.write96('GS_model.mod96')

# only one item here
wave, type_, mode, freqs, DLOGVADZ, DLOGVADLOGVS, DLOGVADLOGPR, DLOGVADLOGRH = \
    next(generator)

# ================== display
plt.figure()
# depth model
ax1 = plt.subplot(121)
dm = depthmodel_from_arrays(ztop, vp, vs, rh)
dm.show(ax1)
ax1.grid(True)
ax1.set_ylabel('Depth (km)',fontsize=12)
ax1.set_xlabel('Model parameters',fontsize=12)

plt.legend(fontsize=12)

# kernels
if norm:
    title = r'$ \frac{H}{H_i} \, \frac{d lnV_{{%s%s%d}}}{d lnVs} $' % (wave, type_, mode)
else:
    title = r'$ \frac{d lnV_{{%s%s%d}}}{d lnVs} $' % (wave, type_, mode)

ax2 = plt.subplot(122, sharey=ax1, title=title, xlabel="sensitivity")
for i in range(len(freqs)):
    ax2.plot(DLOGVADLOGVS[:, i], ztop, label="%.2fHz" % (freqs[i]))

#ax2.plot(DLOGVADLOGVS[:, 0], ztop, label="%s%s%d@%.2fHz" % (wave, type_, mode, freqs[0]))
#ax2.plot(DLOGVADLOGVS[:, 1], ztop, label="%s%s%d@%.2fHz" % (wave, type_, mode, freqs[1]))
ax2.set_ylabel('Depth (km)',fontsize=12)
ax2.set_xlabel('Normalized sensitivity',fontsize=12)
ax2.grid(True,ls='--',lw=0.5)
ax2.set_title("%s%s%d" % (wave, type_, mode))
plt.legend(fontsize=12)
# plt.ion()
plt.tight_layout()
plt.savefig(figdir+"/Sensitivity_%s%s%d"%(wave, type_, mode)+'.pdf',format = 'pdf', dpi=300 )
plt.show()
# input('pause')



