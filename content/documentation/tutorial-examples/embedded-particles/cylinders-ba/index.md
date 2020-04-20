+++
title = "Cylinders in Born Approximation"
weight = 10
+++

### Cylinders in Born Approximation

Scattering from a monodisperse distribution of cylinders using the Born approximation.

* The cylinders are all identical with radii and heights equal to $5$ nanometers.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are equal to $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.
* There is no substrate (particles are embedded in the air layer), hence no refraction, hence no distorted waves, hence DWBA boils down to regular Born approximation.
* Scattering is not affected by inter-particle correlations (dilute-particles approximation).

{{< galleryscg >}}
{{< figscg src="CylindersInBA_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="CylindersInBA.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex01_BasicParticles/CylindersInBA.py" language="python" >}}
