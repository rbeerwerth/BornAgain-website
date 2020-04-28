+++
title = "Find background"
weight = 30
+++

## Find background

This example demonstrates how to introduce a background in the simulation and fit its value.
Here we are simulating cylinders on top of a substrate without interference. The simulation builder function, defined at line 42, requires 4 parameters:

+ the height of the cylinders
+ the radius of the cylinders
+ the value of the constant background
+ a scale factor for the beam's intensity

The radius and height of the cylinders are passed to the function constructing the multi layer
while the scale and background values are used to initialize the instrument.

{{< highlightfile file="/static/files/python/fitting/ex02_AdvancedExamples/find_background.py" language="python" >}}
