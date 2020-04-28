+++
title = "Size-distribution model: local monodisperse approximation"
weight = 100
+++

### Size-distribution model: local monodisperse approximation

Scattering from cylinders of two different sizes using the Local Monodisperse Approximation (LMA).

* The sample is made of cylinders deposited on a substrate.
* The cylinders are of two different sizes:
  * 80% of Type $1$: radius $R\_1 = 5$ nm, height $H\_1 = 5$ nm. The interference function is a radial paracrystal with a peak distance equal to $16.8$ nm and a damping length of $1$ $\mu$m.
  * 20% of Type $2$: radius $R\_2 = 8$ nm, height $H\_2 = 8$ nm. The interference function is also a radial paracrystal but with a peak distance of $22.8$ nm and a damping length equal to $1$ $\mu$m. 
* Each type of cylinders is associated with a "particle layout".
* The LMA is used since the sample is made of two domains containing particles of the same size and shape.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.

{{< galleryscg >}}
{{< figscg src="ApproximationLMA.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex03_InterferenceFunctions/ApproximationLMA.py" language="python" >}}
