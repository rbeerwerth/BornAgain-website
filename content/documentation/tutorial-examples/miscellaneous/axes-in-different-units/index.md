+++
title = "Plotting with axes in different units"
weight = 20
+++

### Plotting with axes in different units

In this example we demonstrate how to plot intensity data with detector axes expressed in different units. It serves as a supporting example to the [Accessing simulation results
]({{% ref-tutorial "accessing-simulation-results/index.md" %}}) tutorial.

* The standard "Cylinders in DWBA" sample (see [this example]({{%ref-example "embedded-particles/cylinders-dwba" %}})) is used to setup the simulation.
* When the simulation is completed, the `Simulation::result()` method is used to get a `SimulationResult` object.
* Depending on an additional parameter `IDetector2D.NBINS`, `IDetector2D.DEGREES`, `IDetector2D.QYQZ`, it will be plotted with axes defined either in millimeters (default units of `RectangularDetector`), detector bins, degrees or in $Q$-space.
* Please note, that the given parameter only affects min/max values of histogram axes (there is no rebinning involved).

{{< galleryscg >}}
{{< figscg src="AxesInDifferentUnits.png" width="670px" caption="Intensity images">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/AxesInDifferentUnits.py" language="python" >}}
