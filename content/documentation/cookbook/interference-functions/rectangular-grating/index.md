+++
title = "Rectangular grating"
weight = 85
+++

### Interference - Rectangular Grating

This example demonstrates how to perform a simulation of a grating using very long boxes and a 1D lattice. To get rid of oscillation arising from large-particle form factors, Monte-carlo integration is used.

[Interference of a 1D lattice]({{% ref-example "interference-functions/interference-1d-lattice" %}}) may provide useful background for this example.

{{< galleryscg >}}
{{< figscg src="Figure.png" width="4500px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex03_InterferenceFunctions/RectangularGrating.py" language="python" >}}
