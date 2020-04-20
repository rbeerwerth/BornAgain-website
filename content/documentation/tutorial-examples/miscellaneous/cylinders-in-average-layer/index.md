+++
title = "Cylinders in Averaged Layer"
weight = 55
+++

## Cylinders in Averaged Layer

Supposing a `Simulation` has been defined in which some layers contain embedded particles of different materials; to regard those layers as composed by a single material, the `setUseAvgMaterials` method is used:

```
simulation.getOptions().setUseAvgMaterials(True)
```

{{< figscg src="Figure.png" width="500px" class="center" caption="The figure shows the intensity map produced by the script below." >}}

The script below shows how to average materials when simulating scattering from a square lattice of cylinders inside a finite layer.

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/CylindersInAverageLayer.py" language="python" >}}
