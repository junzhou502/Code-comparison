
This repo is to record and demonstrate the progress and results of code comparison between COCOA-CosmoLike and CCL. Firecrown is not present here because we don't have plan yet to compare the sampling. All number present here is repoducible. To reproduce the reuslts, you should be able to run the COCOA and CCL. However some modifications are inevitable hard-coded, you may need read the commit history to precisely recover these number. We mainly modify the COCOA-CosmoLike and only do this to CCL when necessary as we encounter bugs or extremely unaccessible speed. 


### Notations of Test Set Up

We employ these systematics models in COCOA-CosmoLike to compute data vectors, and compare with the one computed by CCL with corresponding modeling. **Bin_average** refers to average correlation function over the angular range $[\theta_\mathrm{min}, \theta_\mathrm{max}]$, which was employed in DES. 

|Setup|Description|
|:---|:---|
|Setup0|bin_average-Limber-noRSD-takahashi|
|Setup1|no_bin_average-Limber-noRSD-takahashi|
|Setup2|no_bin_average-NonLimber(gg only)-noRSD-takahashi|
|Setup3|no_bin_average-NonLimber(gg only)-RSD-takahashi|
|Setup4|no_bin_average-NonLimber(gg only)-RSD-takahashi **<br>**-IA_NLA(A=0.5, eta=0)|
|Setup5|no_bin_average-NonLimber(gg only)-RSD-takahashi **<br>**-IA_NLA(A=0.5, eta=0)-MagnificationBias(s=0.44)|
|Setup6|no_bin_average-Limber-RSD-takahashi **<br>**-IA_NLA(A=0.5, eta=0)-MagnificationBias(s=0.44)|


## $\chi^2 (\mathrm{masked}/\mathrm{full})$ between two pipelines under these setups

**Note**: since comparison in configuration space is more strigent, we mainly show results in the configuration space here.

### Fourier Space
|Probes|Setup0|Setup1|Setup2|Setup3|Setup4|Setup5|
|:---|:---|:---|:---|:---|:---|:---|
|$C_\ell^{ss}$|0.006/0.052|x|x|x|x|x|
|$C_\ell^{gs}$|0.021/0.063|x|x|x|x|x|
|$C_\ell^{gg}$|0.028/0.078|x|x|x|x|x|
|Total|0.087/0.198|x|x|x|x|x|

**Note**: We compute $\gamma t$ and $w(\theta)$ with full-sky approach while using flat-sky for $\xi^+$ and $\xi^-$ in CCL unless otherwise specified. In cosmolike, all correlation functions are done with the full-sky approach.

### Configuration Space

|Probes|Setup0|Setup1|Setup2|Setup3|Setup4|
|:---|:---|:---|:---|:---|:---|
|$\xi$      |0.73/20.46    |0.374/3.642  |0.374/3.642  |0.374/3.642  |0.374/3.522  |
|$\gamma t$ |1.76/96.63    |0.007/0.055  |0.007/0.055  |0.007/0.055  |0.007/0.051  |
|$w(\theta)$|3.69/419.61   |0.001/0.014  |0.048/0.062  |0.033/0.047  |0.033/0.047  |
|Total      |5.90/x        |0.910/x      |1.08/x       |1.053/x      |1.105/x      |

### Conclusions or Unresolved Problems

1. **Matter power spectrum**: note that the power spectrum of COCOA and CCL is never aligned during our test, therefore we force CCL uses the one simulated from COCOA.

2. **Setup0 and Setup1**: Bin-average can raise great difference. People should decide which is more physical to use.

||$\xi^-$|$\xi^+$|$\gamma t$|$w(\theta)$|Total|
|:---|:---|:---|:---|:---|:---|
|Setup0|0.33/4.42|0.22/14.66|1.76/96.63|3.69/419.61|5.90/x|
|Setup1|0.093/0.570|0.040/0.780|0.007/0.055|0.006/0.023|0.957|

3. **Setup5,Setup5_1,Setup5_2,**: We employ 'Bessel' (a fast full-sky algorithm) approach for galaxy clustering and lensing in CCL as the **Setup5_1**, and use Flat-sky approach for those in CCL as the **Setup5_2**. It demonstrates that a frute-force full-sky is necessary for galaxy-clustering, and it is also good to use a frute-force for galaxy-lensing. The speed is not a problem if the Legendre function is cached.

||$\xi^-$|$\xi^+$|$\gamma t$|$w(\theta)$|Total|
|:---|:---|:---|:---|:---|:---|
|Setup5|0.094/0.553|0.040/0.763|0.007/0.052|0.562/0.581|2.130|
|Setup5_1|0.094/0.553|0.040/0.763|0.136/0.207|1.100/1.616|2.228|
|Setup5_2|0.094/0.553|0.040/0.763|0.436/5.862|1.577/53.785|2.855|

4. **Setup5 and Setup6**: Likely their NonLimber has something wrong about the magnification bias.

||$\xi^-$|$\xi^+$|$\gamma t$|$w(\theta)$|Total|
|:---|:---|:---|:---|:---|:---|
|Setup5|0.094/0.553|0.040/0.763|0.007/0.052|0.562/0.581|2.130|
|Setup6|0.094/0.553|0.040/0.763|0.007/0.052|0.006/0.023|0.957|


### Current Supported Systematics Models and Approximations (to my knowledge*)

* please reach out if you have additional knowledge and this is incorrect

||COCOA-CosmoLike|Firecrown-CCL|
|:---|:---|:---|
|NonLimber|only support galaxy clustering|support three probes|
|RSD|linear model|linear model|
|Intrinsic Alignment|NLA, TATT, LF|NLA(no eta)|
|Magnification Bias|Support|Support|
|Photo-z|Shift|(Firecrown)Shift and Stretch|
|Multiplicative Bias|Support|(Firecrown)Support|
|Galaxy Bias|Linear Bias, NonLinear Bias|Linear Bias|
|Point Mass Parameter|Support|x|
