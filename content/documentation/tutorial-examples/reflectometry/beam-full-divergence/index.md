+++
title = "Beam Wavelength Spread"
weight = 30
+++

### Beam Wavelength Spread in Specular Simulations

This example demonstrates beam wavelength spread effects in reflectivity computations.
All simulation parameters (except for those related to beam spread itself)
coincide with those defined in
[reflectometry simulation tutorial]({{% ref-tutorial "simulation-classes/reflectometry" %}}).

In real specular experiments the observed reflectivity is always affected
by the beam spread in both wavelength and incident angle.

{{< galleryscg >}}
{{< figscg src="BeamDivergence.png" width="500px" caption="Intensity image">}}
{{< /galleryscg >}}

In this example the following parameters related to the spread of the beam were set to the simulation:

* Gaussian distributions both in wavelength and incident angle
* The mean value for beam wavelength $\lambda_0 = 1.54 \, \unicode{x212B}$
* Standard deviation in the wavelength $\sigma_{\lambda} = 0.01 \cdot \lambda_0$
* Standard deviation in the incident angle $\sigma_{\alpha} = 0.01^{\circ}$

As one can see from the python script, the definitions of beam parameter distributions
match ones described in [similar example for GISAS simulations]({{% ref-example "beam-and-detector/beam-divergence" %}}).
However, in the case of the incident angle one should always use a distribution with zero mean,
since the actual mean value is substituted by `SpecularSimulation` in dependence on the
defined inclination angle range.
If the distribution of the incident angle has non-zero mean value, an exception
is thrown:

```python
terminate called after throwing an instance of 'std::runtime_error'
  what():  Error in SpecularSimulation: parameter distribution of beam inclination angle should have zero mean.
```

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/BeamFullDivergence.py"  language="python" >}}
