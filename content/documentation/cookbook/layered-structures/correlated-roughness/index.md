+++
title = "Correlated roughness"
weight = 20
+++

### Correlated roughness

Scattering from a multilayered sample with correlated roughness.

* The sample is composed of a substrate on which is sitting a stack of layers. These layers consist in a repetition of 5 times two different superimposed layers (from bottom to top):
  * layer A: $2.5$ nm thick with a real refractive index $n = 5 \cdot 10^{-6}$.
  * layer B: $5$ nm thick with a real refractive index $n = 10 \cdot 10^{-6}$.
* There is no added particle. 
* All layers present the same type of roughness on the top surface, which is characterized by:
  * a rms roughness of the interfaces $\sigma = 1$ nm,
  * a Hurst parameter $H$ equal to $0.3$,
  * a lateral correlation length $\xi$ of $5$ nm,
  * a cross correlation length $\xi\_{\perp}$ equal to $10^{-4}$ nm.
* The incident beam is characterized by a wavelength of $1$ $\unicode{x212B}$.
* The incident angles are $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.

**Note:**

The roughness profile is described by a normally-distributed random function. The roughness correlation function at the jth interface is expressed as: $$ < U\_j (x, y) U\_j (x', y')> = \sigma^2 e^{-\frac{\tau}{ξ}2H}, \tau=[(x-x')^2+(y-y')^2]^{\frac{1}{2}}$$ 

* $U\_j(x, y)$ is the height deviation of the jth interface at position $(x, y)$.
* $\sigma$ gives the rms roughness of the interface. The Hurst parameter $H$, comprised between $0$ and $1$ is connected to the fractal dimension $D=3-H$ of the interface. The smaller $H$ is, the more serrate the surface profile looks. If $H = 1$, the interface has a non fractal nature.
* The lateral correlation length ξ acts as a cut-off for the lateral length scale on which an interface begins to look smooth. If $\xi \gg \tau$ the surface looks smooth.
* The cross correlation length $\xi\_{\perp}$ is the vertical distance over which the correlation between layers is damped by a factor $1/e$. It is assumed to be the same for all interfaces. If $\xi\_{\perp} = 0$ there is no correlations between layers. If $\xi\_{\perp}$ is much larger than the layer thickness, the layers are perfectly correlated.

{{< galleryscg >}}
{{< figscg src="CorrelatedRoughness_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="CorrelatedRoughness.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex02_LayeredStructures/CorrelatedRoughness.py" language="python" >}}
