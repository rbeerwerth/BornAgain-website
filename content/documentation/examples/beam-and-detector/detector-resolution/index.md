+++
title = "Detector resolution function"
weight = 20
+++

### Detector resolution function

By default, the detector has perfect resolution.
Here we show how to set a finite blur.

* The detector resolution function is a two-dimensional Gaussian with the same width for the $x$ and $y$ axes: $\sigma\_x = \sigma\_y = 0.0025^{\circ}$.
* The wavelength is equal to $1$ $\unicode{x212B}$.
* The incident angles are $\sigma_{\alpha\_i} = \sigma\_{\phi\_i} = 0.1^{\circ}$.

Besides this, the example is a DWBA simulation for our standard sample model,
 [Cylinders in DWBA]({{% ref-example "embedded-particles/cylinders-dwba" %}})

* The sample is composed of monodisperse cylinders deposited on a substrate.
* The cylinders are dilute and distributed at random,
  hence there is no interference between scattered waves.

{{< galleryscg >}}
{{< figscg src="DetectorResolutionFunction.png" width="350px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex05_BeamAndDetector/DetectorResolutionFunction.py" language="python" >}}
