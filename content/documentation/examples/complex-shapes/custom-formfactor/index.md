+++
title = "Custom formfactor"
weight = 40
+++

### Custom formfactor

Scattering from a monodisperse distribution of particles, whose form factor is defined by the user.

* This example shows how users can simulate their own particle shape by implementing the analytical expression of its form factor.
* The particular shape used here is a polyhedron, whose planar cross section is a "plus" shape with a side length of $20$ nm and a height of $15$ nm.
* These particles are distributed on a substrate.
* There is no interference between the scattered waves.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.

{{< galleryscg >}}
{{< figscg src="CustomFormFactor_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="CustomFormFactor.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex04_ComplexShapes/CustomFormFactor.py" language="python" >}}
