+++
title = "Adding constant background"
weight = 20
+++

### Adding constant background

Given a `Simulation` instance, adding a constant background to it is as easy as:

```python
simulation.setBeamIntensity(1e6)
bg = ba.ConstantBackground(1e3)
simulation.setBackground(bg)
```

{{< galleryscg >}}
{{< figscg src="Figure.png" width="450px" caption="Intensity image">}}
{{< /galleryscg >}}

The script below shows how to add a constant background in the context of a GISAXS simulation of an air-substrate bilayer with cylindrical particles embedded. 

{{< highlightfile file="/static/files/python/simulation/ex05_BeamAndDetector/ConstantBackground.py" language="python" >}}
