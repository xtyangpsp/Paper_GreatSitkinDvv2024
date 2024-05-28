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

figdir='Figures'

dmref=depthmodel_from_mod96('./GS_model.mod96')
#### compute synthetic dispersion curves
# define the dipsersion curves to compute
f = freqspace(0.2, 5, 35, "log")
curves = [Curve(wave='R', type='U', mode=0, freqs=f),
          Curve(wave='R', type='C', mode=0, freqs=f),
          Curve(wave='L', type='U', mode=0, freqs=f),
          Curve(wave='L', type='C', mode=0, freqs=f)]

# compute dispersion curves and display
hc = HerrmannCaller(curves=curves)
curves_out = hc(
    ztop=dmref.vp.z,
    vp=dmref.vp.values, 
    vs=dmref.vs.values, 
    rh=dmref.rh.values, 
    keepnans=False)

fig = plt.figure()
ax = fig.add_subplot(111, xscale="log", yscale="log")
for curve in curves_out:
    curve.plot(ax, "+-", label="{}-{}-mode{}".format(curve.wave, curve.type, curve.mode))

logtick(ax, "xy")
ax.set_yticks(np.arange(0.4,1.1,0.1))
ax.set_ylabel('Velocity (km/s)',fontsize=12)
ax.set_xlabel('Period (s)',fontsize=12)
ax.set_title('Synthetic dispersion curves for fundamental \n mode Rayleigh (R) and Love (L) waves',fontsize=14)

plt.legend(fontsize=12)
plt.savefig(figdir+"/SyntheticDispersionCurves.pdf",format = 'pdf', dpi=300 )
plt.show()
