+++
title = "Reflectometry"
weight = 16
+++

## Specular simulation tutorial

In this example, we will simulate specular signal from a sample with 10
double layers of Ti-Ni on silicon substrate in vacuum environment.

### Importing the Python modules

We start by importing the BornAgain Python API and alias it as `ba`.
Then we import some often used unit designations from BornAgain.

{{< highlight python >}}

import bornagain as ba
from bornagain import deg, angstrom

{{< /highlight >}}

### Sample definition

Our sample will consist of (in the order from top to bottom):

1. Ambient layer (which is not the sample by itself, but is used as initial media
   of beam propagation) with scattering length density (SLD) exactly equal to zero.
1. Ten repetitions of
  * 3 nm thick titanium layer with SLD $\rho_{Ti} = -1.9493 \cdot 10^{-6}$ $\unicode{x212B}^{-2}$.
  * 7 nm thick nickel layer with SLD $\rho_{Ni} = 9.4245 \cdot 10^{-6}$ $\unicode{x212B}^{-2}$.
1. Substrate silicon layer with SLD $\rho_{Si} = 2.0704 \cdot 10^{-6}$ $\unicode{x212B}^{-2}$.

As in many other tutorials we will create the sample with dedicated function

{{< highlight python >}}

def get_sample():
    """
    Defines sample and returns it
    """

{{< /highlight >}}

At first we will create materials of our sample. Here we will use `MaterialBySLD`,
general syntax of which is as follows

```python
<material> = MaterialBySLD("name", sld_real, sld_imag)
```

where `name` is the arbitrary name of the material, `sld_real` and `sld_imag` correspond to real and imaginary part of material scattering length density in $\unicode{x212B}^{-2}$. Variable `<material>` is later used when referring to this particular material. In this example we will create four materials: `m_ambient`, `m_ti`, `m_ni` and `m_substrate`:

{{< highlight python >}}

    m_ambient = ba.MaterialBySLD("Ambient", 0.0, 0.0)
    m_ti = ba.MaterialBySLD("Ti", -1.9493e-06, 0.0)
    m_ni = ba.MaterialBySLD("Ni", 9.4245e-06, 0.0)
    m_substrate = ba.MaterialBySLD("SiSubstrate", 2.0704e-06, 0.0)

{{< /highlight >}}

Here we assume for simplicity absorption coefficients (imaginary part of SLDs) being equal to zero.

{{< notice note >}}
One can find out more about materials in BornAgain from [material types tutorial]({{% relref "documentation/scripting/materials/index.md" %}}).
{{< /notice >}}

After creating materials, we create associated layers. It is done with `Layer`
command:

```python
<layer> = Layer(<material>[, thickness])
```

The first argument to the command (`<material>`) is the material object created previously with
`MaterialBySLD` command. The second argument (`thickness`) is the thickness of the layer. Default units are
nanometers. The thickness shall be specified only for the intermediate layers, while the ambient
and substrate layers are considered half-infinite. Further we create four layers from previously
defined materials:

{{< highlight python >}}

    ambient_layer = ba.Layer(m_ambient)
    ti_layer = ba.Layer(m_ti, 30 * angstrom)
    ni_layer = ba.Layer(m_ni, 70 * angstrom)
    substrate_layer = ba.Layer(m_substrate)

{{< /highlight >}}

Note that here we used angstroms as thickness units by multiplying thickness values
by imported `angstrom` factor.

Finally, we create the `MultiLayer` --- enclosing object, which contains all sample
properties:

{{< highlight python >}}

    multi_layer = ba.MultiLayer()
    multi_layer.addLayer(ambient_layer)
    for i in range(10):
        multi_layer.addLayer(ti_layer)
        multi_layer.addLayer(ni_layer)
    multi_layer.addLayer(substrate_layer)

{{< /highlight >}}

`MultiLayer()` command creates empty sample. After that the layers are added into it
one by one from top to bottom with `addLayer` command. Note that titanium and nickel
layers are added in a cycle, which create periodic Ti/Ni structure.

Summing up all the code snippets, we get the following `get_sample` function:
{{< highlight python >}}

def get_sample():
    """
    Defines sample and returns it
    """

    # creating materials
    m_ambient = ba.MaterialBySLD("Ambient", 0.0, 0.0)
    m_ti = ba.MaterialBySLD("Ti", -1.9493e-06, 0.0)
    m_ni = ba.MaterialBySLD("Ni", 9.4245e-06, 0.0)
    m_substrate = ba.MaterialBySLD("SiSubstrate", 2.0704e-06, 0.0)

    # creating layers
    ambient_layer = ba.Layer(m_ambient)
    ti_layer = ba.Layer(m_ti, 30 * angstrom)
    ni_layer = ba.Layer(m_ni, 70 * angstrom)
    substrate_layer = ba.Layer(m_substrate)

    # creating multilayer
    multi_layer = ba.MultiLayer()
    multi_layer.addLayer(ambient_layer)
    for i in range(10):
        multi_layer.addLayer(ti_layer)
        multi_layer.addLayer(ni_layer)
    multi_layer.addLayer(substrate_layer)

    return multi_layer

{{< /highlight >}}

### Setting up simulation parameters

{{< highlight python >}}

def get_simulation(scan_size=500):
    """
    Defines and returns a specular simulation.
    """
    simulation = ba.SpecularSimulation()
    scan = ba.AngularSpecScan(1.54 * angstrom, scan_size,
                              0.0 * deg, 2.0 * deg)
    simulation.setScan(scan)
    return simulation

{{< /highlight >}}

In this code snippet we have 1. initialized a reflectometry specular simulation with `ba.SpecularSimuation()`, 
2. defined the type of scan to be used for the simulation, and 
3. use that scan for the simulation just created. The general sintax to define a scan is:

```python
scan = ba.AngularSpecScan(wavelength, n_bins, angle_min, angle_max)
simulation.setScan(scan)
```

where the `wavelength` of the incident beam is in nanometers;
the initial and final angles to be swept by the beam, `angle_min` and `angle_max`, are in radians; 
and `n_bins` defines the number of points to be uniformly sampled between `angle_min` and `angle_max`.

One can express the input arguments in degrees and angstroms via the conversion factors `ba.deg` and `ba.angstrom`.

Note that, as opposed to a `GISASSimulation`s (see [GISAS simulation tutorial]({{% relref "documentation/scripting/simulation-classes/gisas/index.md" %}})),
`SpecularSimuation`s do not need to define a detector. Their outcomes are always reflected intensities as
function of the selected incident angles.

### Running the simulation and plotting the results

{{< highlight python >}}

def run_simulation():
    """
    Runs simulation and returns its result.
    """
    sample = get_sample()
    simulation = get_simulation()
    simulation.setSample(sample)
    simulation.runSimulation()
    return simulation.result()

{{< /highlight >}}

The function `run_simulation` gathers together all previously defined items.
We first create the sample and simulation objects using calls to the previously defined functions.
Then we assign the sample to the simulation and finally launch the simulation with `runSimulation`.
In the last line, we obtain the result of the simulation as a `SimulationResult` object,
which contains the axes definition and the simulated intensity as a function of
the beam inclination angle $\alpha_i$.

{{< highlight python >}}

if __name__ == '__main__':
    result = run_simulation()
    ba.plot_simulation_result(result)

{{< /highlight >}}

To plot the data using matplotlib routines, we use a convenience function, defined in the BornAgain namespace: `plot_simulation_result()`.

As a result of executing the whole script in the python interpreter
```bash
$ python BasicSpecularSimulation.py
```

The following image should be displayed on the screen

{{< figscg src="BasicSpecResult.png" width="500" class="center">}}

### Further topics

Further examples of specular simulations with `BornAgain` can be found on the following pages:

* [specular signal from a rough sample]({{% relref "documentation/examples/reflectometry/specular-simulation-with-roughness/index.md" %}})
* [beam footprint correction]({{% relref "documentation/examples/reflectometry/footprint-correction/index.md" %}})
* [beam divergence in specular simulations]({{% relref "documentation/examples/reflectometry/beam-full-divergence/index.md" %}})
* [fitting reflectometry data]({{% relref "documentation/examples/fitting/extended/fit-specular-data/index.md" %}})

### Complete script

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/BasicSpecularSimulation.py">}}
