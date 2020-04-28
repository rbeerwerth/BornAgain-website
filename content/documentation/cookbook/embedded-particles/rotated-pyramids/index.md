+++
title = "Rotated Pyramids"
weight = 50
+++

### Rotated Pyramids

Scattering from a monodisperse distribution of rotated pyramids.

This example illustrates how the in-plane rotation of non-radially symmetric particles influences the scattering pattern.

* The sample is made of pyramids deposited on a substrate.
* Each pyramid is characterized by a squared-base side length of $10$ nm, a height of $5$ nm, and a base angle $\alpha$ equal to $54.73^{\circ}$.
* These particles are rotated in the $(x, y)$ plane by $45^{\circ}$.
* There is no interference between the scattered waves.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.

{{< galleryscg >}}
{{< figscg src="RotatedPyramids_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="RotatedPyramids.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex01_BasicParticles/RotatedPyramids.py" language="python" >}}
