+++
title = "Fitting in GISAS"
weight = 20
+++

## Fitting in GISAS

A GISAS data fit deals with the following 5 components:

+ [Experimental data](#experimental-data)
+ [Simulation builder](#simulation-builder)
+ [Fit objective](#fit-objective)
+ [Fit parameters](#fit-parameters)
+ [Minimizer](#minimizer)

{{< figscg src="fit_modules.png" width="600" class="center">}}

#### Experimental data

The experimental data is a 2D numpy array, obtained in the course of a GISAS experiment and containing a 2D map of the intensities measured in the detector channels.

#### Simulation builder

This is a Python callable, a function or a class method, returning a `GISASSimulation` object with beam, detector and user sample defined.
The function accepts a Python dictionary as input parameters, which it uses to build a new simulation object. The parameter values will be varied during the fit and `get_simulation` will be called on every fit iteration.

{{< highlight python >}}

def get_simulation(params):
    simulation = GISASSimulation()
    ...
    simulation.setBinIntensity(params["intensity"])
    ...
    return simulation

{{< /highlight >}}

The main requirement here is that the geometry of the detector defined in the `GISASSimulation` object
matches the shape of numpy array with the experimental intensities.

#### Fit objective

A special module providing an objective function for the minimizer.

It contains at least one pair of *experimental data/simulation builder* and the logic 
to retrieve new simulation results on every fit iteration and compare them against the experimental one.

{{< highlight python >}}
fit_objective = FitObjective()
fit_objective.addSimulationAndData(get_simulation, real_data)
{{< /highlight >}}

The `FitObjective` public interface provides access to two objective functions

+ `FitObjective.evaluate(params)` returns $\chi\_{2}$ calculated for experimental/simulated images
+ `FitObjective.evaluate_residuals(params)` returns 1d vector of residuals for all bins of the experimental/simulated images

#### Fit parameters

A collection of fit parameters which will be varied during the fit.

The BornAgain fit parameters and minimizer interface was developed with the idea to simplify the switch between our own minimization engines and other, possibly more advanced, minimization libraries.
Particularly, we have been inspired by [lmfit Python package](https://lmfit.github.io/lmfit-py/),
which explains why the BornAgain setup looks very similar.

For each fit parameter one has to define a unique name, starting value and parameter bounds.
The name of the fit parameter should coincide with the name that the simulation builder function expects.

{{< highlight python >}}
params = ba.Parameters()
params.add("intensity", 1e+08, min=1e+07, max, 1e+08)
params.add("sphere_radius", 10*nm, min=0.1)
{{< /highlight >}}

#### Minimizer

Provides  the top level interface for multiple minimization engines.

In the code snippet below we create a default BornAgain minimizer and start the minimization by calling the `minimize` function. The minimizer takes an objective function and the fit parameters as input.

{{< highlight python >}}
minimizer = ba.Minimizer()
minimizer.minimize(fit_objective.evaluate, params)
{{< /highlight >}}

## Minimization workflow

After all fit components are in place, the users can start the minimization by running the `minimize` method. The figure below shows the general workflow of a minimization procedure.

{{< figscg src="minimization_workflow.png" width="650" class="center">}}

The minimization workflow involves many iterations, during each of which

+ the minimizer makes an assumption about the optimal sample parameters,
+ these parameter values are propagated to the simulation builder,
+ a simulation is performed for the given parameter values,
+ the simulated data (intensities) is propagated to the module calculating the difference between simulated and experimental data,
+ the result of the calculations, represented by a $\chi\_{2}$ value of the vector of residuals, is propagated to the minimizer,
+ the minimizer makes new assumptions about the optimal fit parameter values.

The iteration process is going on under the control of the selected minimization algorithm, without any intervention from the user. It stops if one of the following is true:

+ the maximum number of iteration steps has been reached
+ the function’s minimum has been reached within a certain tolerance
+ the minimizer cannot improve the $\chi\_{2}$ estimate further

After the control has returned, the fitting results can be retrieved. These include the best $\chi\_{2}$ value found, the corresponding optimal sample parameter values and the intensity map simulated with this set of values.