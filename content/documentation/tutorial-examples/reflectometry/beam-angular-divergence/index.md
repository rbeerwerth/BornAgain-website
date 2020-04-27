+++
title = "Beam Angular Spread"
weight = 30
+++

### Beam Angualr Spread in Specular Simulations

This example demonstrates beam angular spread effects in reflectivity computations.
It also offers a comparison with data generated using another well known code: GenX.
Further information about reflectometry simulations can be found in the
[Reflectometry Simulation Tutorial]({{% ref-tutorial "simulation-classes/reflectometry" %}}).

The observed reflectometry signal can be affected either by a spread in the beam wavelength or in the incident angle.

{{< galleryscg >}}
{{< figscg src="Figure.png" width="500px" caption="Intensity image">}}
{{< /galleryscg >}}

In this example, a Gaussian distribution is used to spread the incident angle, with a standard deviation of $\sigma_{\alpha} = 0.01^{\circ}$.

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/BeamAngularDivergence.py"  language="python" >}}

{{% filelink file="/static/files/python/simulation/ex06_Reflectometry/genx_angular_divergence.dat.gz" name="Reference data" %}}
