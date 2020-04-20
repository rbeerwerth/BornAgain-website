+++
title = "Buried particles"
weight = 10
+++

### Buried particles

Scattering from a sample containing spherical embedded particles.

* From top to bottom, the sample is composed of the air layer, an intermediate material layer, and the substrate.
* The particles are spheres with radius $10.2$ nm.
* They are placed vertically in the middle of the intermediate layer. The depth to place the spheres is measured between the top of the layer and the bottom of the particles.
* There is no interference between the scattered waves. The horizontal distribution of the particles is diluted.
* The wavelength is equal to $1.5$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.15 ^{\circ}$ and $\phi\_i = 0^{\circ}$.

{{< galleryscg >}}
{{< figscg src="BuriedParticles_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="BuriedParticles.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex02_LayeredStructures/BuriedParticles.py" language="python" >}}
