+++
title = "Cosine ripples in a lattice"
weight = 60
+++

### Cosine Ripples in a Rectangular Lattice

Scattering from elongated particles distributed along a two-dimensional rectangular lattice.

* Each particle has a sinusoidal profile ("Ripple1" form factor) with a length of $100$ nm, a width of $20$ nm and a height of $4$ nm.
* They are placed along a rectangular lattice on top of a substrate.
* This lattice is characterized by a lattice length of $200$ nm in the direction of the long axis of the particles and of $50$ nm in the perpendicular direction.
* The lattice's base vectors coincide with the reference Cartesian frame.
* The wavelength is equal to $1.6$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.3 ^{\circ}$ and $\phi\_i = 0^{\circ}$.

{{< galleryscg >}}
{{< figscg src="CosineRipplesAtRectLattice_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="CosineRipplesAtRectLattice.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex03_InterferenceFunctions/CosineRipplesAtRectLattice.py" language="python" >}}
