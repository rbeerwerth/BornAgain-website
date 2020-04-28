+++
title = "Minimal fitting example"
weight = 30
+++

## Minimal fitting example

On this page you will find a small example of a script that needs to be created to run a fitting. 
The scattering from spherical nano particles in the Born approximation is used here as an example.
Short explanations follow below.

{{< highlight python "linenos=table" >}}
"""
Minimal working fit examples: finds radius of sphere in Born approximation.
"""
import bornagain as ba
from bornagain import deg, angstrom, nm


def get_simulation(params):
    """
    Returns GISAS simulation for given set of parameters.
    """
    radius = params["radius"]

    sphere = ba.Particle(ba.HomogeneousMaterial("Particle", 6e-4, 2e-8),
                         ba.FormFactorFullSphere(radius))

    layer = ba.Layer(ba.HomogeneousMaterial("Air", 0.0, 0.0))
    layer.addLayout(ba.ParticleLayout(sphere))
    multi_layer = ba.MultiLayer()
    multi_layer.addLayer(layer)

    simulation = ba.GISASSimulation()
    simulation.setDetectorParameters(100, -1.0*deg, 1.0*deg,
                                     100, 0.0*deg, 2.0*deg)
    simulation.setBeamParameters(1.0*angstrom, 0.2*deg, 0.0*deg)
    simulation.setSample(multi_layer)

    return simulation


def real_data():
    """
    Generating "experimental" data by running simulation with default parameters.
    """
    simulation = get_simulation({'radius': 5.0*nm})
    simulation.runSimulation()
    return simulation.result().array()


def run_fitting():
    """
    Setups and runs fit.
    """
    fit_objective = ba.FitObjective()
    fit_objective.addSimulationAndData(get_simulation, real_data())
    fit_objective.initPrint(10)

    params = ba.Parameters()
    params.add("radius", 4.*nm, min=0.01)

    minimizer = ba.Minimizer()
    result = minimizer.minimize(fit_objective.evaluate, params)
    fit_objective.finalize(result)


if __name__ == '__main__':
    run_fitting()
{{< /highlight >}}

#### Simulation builder

*Simulation builder* is represented by the `get_simulation` function. Its main task is to generate a
new simulation object for the given values of the fit parameters.
In the given case it returns a GISAS simulation object with a beam, detector and user sample defined.
Here we are simulating the scattering from spherical nano particles in the Born approximation. The function has one free parameter: the radius of the spheres in nanometers.
This is the value we will try to find in the course of the minimization.

#### The data

*Experimental data* is represented by the `real_data` function. It returns a 2D `numpy` array with intensity values obtained from the same simulation with the radius of the spheres equals to $5~nm$.

#### Fit objective

The method `FitObjective.addSimulationAndData` is used to put the *model* and the *data* in correspondence.
Please pay attention on how `get_simulation` (no brackets) and `real_data()` (with brackets) are used.
The absence of brackets in `get_simulation` means that we pass a callable object (aka function pointer) to `FitObjective`.
During the fit it will be used on every iteration to generate a new simulation for every new set of fit parameter values.

#### Fit parameters and minimizers

The fit parameters collection contains a single fit parameter with the name *radius* and a starting value of $4~nm$. The method `FitObjective.evaluate` serves as the objective function. It is passed to the minimizer together with the fit parameters.