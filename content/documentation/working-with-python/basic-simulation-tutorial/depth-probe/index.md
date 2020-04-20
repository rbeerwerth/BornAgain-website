+++
title = "Depth-probe"
weight = 17
+++

## Depth-probe simulation tutorial

Depth-probe simulation is an auxiliary simulation type, which helps to visualize
the total intensity in dependence on the beam incidence angle and the position in
the sample.

Here we will consider the intensity map produced by a neutron resonator,
composed of one Ti/Pt bilayer.

### Used conventions

Depth-probe simulation takes into account the position across the surface of the sample.
This position will be denoted as ''z'' and measured in nanometers.
The surface of the sample will be assigned to $z = 0$, while the direction of z-axis
will be from the bulk of the sample out to the ambient. That is, $z < 0$
corresponds to the region from the substrate to the surface of the sample, and $z > 0$
corresponds to the ambient media.

### Sample description

{{< figscg src="DepthProbeSample.png" width="500" class="center">}}

The layout of the sample is presented in the figure above.
A Ti-Pt sample on a silicon substrate is placed in $D_2 O$ environment and
is irradiated by a diagnostic beam. Note that in this layout the beam enters
the sample from the substrate side. For this reason the sample has reversed structure,
with silicon being defined as the ''ambient media'' and $D_2 O$ being defined as the
''substrate''.

Before constructing the sample we will import `bornagain` library and units
which will be used throughout our tutorial:

{{< highlight python >}}

import bornagain as ba
from bornagain import deg, angstrom, nm

{{< /highlight >}}

The process of constructing the sample is the same as the one described in  
[GISAS]({{% ref-tutorial "basic-simulation-tutorial/gisas/index.md" %}})
and [reflectometry]({{% ref-tutorial "basic-simulation-tutorial/reflectometry/index.md" %}})
tutorials. First of all we will define the `get_sample` function:

{{< highlight python >}}

def get_sample():
    """
    Constructs a sample with one resonating Ti/Pt bilayer
    """

{{< /highlight >}}

Then we will create the materials of the sample, substrate and the ambient media:

{{< highlight python >}}

    # define materials
    m_Si = ba.HomogeneousMaterial("Si", 3.3009e-05, 0.0)
    m_Ti = ba.HomogeneousMaterial("Ti", -3.0637e-05, 1.5278e-08)
    m_TiO2 = ba.HomogeneousMaterial("TiO2", 4.1921e-05, 8.1293e-09)
    m_Pt = ba.HomogeneousMaterial("Pt", 1.0117e-04, 3.01822e-08)
    m_D2O = ba.HomogeneousMaterial("D2O", 1.0116e-04, 1.8090e-12)

{{< /highlight >}}

Note, that here we set the attenuation factor for silicon to zero. It is necessary,
since this material will serve as the media of the beam propagation and is assumed to be
semi-infinite. Thus setting a non-zero attenuation factor will lead to complete
dissipation of the beam even before its entering the sample.

After the materials are defined, it is necessary to create the layers and the
`MultiLayer` object representing the whole sample:

{{< highlight python >}}

    # create layers
    l_Si = ba.Layer(m_Si)
    l_Ti = ba.Layer(m_Ti, 130.0 * angstrom)
    l_Pt = ba.Layer(m_Pt, 320.0 * angstrom)
    l_Ti_top = ba.Layer(m_Ti, 100.0 * angstrom)
    l_TiO2 = ba.Layer(m_TiO2, 30.0 * angstrom)
    l_D2O = ba.Layer(m_D2O)

    # construct sample from top to bottom
    sample = ba.MultiLayer()
    sample.addLayer(l_Si)

    sample.addLayer(l_Ti)
    sample.addLayer(l_Pt)

    sample.addLayer(l_Ti_top)
    sample.addLayer(l_TiO2)
    sample.addLayer(l_D2O)

    return sample

{{< /highlight >}}

### Setting up the depth-probe simulation

Depth-probe simulation can be created with the command `DepthProbeSimulation()`,
while its parameters are set with `setBeamParameters` and `setZSpan`.
The signature of `setBeamParameters` coincides completely with the signature
of analogous method in `SpecularSimulation`:

```python
<simulation>.setBeamParameters(wavelength, n_bins, angle_min, angle_max)
```

Here `<simulation>` is the simulation object created with `DepthProbeSimulation` command,
`wavelength` is the wavelength of the incident beam (in nanometers by default),
`angle_min` and `angle_max` --- minimum and maximum incident angles (in radians by default).
Units of the input arguments can be adjusted by multiplying factors `deg`, `angstrom`, etc.
`n_bins` defines the number of points uniformly distributed from `angle_min` to `angle_max`.

`setZSpan` allows to define the coordinates across the sample surface,
at which the signal intensities should be calculated. The signature of the command is

```python
<simulation>.setZSpan(n_z_bins, z_min, z_max)
```

Again, `<simulation>` is the object created with `DepthProbeSimulation` command,
`z_min` and `z_max` denote the limits of the z-axis (in nanometers by default), while
`n_z_bins` defines the number of points uniformly distributed
between `z_min` and `z_max`.

Let us write down `get_simulation` function, which creates a depth-probe simulation
with incident angle range from $0^{\circ}$ to $1^{\circ}$ and 5000 points in between.
The z-axis will be defined as the range $[-100, 100]$ nm with 500 points.

{{< highlight python >}}

def get_simulation():
    """
    Returns a depth-probe simulation.
    """
    simulation = ba.DepthProbeSimulation()
    simulation.setBeamParameters(10 * angstrom, 5000, 0.0 * deg, 1.0 * deg)
    simulation.setZSpan(500, -100 * nm, 100 * nm)
    return simulation

{{< /highlight >}}

### Running the simulation and plotting the results

Running the simulation does not differ from doing it with any other type
of simulation in `BornAgain`:

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

Plotting can be done with built-in `BornAgain` function `plot_simulation_result`:

{{< highlight python >}}

if __name__ == '__main__':
    result = run_simulation()
    ba.plot_simulation_result(result)

{{< /highlight >}}

As a result of executing the script, the following image
should be displayed on the screen

{{< figscg src="DepthProbeSimulation.png" width="500" class="center">}}

In this figure the y-axis corresponds to the position across the sample surface
(in nanometers), while the x-axis corresponds to the
incident angle values $\alpha_i$.

### Complete script

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/DepthProbe.py" language="python" >}}
