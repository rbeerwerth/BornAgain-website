+++
title = "Boxes With Specular Peak"
weight = 55
+++

## Boxes With Specular Peak

Once a `Simulation` is defined, one can add the specular peak as follows:

```
simulation.getOptions().setIncludeSpecular(True)
```

{{< figscg src="Figure.png" width="500px" class="center" caption="The figure shows the intensity map produced by the script below." >}}

The script below shows how to include the specular peak when simulating a square lattice of boxes on a substrate.

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/BoxesWithSpecularPeak.py" language="python" >}}
