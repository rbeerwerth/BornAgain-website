+++
title = "Functionality overview"
weight = 10
+++

### Functionality overview

This section provides a bird's-eye view of the functionality provided by BornAgain.

#### Multilayers

* Multilayers with arbitrary number of layers
* Optional roughness of layer interfaces
* Correlation between different interface roughness profiles
* Magnetic materials

{{< figscg src="fct_layer.png" width="400px" caption="Multilayered structure with roughness" class="center">}}

#### Particles

* Library of basic shapes of particles (form factors)
* Particles with inner structures
* Possibility to assemble complex particle shapes from the basic ones
* Size distribution of particles (polydispersity)

{{< figscg src="fct_diff_ff.png" caption="Selection of available shapes: basic shapes, combinations of particles, core-shell particles and polydisperse particles" class="center">}}

#### Positions of particles

In BornAgain, the in-plane and out-of-plane positions of particles are decoupled. Out-of-pane positions are set by the user to a specific value for each particle, while the correlation between the in-plane positions is encoded by an interference function. 

* Out-of-plane: particles at specific depth in layers or on top.

{{< figscg src="fct_buried_emb_part.png" width="400px" caption="Deposited or embedded layers of particles" class="center">}}

* In-plane correlations
  * Fully disordered systems
  * Short-range order (paracrystals)
  * Two- and one-dimensional lattices

{{< figscg src="fct_disorder_lattice.png" caption="Examples of in-plane distributions of particles: disordered and 2D lattice" class="center">}}

#### Beam

* Polarized or unpolarized neutrons
* X-rays
* Divergence of the beam (wavelength, incident angles) according to different distributions

{{< figscg src="fct_beamdiv.png" width="400px" caption="Beam with angular divergence" class="center">}}

#### Detector

* Spherical detectors, defined by their angular range
* Rectangular detectors, defined by their size and relative position to the sample
* Optional polarization analysis

#### Background/noise

* Background of constant intensity
* Poisson noise

#### Use of BornAgain

* Simulation of different scattering experiments: GISAXS, GISANS, off-specular and specular scattering
* Fitting of simulations to measured data
* Interactions via Python scripts or graphical user interface (GUI)

