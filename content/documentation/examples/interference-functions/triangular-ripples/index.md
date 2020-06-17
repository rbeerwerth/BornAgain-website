+++
title = "Triangular ripples in a lattice"
weight = 60
+++

### Triangular Ripples in a Rectangular Lattice

Scattering from elongated particles distributed along a two-dimensional rectangular lattice.

* Each particle has a triangular profile ("Ripple2" form factor) with a length of $100$ nm, a width of $20$ nm and a height of $4$ nm.
* They are placed along a rectangular lattice on top of a substrate.
* This lattice is characterized by a lattice length of $200$ nm in the direction of the long axis of the particles and of $50$ nm in the perpendicular direction.
* The lattice's base vectors coincide with the reference Cartesian frame.
* The wavelength is equal to $1.6$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.3 ^{\circ}$ and $\phi\_i = 0^{\circ}$.

View the example on [Cosine Ripples on a Rectangular Lattice]({{% ref-example "interference-functions/cosine-ripples-at-rect-lattice" %}}) for comparison.

{{< galleryscg >}}
{{< figscg src="Figure.png" width="4500px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex03_InterferenceFunctions/TriangularRipple.py" language="python" >}}
