+++
title = "Cylinders with size distribution"
weight = 30
+++

### Cylinders with size distribution

Scattering from a polydisperse distribution of cylinders in Born Approximation.

* The average radii and heights of the cylinders are equal to $5$ nm.
* The radii of the cylinders vary according to a normal distribution with a standard deviation $\sigma$ equal to $0.2$ times the average radius.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are equal to $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.
* There is no substrate (particles embedded in air layer, DWBA boils down to BA).
* No interference effects from inter-particle correlations (dilute-particles approximation).

{{< galleryscg >}}
{{< figscg src="CylindersWithSizeDistribution_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="CylindersWithSizeDistribution.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex01_BasicParticles/CylindersWithSizeDistribution.py" language="python" >}}
