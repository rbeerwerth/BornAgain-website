+++
title = "Mesocrystal"
weight = 20
+++

### Mesocrystal

This examples deals with the modelling of a cylindrically shaped mesocrystal on a substrate.
With this scope, three lattice basis vectors are defined, using spherical particles as the base of a first crystal structure.
This base crystal structure is later combined with a cylinder form factor to form the mesocrystal. 

The basis vectors of the base crystal are $5 \, {\rm nm}$ each, the sperical particles have a radius of $2 \, {\rm nm}$ and the cylindrical form factor to shape the mesocrystal is $20 \, {\rm nm}$ in radius and $50 \, {\rm nm}$ in height.

{{< galleryscg >}}
{{< figscg src="Figure.png" width="450px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex04_ComplexShapes/MesoCrystal.py" language="python" >}}
