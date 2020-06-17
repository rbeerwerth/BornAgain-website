+++
title = "1D lattice"
weight = 10
+++

### Interference 1D lattice

In this example we simulate the scattering from infinite 1D repetition of rectangular patches (rectangular grating). This is done by using the interference function of a 1D lattice together with very long boxes. 

* By-default, the axis of the one-dimensional lattice coincides with the $x$-axis of the reference cartesian frame, so it coinsides with the beam direction.
* Long boxes are placed along a one-dimensional lattice on top of substrate, the lattice_length parameter corresponds to the grating period.
* The size of boxes is initially chosen to form a grating which is perpendicular to the beam (long side of the box is along $y$-axis).
* Please keep in mind, that `length`, `width`, `height` in the `FormFactorBox(length, width, height)` constructor correspond to the directions in the $x,y,z$ axes, in that order, so to achieve the desired setup we use the values: `length`= $10$ nm, `width`= $10000$ nm, `height`= $10$ nm.
* The whole grating is rotated at the end by an angle of $45^{\circ}$ with respect to the beam axis. This is achieved by rotating _both_ the 1D lattice and the long boxes (see lines 25 and 34).
* To avoid the problem of rapidly oscillating form factors of long boxes (see [this example]({{% ref-example "complex-shapes/large-particles-formfactor" %}}) for more details), the simulation is performed in monte carlo integration mode.

{{< galleryscg >}}
{{< figscg src="Interference1DLattice_setup.jpg" width="200px" caption="Real-space model">}}
{{< figscg src="Interference1DLattice_sketch.jpg" width="200px" caption="Sketch">}}
{{< figscg src="Interference1DLattice.png" width="200px" caption="Intensity image">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex03_InterferenceFunctions/Interference1DLattice.py" language="python" >}}
