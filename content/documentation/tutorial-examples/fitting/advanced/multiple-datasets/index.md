+++
title = "Simultaneous fit of two datasets"
weight = 40
+++

## Simultaneous fit of two datasets

In this example we demonstrate how to fit two datasets simultaneously.

Suppose that we have a sample measured twice for two different incident angles. We are going to fit both datasets simultaneously to find the unknown sample parameters.

To do this, we define one dataset (a pair of real data and corresponding simulation builder) for the first incidence angle and another pair for the second incidence angle. We add both pairs to the `FitObjective` and run the fit as usual.

+ In the given script we simulate hemi-ellipsoids on top of a substrate without interference. At lines 184-186 we define 3 fitting parameters: `radius_a` and `height` are parameters to find, `radius_b` is fixed.
+ At lines 171-145 we define two fixed incident alpha angles equal to $0.1^{\circ}$ and $0.4^{\circ}$ and generate two arrays with experimental data.
+ The functions defined at lines 55 and 60 represent simulation builders to use together with the experimental data.
+ The FitObjective is initialized on lines 174-176 with two simulation/data pairs.
* The majority of the code is located in a custom `PlotObserver` class (defined in line 85, and invoked at lines 180, 181), which plots the fit progress for the two datasets every 10th iteration.

{{< galleryscg >}}
{{< figscg src="multiple_datasets.png" width="600px" caption="Fit window">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/fitting/ex02_AdvancedExamples/multiple_datasets.py" language="python" >}}
