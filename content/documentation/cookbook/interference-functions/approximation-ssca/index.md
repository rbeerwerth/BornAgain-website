+++
title = "Size-distribution model: size-spacing coupling approximation"
weight = 110
+++

### Size-distribution model: size-spacing coupling approximation

Scattering from cylinders of two different sizes using the Size-Spacing Coupling Approximation.

* The sample is made of cylinders deposited on a substrate.
* The distribution of particles is made of:
  * 80% of cylinders with radii and heights equal to $5$ nm
  * 20% of cylinders with radii and heights equal to $8$ nm.
* The interference function is Radial Paracrystal with a peak distance of $18$ nm and a damping length of $1$ $\mu$m.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.
* The Size-Spacing Coupling Approximation is implemented using the function setApproximation. By default the Decoupling Approximation is used (see [Size-distribution model: Decoupling Approximation]({{% ref-example "interference-functions/approximation-da" %}})).
* For this size-distribution model, an additional dimensionless parameter, the coupling parameter `Kappa`, has to be specified (see line 33). It defines how the distance between particles is linked with their sizes.

{{< galleryscg >}}
{{< figscg src="ApproximationSSCA.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile 
file="/static/files/python/simulation/ex03_InterferenceFunctions/ApproximationSSCA.py" language="python" >}}
