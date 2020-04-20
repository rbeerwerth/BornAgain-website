+++
title = "ToF - Resolution effects"
weight = 30
+++

### Resolution effects in TOF Reflectometry

In real experiments, the $q_z$ resolution is non infinite. To take this into account in TOF simulations,
one needs to define the spread in $q$ as $dq$, set up a distribution with a given number of samples, `n_samples`,
and define the desired sigma factor, `n_sig` (e.g. the range in standard deviations to take into account 
during the sample generation).

``` python
    qzs = np.linspace(0.01, 1.0, scan_size)  # qz-values
    dq = 0.03 * qzs
    n_sig = 2.0
    n_samples = 25

    distr = ba.RangedDistributionGaussian(n_samples, n_sig)

    scan = ba.QSpecScan(qzs)
    scan.setAbsoluteQResolution(distr, dq)

    simulation = ba.SpecularSimulation()
    simulation.setScan(scan)
```

In the snippet above, a Gaussian distribution has been used, but there are several distributions available to chose from:

 -  Gate: `RangedDistributionGate(n_samples, sigma_factor, min, max)`
 -  Lorentz: `RangedDistributionLorentz(n_samples, hwhm_factor, min, max)`
 -  Gaussian: `RangedDistributionGaussian(n_samples, sigma_factor, min, max)`
 -  LogNormal: `RangedDistributionLogNormal(n_samples, sigma_factor, min, max)`
 -  Cosine: `RangedDistributionCosine(n_samples, sigma_factor, min, max)`

{{< galleryscg >}}
  {{< figscg src="TimeOfFlightReflectometry.png" width="350px" caption="TOF simulation without resolution effects" >}}
  {{< figscg src="TOFRWithResolution.png" width="350px" caption="TOF simulation with $dq = 0.03\,q$" >}}
{{< /galleryscg >}}



{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/TOFRWithResolution.py"  language="python" >}}
