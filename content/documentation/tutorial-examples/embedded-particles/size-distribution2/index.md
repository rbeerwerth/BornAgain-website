+++
title = "Two types of cylinders with size distribution"
weight = 40
+++

### Two types of cylinders with size distribution

Scattering of a polydisperse distribution of two types of cylinders.

* The simulation is performed using the Born approximation, i.e. there is no "substrate" layer.
* The sample is made of polydisperse cylinders of two different sizes: $R\_1 = H\_1$ and $R\_2 = H\_2$, where $R\_i$ and $H\_i$ are the radius and width of cylinder of type $i$.
* There are 95% of cylinders of type $1$ and 5% of cylinders of type $2$.
* The polydispersity affects the radii of the cylinders, following a normal distribution. For the small cylinders, their characteristic sizes vary around $R\_1 = 5$ nm with a standard deviation $\sigma\_1 = 0.2 R\_1$. For type 2, the average value $R\_2$ is $10$ nm and $\sigma\_2 = 0.02 R\_2$.
* There is also no interference between the scattered beams.
* The incident beam is characterized by a wavelength of $1$ $\unicode{x212B}$.
* The incident angles $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.

{{< galleryscg >}}
{{< figscg src="TwoTypesOfCylindersWithSizeDistribution_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="TwoTypesOfCylindersWithSizeDistribution.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex01_BasicParticles/TwoTypesOfCylindersWithSizeDistribution.py" language="python" >}}
