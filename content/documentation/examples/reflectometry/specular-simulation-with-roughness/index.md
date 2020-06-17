+++
title = "Simulation with a rough sample"
weight = 10
+++

### Specular simulation with a rough sample

This example demonstrates how to compute reflected signal from
a multilayered sample with surface roughness. All the experiment
layout is exactly the same as the one described in
[reflectometry tutorial]({{% ref-tutorial "simulation-classes/reflectometry" %}}),
but now all the layers (except the ambient media) have roughness on the top surface. The
roughness is characterized by root-mean-square deviation from the mean surface position
$\sigma = 1$ nm.

{{< galleryscg >}}
{{< figscg src="SpecularSimulationWithRoughnessSetup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="SpecularSimulationWithRoughness.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

When comparing the result of the simulation to the result obtained in the
[reflectometry tutorial]({{% ref-tutorial "simulation-classes/reflectometry" %}}),
one can notice up to two orders of magnitude attenuation of the reflected signal due to
the roughness of the sample.

{{< notice note >}}
Please note that other roughness characteristics (like Hurst parameter or lateral and cross correlation lengths)
previously described in [example on correlated roughness]({{% ref-example "layered-structures/correlated-roughness" %}})
do not affect the result of the simulation. The computation model takes into account only the
rms-deviation from the mean surface position.
{{< /notice >}}

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/SpecularSimulationWithRoughness.py"  language="python" >}}
