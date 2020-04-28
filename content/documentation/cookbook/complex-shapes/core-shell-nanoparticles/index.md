+++
title = "Core shell nanoparticles"
weight = 10
+++

### Core shell nanoparticles

Scattering from cuboidal core-shell particles.

* The sample is made of core-shell particles whose outer and inner shells are boxes with dimensions $L\_1 = W\_1 = 16$ nm, $H\_1 = 8$ nm and $L\_2 = W\_2 = 12$ nm, $H\_2 = 7$ nm, respectively, where $L\_i$, $W\_i$ and $H\_i$ are the length, width and height of box $i$.
* The smaller box is positioned so that the centres of the bottom faces of both particles coincide.
* The simulation is run using the Born approximation. There is no substrate and no interference between the different scattered beams.
* The planar distribution of the particles is diluted and random.
* The incident wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.  

{{< galleryscg >}}
{{< figscg src="CoreShellNanoparticles_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="CoreShellNanoparticles.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex04_ComplexShapes/CoreShellNanoparticles.py" language="python" >}}
