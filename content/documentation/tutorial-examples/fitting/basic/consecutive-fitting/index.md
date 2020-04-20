+++
title = "Consecutive fitting"
weight = 40
+++

## Consecutive fitting

This example demonstrates how to run two fits one after the other using different minimizer settings and starting values of the fit parameters.

* In this example we are looking for the `radius` and `height` of cylindrical nano particles randomly distributed on a surface.
* During the first (started at line 101) fit we are setting the initial values of the fit parameters to be quite far from the expected values and use a genetic minimizer to explore a large parameter space.
* The second fit at line 112 starts from the best parameter values found in the previous step and uses one of the gradient descent algorithms to find the precise location of the minimum.

{{< highlightfile file="/static/files/python/fitting/ex01_BasicExamples/consecutive_fitting.py" language="python" >}}
