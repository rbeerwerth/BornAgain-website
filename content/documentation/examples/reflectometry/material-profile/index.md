+++
title = "Material profile"
weight = 30
+++

### Plotting the sample profile 

This short tutorial demonstrates how to visualize the Scattering Length Density (SLD) profile of a `Multilayer` sample.
For more details about preparing a sample and carrying on a reflectometry simulated experiment, read the
[reflectometry simulation tutorial]({{% ref-tutorial "simulation-classes/reflectometry" %}}).

{{< galleryscg >}}
{{< figscg src="MaterialProfile.png" width="500px" caption="This figure shows the sld profile of the sample built, i.e. the sld value ($y$ axis) as a function of depth ($x$ axis). $x = 0$ represents the surface of the sample, while the substrate is located at $x = -40 \, [{\rm nm}]$ in this example." >}}
{{< /galleryscg >}}

To obtain the figure above, one must run the script below, which is basically about [defining a sample with interfacial roughness]({{% ref-example "reflectometry/specular-simulation-with-roughness" %}}) and plotting right away its sld profile.

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/MaterialProfile.py"  language="python" >}}
