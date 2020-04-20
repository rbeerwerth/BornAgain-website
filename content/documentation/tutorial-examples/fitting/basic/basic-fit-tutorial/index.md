+++
title = "Basic fit example"
weight = 20
+++

## Basic fit example

In this example we use a simple geometry: cylinders and prisms in an air layer, deposited on a substrate layer, with no interference. There are 4 fitting parameters:

1. the radius of the cylinders
2. the height of the cylinders
3. the side length of the prisms
4. the height of the prisms

Our reference data is a “noisy” two-dimensional intensity map obtained from the simulation of the same geometry with a fixed value of 5nm for all sizes of the cylinders and prisms.
Then we run the fit using the default minimizer settings starting with a cylinder height of $4$ nm, a cylinder radius of $6$ nm, a prism half side of $12$ nm and height equal to $4$ nm. 
As a result, the fitting procedure is able to find the correct value of $5$ nm for all four parameters.

{{< galleryscg >}}
{{< figscg src="basic_fitting_tutorial.png" width="600px" caption="Fit window">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/fitting/ex01_BasicExamples/basic_fitting_tutorial.py" language="python" >}}
