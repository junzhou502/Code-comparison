import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from typing import List, Dict, Tuple
import warnings

def compare(
    dv1: np.ndarray,
    dv2: np.ndarray,
    label1: str,
    label2: str,
    domain: str,
    nlens: int = 10,
    nsrcs: int = 8,
    nbin : int = 20,
    dv1_include: list[bool] = [True, True, True, True],
    dv2_include: list[bool] = [True, True, True, True],
    show_include: list[bool] = [True, True, True, True],
):
    domain = domain.lower()
    dv1_include = np.array(dv1_include)
    dv2_include = np.array(dv2_include)
    show_include = np.array(show_include)
    Nprobe = 0
    dv_starts = []
    probes_latex = []
    if domain == 'real':
        Nprobe = 4
        dv_starts = [
            0,
            int(nsrcs*(nsrcs+1)/2*nbin),
            int(nsrcs*(nsrcs+1)*nbin),
            int((nsrcs*(nsrcs+1)+nlens*nsrcs)*nbin),
            int((nsrcs*(nsrcs+1)+nlens*nsrcs+nlens)*nbin),
        ]
        probes_latex = ['xi+', 'xi-', 'gammat', 'wtheta']
    else:
        Nprobe = 3
        dv_starts = [
            0,
            int(nsrcs*(nsrcs+1)/2*nbin),
            int((nsrcs*(nsrcs+1)/2+nlens*nsrcs)*nbin),
            int((nsrcs*(nsrcs+1)/2+nlens*nsrcs+nlens)*nbin),
        ]
        probes_latex = ['ss', 'gs', 'gg']
        
    #sanity check
    Length = 0
    for i in range(Nprobe):
        if dv1_include[i]:
             Length += dv_starts[i+1] - dv_starts[i]
    if Length != len(dv1):
        warning.warn(f'Length of dv1 is not as expected! the expectation is {Length}, while the real length is {len(dv1)}!')
        
    Length = 0
    for i in range(Nprobe):
        if dv2_include[i]:
             Length += dv_starts[i+1] - dv_starts[i]
    if Length != len(dv2):
        warning.warn(f'Length of dv2 is not as expected! the expectation is {Length}, while the real length is {len(dv2)}!')
        
    if (dv1_include&dv2_include&show_include).all()!=(show_include).all():
        warning.warn(f'we dont have the required probe to compare! check the bool array')

    
    #plot comparison
    dv1_l, dv2_l = 0, 0
    for i in range(Nprobe):
        delta = dv_starts[i+1] - dv_starts[i]
        ntomo = int(delta/nbin)
        if show_include[i]:
            dv1_seg = dv1[dv1_l:dv1_l+delta]
            dv2_seg = dv2[dv2_l:dv2_l+delta]

            for j in range(ntomo):
                l = int(j*nbin)
                r = int((j+1)*nbin)
                plt.plot(dv1_seg[l:r],label=label1)
                plt.plot(dv2_seg[l:r],label=label2)
                plt.legend()
                plt.title(probes_latex[i] +' '+str(j))
                plt.show()
            
        
        #correct the real index
        if dv1_include[i]:
            dv1_l += delta
        if dv2_include[i]:
            dv2_l += delta
        
    

import matplotlib

# GENERAL PLOT OPTIONS
# GENERAL PLOT OPTIONS
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
matplotlib.rcParams['xtick.bottom'] = True
matplotlib.rcParams['xtick.labelsize'] = 18
matplotlib.rcParams['xtick.top'] = False
matplotlib.rcParams['ytick.right'] = False
matplotlib.rcParams['ytick.labelsize'] = 18
matplotlib.rcParams['ytick.major.size'] = 6
matplotlib.rcParams['ytick.major.width'] = 1.2
matplotlib.rcParams['ytick.minor.size'] = 3
matplotlib.rcParams['ytick.minor.width'] = 0.8
matplotlib.rcParams['axes.edgecolor'] = 'black'
matplotlib.rcParams['axes.linewidth'] = '1.0'
matplotlib.rcParams['axes.labelsize'] = 18
matplotlib.rcParams['axes.titlesize'] = 24
matplotlib.rcParams['axes.grid'] = True
matplotlib.rcParams['grid.linewidth'] = '0.0'
matplotlib.rcParams['grid.alpha'] = '0.18'
matplotlib.rcParams['grid.color'] = 'lightgray'
matplotlib.rcParams['legend.labelspacing'] = 0.77
matplotlib.rcParams['legend.fontsize'] = 14
matplotlib.rcParams['legend.title_fontsize'] = 18
matplotlib.rcParams['savefig.bbox'] = 'tight'
matplotlib.rcParams['savefig.dpi'] = 300
                
                
                
        
        
    
    