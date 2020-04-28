+++
title = "Different roughness models"
weight = 15
+++

### Specular simulation with different roughness models

This example demonstrates how to apply different roughness models
in a specular reflectivity calculation. The considered sample is 
exactly the same as the one described in the
[reflectometry tutorial]({{% ref-tutorial "simulation-classes/reflectometry" %}}),
and the [basic roughness tutorial]({{% ref-example "reflectometry/specular-simulation-with-roughness" %}}).
Hewever, now the computation is performed twice with the standard $tanh$ interface profile
and the Névot-Croce roughness model that arises from a Gaussian distribution of the 
deviation from the mean-surface position.

{{< galleryscg >}}
{{< figscg src="RoughnessModel.png" width="650px" caption="Intensity image">}}
{{< /galleryscg >}}

In both cases, the root-mean-square deviation from the mean surface position is chosen 
to be $\sigma = 1$ nm.


{{< notice note >}}
Even though the same selection of the underlying roughness model can be done for 
GISAS computations, we recommend to always use the default ($tanh$) for those simulations.
{{< /notice >}}


{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/RoughnessModel.py"  language="python" >}}
