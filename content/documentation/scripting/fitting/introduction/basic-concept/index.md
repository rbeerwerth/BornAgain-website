+++
title = "Basic concept"
weight = 10
+++

## Basic concept

Fitting in BornAgain is no different from any other optimization problem, like fitting a curve to some data points.
The user has to define an objective function, which takes the values of the fitting variables and calculates
the metric that needs to be minimized.
The objective function has to be passed to the minimization engine, together with the starting values of the fit parameters.

The following code snippet was borrowed from the
[Getting started with Non-Linear Least-Squares Fitting](https://lmfit.github.io/lmfit-py/intro.html) 
tutorial of the [lmfit](https://lmfit.github.io/lmfit-py) package to demonstrate the basic principles of curve fitting.

{{< highlight python >}}
from numpy import exp, sin
from scipy.optimize import leastsq

def residual(vars, x, data, eps_data):
    amp = vars[0]
    phaseshift = vars[1]
    freq = vars[2]
    decay = vars[3]

    model = amp * sin(x*freq + phaseshift) * exp(-x*x*decay)

    return (data-model) / eps_data

vars = [10.0, 0.2, 3.0, 0.007]
out = leastsq(residual, vars, args=(x, data, eps_data))
{{< /highlight >}}

The objective function `residual` takes the values of the fit parameters, data points and errors. It then calculates a vector of residuals using a hard coded `model` of the data: a decaying `sin` wave.

The minimum of the objective function is then found using the `leastsq` method of the `scipy.optimize` package.

{{< alert theme="info" >}}
Similarly, fitting in BornAgain is all about constructing an objective function that represents the difference between simulation and data, and passing it to a minimization engine.
{{< /alert >}}

Conceptually, the `residual` objective function should adjust the scattering sample using the fit parameters provided, run the simulation and then calculate the difference between the experimental and simulated scattering images.

The corresponding pseudo code is shown below.

{{< highlight python >}}
from scipy.optimize import leastsq

def residual(sample_pars):
    sample = create_sample(sample_pars)
    simulation.setSample(sample)
    simulation.runSimulation()
    return exp_intensities-simulation

sample_pars = [42]
out = leastsq(residual, sample_pars)
{{< /highlight >}}



