+++
title = "Off-Specular"
weight = 30
+++

### Off-Specular

Off-specular scattering from a monodisperse distribution of long boxes.

* The sample is made of very long boxes with length equal to $1000$ nm, width $20$ nm and height $10$ nm.
* The particles are distributed along a one-dimensional lattice with a lattice spacing of $100$ nm in the $x$-direction.
* The particles are rotated around the $z$-axis by $90^{\circ}$ so that their "infinite" dimension is parallel to the $y$-direction.
* The incident wavelength is equal to $1$ $\unicode{x212B}$.
* The output intensity is the result of an average over $\phi\_i$ comprised between $-1^{\circ}$ and $1^{\circ}$ and of a scan of $\alpha\_i$ and $\alpha\_f$ between $0^{\circ}$ and $10^{\circ}$.

**Note:**

> The two-dimensional output intensity is plotted as a function of $\alpha\_i$ and $\alpha\_f$.

{{< galleryscg >}}
{{< figscg src="OffSpecularSimulation_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="OffSpecularSimulation.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex05_BeamAndDetector/OffSpecularSimulation.py" language="python" >}}
