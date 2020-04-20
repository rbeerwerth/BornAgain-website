+++
title = "Particles crossing an interface"
weight = 10
+++

### Particles Crossing an Interface

In this example, very similar to the one on [Cylinders and Prisms]({{% ref-example "embedded-particles/cylinders-and-prisms" %}}), it is shown how to position particles in order to cross multilayer interfaces: the $z$ position of particles originally located within the air layer must be adjusted slightly downwards in order to cross the air-substrate interface.

The simulation kernel automatically detects particles crossing interfaces and adjusts the calculations accordingly, causing a drop on speed to complete each simulation.

The script below models a air-substrate bilayer in which cylindrical particles made of two materials are added to the air layer and their $z$ coordinate is shifted downwards in order to cross the air-substrate interface.


{{< galleryscg >}}
{{< figscg src="Figure.png" width="450px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex04_ComplexShapes/ParticlesCrossingInterface.py" language="python" >}}
