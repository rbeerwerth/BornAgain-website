+++
title = "Cylinders and Prisms"
weight = 60
+++

### Cylinders and Prisms

Scattering from a mixture of cylinders and prisms without interference.

* The sample comprises a substrate on which are deposited, in equal proportion, cylinders and prisms.
* All particles are made of the same material.
* Each type of particle has the same orientation.
* The cylinders are $5$ nm high and $5$ nm in radius.
* Each prism is $5$ nm high with an equilateral triangular base, whose side length is equal to $10$ nm.
* There is no interference between the waves scattered by these particles. The distribution is therefore diluted.
* The incident neutron beam is characterized by a wavelength of $1$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.
* The simulation is performed using the Distorted Wave Born Approximation (due to the presence of a substrate).

{{< galleryscg >}}
{{< figscg src="CylindersAndPrisms_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="CylindersAndPrisms.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex01_BasicParticles/CylindersAndPrisms.py" language="python" >}}
