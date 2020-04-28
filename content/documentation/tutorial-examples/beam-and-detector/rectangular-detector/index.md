+++
title = "Rectangular detector"
weight = 40
+++

### Rectangular detector

In this example we demonstrate the difference between GISAS simulation using default spherical detector and using special rectangular detector. The later provides more accurate representation of real experimental detectors.

> See the [Detector types]({{% relref "documentation/scripting/detectors" %}}) tutorial for detailed explanations about various detector types in BornAgain.

* As an example we take typical PILATUS detector ($981\times1043$ pixels) placed at the distance $2000$ mm from sample origin. The detector is perpendicular to the $x$-axis of sample reference frame, as shown on the plot.
* Scattering from monodisperse distribution of cylindrical particles in DWBA is simulated.
* Two detectors are defined in the code: a spherical detector (line 42) and rectangular detector (line 58). They parameters are selected to represent a real PILATUS detector as close as possible.
* We run two simulations for two different detectors independently, and then compare results.
Both simulations looks very much alike. The relative difference plot indicates the difference on the level $10^{-1}-10^{-3}$.
* The difference is coming from the fact, that detector pixel shapes, as well as coordinates of pixel centers in $\phi\_f$, $\alpha\_f$ space, are slighly different in the case of spherical and rectangular detectors.

{{< galleryscg >}}
{{< figscg src="RectangularDetector_setup.jpg" width="650px" caption="Real-space model">}}
{{< figscg src="RectangularDetector.png" width="700px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex05_BeamAndDetector/RectangularDetector.py" language="python" >}}
