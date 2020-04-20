+++
title = "Off-Specular - Resonators"
weight = 30
+++

### Resonators in Off-Specular Simulations

Having defined a couple of `Layers` of different materials --let's consider Titanium and Lead, a resonator with `N` bilayers can be easily added to a `Sample` using a for loop:

```python
for i in range(N):
    sample.addLayer(l_Ti)
    sample.addLayer(l_Pt)
```

{{< galleryscg >}}
{{< figscg src="Figure.png" width="450px" caption="Intensity image">}}
{{< /galleryscg >}}

The script below show how to add a resonator of this kind in the context of an Offspecular Simulation, additionaly describing the roughness between the interfaces.

{{< highlightfile file="/static/files/python/simulation/ex05_BeamAndDetector/ResonatorOffSpecSetup.py" language="python" >}}
