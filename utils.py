import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from typing import List, Dict, Tuple
import warnings

def compare(
    dv1: np.ndarray,
    dv2: np.ndarray,
    cov: np.ndarray,
    mask: np.ndarray,
    label1: str,
    label2: str,
    domain: str,
    nlens: int,
    nsrcs: int,
    vmin: int,
    vmax: int,
    nbin : int = 20,
    dv1_include: list[bool] = [True, True, True, True],
    dv2_include: list[bool] = [True, True, True, True],
    show_include: list[bool] = [True, True, True, True],
    cal_chi2: bool = False,
    cal_full_chi2: bool = False,
    cal_all_probes_chi2: bool = False,
    if_plot: bool = False
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
        xlabel = r'$\theta(\mathrm{arcmin})$'
        logtmin = np.log(vmin)
        logtmax = np.log(vmax)
        logdt=(logtmax - logtmin)/nbin
        fac = (2./3.)
        xs = np.zeros(nbin)

        for i in range(nbin):
            thetamin = np.exp(logtmin + (i + 0.)*logdt)
            thetamax = np.exp(logtmin + (i + 1.)*logdt)
            xs[i] = fac * (thetamax**3 - thetamin**3) / (thetamax*thetamax    - thetamin*thetamin)

    else:
        Nprobe = 3
        dv_starts = [
            0,
            int(nsrcs*(nsrcs+1)/2*nbin),
            int((nsrcs*(nsrcs+1)/2+nlens*nsrcs)*nbin),
            int((nsrcs*(nsrcs+1)/2+nlens*nsrcs+nlens)*nbin),
        ]
        probes_latex = ['ss', 'gs', 'gg']
        xlabel = r'$\ell$'
        logdl = (np.log(vmax) - np.log(vmin))/nbin
        xs = np.zeros(int(nbin))
        for i in range(int(nbin)):
            xs[i] = np.exp(np.log(vmin) + (i + 0.5)*logdl)
        
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

    if cal_all_probes_chi2 and Nprobe!=int(np.sum(dv1_include&dv2_include)):
        raise ValueError("you have to pass into all probes data vector before \n \
            you calcualate the their chi2.")
    
    #calculate the chi2
        #plot comparison
    if cal_chi2:
        dv1_l, dv2_l = 0, 0
        for i in range(Nprobe):
            delta = dv_starts[i+1] - dv_starts[i]
            ntomo = int(delta/nbin)
            if show_include[i]:
                dv1_seg = dv1[dv1_l:dv1_l+delta]
                dv2_seg = dv2[dv2_l:dv2_l+delta]
                    
                cov_seg = cov[dv_starts[i]:dv_starts[i+1],:][:,dv_starts[i]:dv_starts[i+1]]
                mask_seg = mask[dv_starts[i]:dv_starts[i+1]]
                if cal_full_chi2:
                    chi2 = (dv1_seg-dv2_seg)@np.linalg.pinv(cov_seg)@(dv1_seg-dv2_seg)
                    print(f'{probes_latex[i]} full chi2 is {chi2:.3f}')
                dv1_seg_masked = dv1_seg[mask_seg]
                dv2_seg_masked = dv2_seg[mask_seg]
                cov_seg_masked = cov_seg[mask_seg,:][:,mask_seg]
                chi2 = (dv1_seg_masked - dv2_seg_masked)@np.linalg.pinv(cov_seg_masked)@(dv1_seg_masked - dv2_seg_masked)
                print(f'{probes_latex[i]} DES-masked chi2 is {chi2:.3f}')
                
            #correct the real index
            if dv1_include[i]:
                dv1_l += delta
            if dv2_include[i]:
                dv2_l += delta
    
    #plot comparison
    if if_plot:
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
                    plt.plot(xs, dv1_seg[l:r],label=label1)
                    plt.plot(xs, dv2_seg[l:r],label=label2)
                    plt.xlabel(xlabel)
                    plt.xscale('log')
                    plt.legend()
                    plt.title(probes_latex[i] +' '+str(j))
                    plt.show()
                            
            #correct the real index
            if dv1_include[i]:
                dv1_l += delta
            if dv2_include[i]:
                dv2_l += delta
                
    if cal_all_probes_chi2:
        masked_dv1 = dv1[mask]
        masked_dv2 = dv2[mask]
        invcov_masked = np.linalg.pinv(cov[mask,:][:,mask])
        chi2 = (masked_dv1 - masked_dv2)@invcov_masked@(masked_dv1 - masked_dv2)
        
        print(f'3x2pt DES-masked chi2 is {chi2:.3f}')
            
    

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
                
                
                
        
        
    
    