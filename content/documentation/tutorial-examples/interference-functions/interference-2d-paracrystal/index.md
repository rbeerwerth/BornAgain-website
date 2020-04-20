+++
title = "2D Paracrystal"
weight = 70
+++

### Interference 2D Paracrystal

Scattering from monodisperse cylinders distributed along a two-dimensional square paracrystal.

* The particles are cylinders with constant radii and heights equal to $5$ nm.
* They are deposited on a substrate, following a two-dimensional square paracrystalline pattern.
* This 2D paracrystal is characterized by:
  * a lattice length of $20$ nm along both axes of the reference Cartesian frame,
  * a damping length equal to $0$,
  * "coherent' domains with a size of $20$ $\mu$m along the axes of the reference Cartesian frame.
* The incident beam is characterized by a wavelength of $1$ $\unicode{x212B}$ and angles $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.  

**Note:**

A damping length is used to introduce finite size effects by applying a multiplicative coefficient equal to $exp \left(-\frac{peak\\_distance}{damping\\_length}\right)$ to the Fourier transform of the probability densities. $damping\\_length$ is equal to $0$ by default and, in this case, no correction is applied.

{{< galleryscg >}}
{{< figscg src="Interference2DParaCrystal.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex03_InterferenceFunctions/Interference2DParaCrystal.py" language="python" >}}

