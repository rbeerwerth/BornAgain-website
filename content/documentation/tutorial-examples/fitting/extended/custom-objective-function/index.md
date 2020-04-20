+++
title = "Custom objective function"
weight = 20
+++

## Custom objective function

The BornAgain fitting API allows users to define a custom objective function to for the minimization engine.

In this example we are going to construct a vector of residuals calculated between the
experimental and simulated intensity values after applying an additional $sqrt$ function to the amplitudes.

$$
residuals = [r\_{0}, r_{1}, ... , r\_{n-1}], ~~~ r\_{i} = \sqrt{e\_{i}} - \sqrt{s\_{i}}
$$

The length of vector `n` corresponds to the total number of *non-masked* detector channels.

This is done by defining our own `MyObjective` class at line 14. It is derived from the parent `FitObjective` class and contains our own definition of the `evaluate_residual` function. At line 26 we call the parent's `evaluate` method to run the simulation and prepare the intensity arrays. At lines 30-34 we calculate the vector of residuals as described above.

Later in the code, the `MyObjective.evaluate_residual` function is used to setup a custom objective function for the minimizer (line 116).

{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/custom_objective_function/custom_objective_function.py" language="python" >}}
