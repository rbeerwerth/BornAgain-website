+++
title = "Fitting along slices"
weight = 20
+++

## Fitting along slices

Here we demonstrate how to fit along slices. The idea is that the user defines the positions of vertical and horizontal lines crossing the detector plane in regions of most interest (Yoneda wings, Bragg peaks, etc.) and then finds the sample parameters which fits those regions best.

Such an approach uses much less CPU while still giving a chance to find the optimal sample parameters. In general, however, it is arguable whether fitting along slices makes more sense than fitting using the whole detector image.

Technically, the idea is to mask the whole detector except thin lines, one vertical and one horizontal, representing slices. This will make the simulation and the fitting procedure to calculate only along these indicated slices.

* In the given script we simulate cylinders on top of a substrate without interference. The fitting procedure looks for the cylinder's height and radius.
* Lines 55, 56, 57 demonstrate the code you need for masking the whole detector and then unmasking the two desired slices: a vertical line at $\phi=0.0^{\circ}$, and a horizontal line at $\alpha=0.2^{\circ}$.
* The majority of the code is located in the custom `PlotObserver` class (defined in line 76, and invoked at lines 190, 191), which plots the fit progress along the slices every 10th iteration.

{{< galleryscg >}}
{{< figscg src="fit_along_slices.png" width="600px" caption="Fit window">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/fitting/ex02_AdvancedExamples/fit_along_slices.py" language="python" >}}
