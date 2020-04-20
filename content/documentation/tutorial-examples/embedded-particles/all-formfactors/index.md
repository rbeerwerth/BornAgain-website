+++
title = "All available form factors"
weight = 70
+++

### All available form factors

Scattering from all individual particle's shapes implemented in BornAgain. For each figure, one particular shape is used.

The dimensions of the object are chosen only in order to get a characteristic signature of the form factor in the same range of values for the output angles.

* The simulation is run using the Born approximation. There is no substrate and also no interference between the scattered waves.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are equal to $\alpha\_i = 0.2 ^{\circ}$ and $\phi\_i = 0^{\circ}$.
  
{{< galleryscg >}}
{{< figscg src="AllFormFactorsAvailable_setup.jpg" width="350px" caption="Real-space models">}}
{{< figscg src="AllFormFactorsAvailable.png" width="350px" caption="Intensity images">}}
{{< /galleryscg >}}
  
{{< highlightfile file="/static/files/python/simulation/ex01_BasicParticles/AllFormFactorsAvailable.py" language="python" >}}
