+++
title = "1D radial paracrystal"
weight = 80
+++

### Interference 1D radial paracrystal

Scattering from a monodisperse distribution of cylinders positioned following a one-dimensional radial paracrystal.

* The sample is made of cylinders with radii and heights equal to $5$ nm, deposited on a substrate.
* The distribution of particles follows a radial paracrystal, characterized by a peak distance of $20$ nm and a damping length of $1$ $\mu$m.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.  

**Note:**

* A damping length is used to introduce finite size effects by applying a multiplicative coefficient equal to 
$exp \left(-\frac{peak\\_distance}{damping\\_length}\right)$ to the Fourier transform of the probability densities.

{{< galleryscg >}}
{{< figscg src="Interference1DRadialParaCrystal.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex03_InterferenceFunctions/Interference1DRadialParaCrystal.py" language="python" >}}
