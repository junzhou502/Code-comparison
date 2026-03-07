
Notations of different modified version of COCOA, or different sets of systematics modeling used in this comparison

|Setup|Description|
|:---|:---|
|Setup0|bin_average-Limber-noRSD-takahashi-bin_average|
|Setup1|no_bin_average-Limber-noRSD-takahashi|
|Setup2|no_bin_average-NonLimber(gg only)-noRSD-takahashi|
|Setup3|no_bin_average-NonLimber(gg only)-RSD-takahashi|
|Setup4|no_bin_average-NonLimber(gg only)-RSD-takahashi **<br>**-IA_NLA(A=0.5, eta=0)|
|Setup5|no_bin_average-NonLimber(gg only)-RSD-takahashi **<br>**-IA_NLA(A=0.5, eta=0)-MagnificationBias|
|Setup6|no_bin_average-Limber-RSD-takahashi **<br>**-IA_NLA(A=0.5, eta=0)-MagnificationBias(s=0.44)|


$\chi^2 (\mathrm{masked}/\mathrm{full})$ between two pipelines under these setups

Fourier Space
|Probes|Setup0|Setup1|Setup2|Setup3|Setup4|Setup5|
|:---|:---|:---|:---|:---|:---|:---|
|$C_\ell^{ss}$|0.006/0.052|x|x|x|x|x|
|$C_\ell^{gs}$|0.021/0.063|x|x|x|x|x|
|$C_\ell^{gg}$|0.028/0.078|x|x|x|x|x|
|Total|0.087/0.198|x|x|x|x|x|

Configuration Space
|Probes|Setup0|Setup1|Setup2|Setup3|Setup4|
|:---|:---|:---|:---|:---|:---|
|$\xi^-$|0.33/4.42|0.093/0.570|--|--|0.094/0.553|
|$\xi^+$|0.22/14.66|0.040/0.780|--|--|0.040/0.763|
|$\gamma t$|1.76/96.63|0.007/0.055|--|0.007/0.055|0.007/0.051|
|$w(\theta)$|3.69/419.61|0.001/0.014|0.048/0.062|0.033/0.047|--|
|Total|5.90/--|0.91/--|1.08/--|1.053/--|1.105/--|

Suspicious Tests
||$\xi^-$|$\xi^+$|$\gamma t$|$w(\theta)$|Total|
|:---|:---|:---|:---|:---|:---|
|Setup5|0.094/0.553|0.040/0.763|0.007/0.052|0.562/0.581|2.130|
|Setup6|0.094/0.553|0.040/0.763|0.007/0.052|0.006/0.023|0.957|

Setup5 and Setup6: Likely NonLimber has something wrong about the magnification bias.

Current Supported Systematics Model and Approximation
||COCOA-CosmoLike|(Firecrown?)-CCL|
|:---|:---|:---|
|NonLimber|only support galaxy clustering|support three probes|
|RSD|linear model|linear model|
|Intrinsic Alignment|NLA, TATT, LF|NLA(no eta)|
|Magnification Bias|Support|Support|
|Photo-z|Shift|Firecrown's Job|
||||
