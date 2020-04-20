+++
title = "Polarized SANS"
weight = 40
+++

### Polarized SANS

This example shows how to simulate polarized SANS with BornAgain, using the Born
Approximation.

While BornAgain is designed for GISAS experiments (using the Distorted Wave Born
Approximation), it naturally also contains the regular (plane wave) Born Approximation.
Accordingly, BornAgain can also simulate standard small-angle scattering (SAS).

However, there exist
[several other specialized SAS softwares](http://smallangle.org/content/software).
Therefore we do not advertise BornAgain for analysing SAS experiments,
and in general we do not provide user support for this application domain.
We rather recommend [SASView](https://www.sasview.org/),
which is institutionally supported by the European Spallation Source,
and was designated as standard SAS software in the European SINE2020 project.

Yet BornAgain can be an appropriate choice in cases where the sample structure or
the experimental conditions are not covered by other software.
For example, other softwares provide no, or limited, support for polarized SANS.
Here, we show how such experiments can be simulated with BornAgain.

The main difference between simulating GISAS and SAS in BornAgain is the presence
of only a single layer in the multilayer object. This triggers the software to
calculate the differential scattering cross section in the Born Approximation:

{{< highlight python>}}
multiLayer = ba.MultiLayer()
multiLayer.addLayer(solvent_layer)
{{< /highlight >}}

The rest of the example script hereafter contains nothing new compared to the
previous examples. A sample with a magnetic core-shell particle is constructed.
Beam and detector are setup to detect the spin-flip scattering channel and the
result of this simulation is plotted as usual.

{{< galleryscg >}}
{{< figscg src="PolarizedSANS.png" width="600px" caption="Intensity images">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/PolarizedSANS.py" language="python" >}}
