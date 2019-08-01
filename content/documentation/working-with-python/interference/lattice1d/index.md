+++
title = "1D lattice"
weight = 10
+++

## Interference function of a one-dimensional lattice

A one dimensional lattice can be viewed as a chain of particles placed at regular intervals on a single axis. The plot below represents one possible use case, where infinitely long (or very long) boxes are placed at nodes of a 1d lattice to form a grating.

{{< figscg src="particles_at_1d_latice.jpg" width="600px" class="center">}}

See the BornAgain user manual (Chapter 3.4.1, One Dimensional Lattice) for details about the theory.

### InterferenceFunction1DLattice constructor

The interference function is created using its constructor

{{< highlight python >}}

InterferenceFunction1DLattice(length, xi)
"""
length   : lattice constant, in nanometers
xi       : rotation of the lattice with respect to the x-axis, in radians
"""

{{< /highlight >}}

`Length` is the length of the lattice basis vector `a` expressed in nanometers (see plot below). `xi` ($\xi$) is the angle defining the lattice orientation. It is taken as the angle between the basis vector of the lattice and the x-axis of the Cartesian coordinate system. It is defined in radians and set to 0 by default.

{{< figscg src="interference_1d_C.png" width="800px" class="center">}}

When the beam azimuthal angle $\varphi_f$ is zero, the beam direction coincides with x-axis. In this case, the $\xi$ angle can be considered as the lattice rotation with respect to the beam.

### Position variance

The position variance parameter `Var`, as depicted on the top plot, allows to introduce uncertainty for each particle position around the lattice point by applying a corresponding Debye-Waller factor.

It can be set using the `setPositionVariance(value)` method, where `value` is given in $nm^2$.

{{< highlight python >}}

lattice = InterferenceFunction1DLattice(100*nm, 0.0*deg)
lattice.setPositionVariance(0.1)
{{< /highlight >}}

By default the variance is set to zero.

### Decay function

To account for finite size effects of the lattice, a decay function should be assigned to the interference function. This function encodes the loss of coherent scattering from lattice points with increasing distance between them. The origin of this loss of coherence could be attributed to the coherence length of the beam or to the domain structure of the lattice. 

In the picture below a one dimensional lattice is represented in real space as a probability 
density function for finding a particle at a given coordinate on the x-axis.
In the presence of a decay function, this density can be given as
$\sum F\_{decay}(x)\cdot\delta(x-na)$.

{{< figscg src="lattice1d_decay_real.png" width="800px" class="center">}}

The Fourier transform of this distribution $P(x)$ provides the scattering amplitude in reciprocal space. An exponential decay law in real space with the decay length $\lambda$ 
will give a Cauchy distribution with characteristic width $1/\lambda$ in reciprocal space, as shown below.

{{< figscg src="lattice1d_decay_reciprocal.png" width="800px" class="center">}}

The decay function can be set using the setDecayFunction(decay) method of the 1D interference function.


{{< highlight python >}}

iff = InterferenceFunction1DLattice(10.0*nm)
iff.setDecayFunction(FTDecayFunction1DCauchy(1000.0*nm))

{{< /highlight >}}

### List of decay functions

BornAgain supports four types of one-dimensional decay functions. 

+ `FTDecayFunction1DCauchy(decay_length)`

One-dimensional Cauchy decay function in reciprocal space,
corresponds to $exp(-|x|/\lambda)$ in real space.


+ `FTDecayFunction1DGauss(decay_length)`

One-dimensional Gauss decay function in reciprocal space,
corresponds to $exp(-x^2/(2*\lambda^2))$ in real space.

+ `FTDecayFunction1DTriangle(decay_length)`

One-dimensional triangle decay function in reciprocal space,
corresponds to $1-|x|/\lambda$, if $|x|<\lambda$, in real space.

+ `FTDecayFunction1DVoigt(decay_length, eta)`

One-dimensional pseudo-Voigt decay function in reciprocal space, corresponds to $eta*Gauss + (1-eta)*Cauchy$.

The parameter $\lambda$ (decay length) is given in nanometers, it is used to set the characteristic length scale at which loss of coherence takes place. In the case of the pseudo-Voigt distribution an additional dimensionless parameter `eta` is used to balance between the Gaussian and Cauchy profiles.

### Particle Density

During the simulation setup the particle density has to be explicitely specified by the user for correct normalization of overall intensity. This is done by using the `ParticleLayout.setParticleDensity(density)` method. The density parameter is given here in "number of particles per square nanometer".

### Lattice rotation in details

In this paragraph we would like to clarify the relation between the lattice orientation and the orientation of the particles forming the lattice.

{{% alert theme="info" %}}
 The rotation of the lattice doesn't change the orientation of the particles with respect to the beam direction.
{{% /alert %}}

### Setup 1

For example, we would like to create a grating: a repetition of rectangular patches perpendicular to the beam, as shown on the plot (view from the top of the sample).

{{< figscg src="interference_1d_particles_orientA.png" width="800px" class="center">}}

The long side of boxes is aligned along y-axes of the reference plane, the lattice axis coincides with the beam direction, the long side of the boxes is perpendicular to the beam.

To achieve such a setup, the following code should be used.

{{< highlight python >}}

layout = ba.ParticleLayout()
 
box = ba.Particle(material, ba.FormFactorBox(10*nm, 1000*nm, 10*nm))
layout.addParticle(box)
layout.setInterferenceFunction(ba.InterferenceFunction1DLattice(40*nm))

{{< /highlight >}}

### Setup 2

If we rotate the lattice by a certain amount, the orientation of the boxes stays the same, but the effective grating period gets smaller. The setup and code are shown below.

{{< figscg src="interference_1d_particles_orientB.png" width="800px" class="center">}}

{{< highlight python >}}

box = ba.Particle(material, ba.FormFactorBox(10*nm, 1000*nm, 10*nm))
layout.addParticle(box)
layout.setInterferenceFunction(ba.InterferenceFunction1DLattice(40*nm, 30.0*deg))

{{< /highlight >}}

### Setup 3

If we want to preserve the grating period and make our boxes rotate with respect to the beam, a separate rotation should be applied.

{{< figscg src="interference_1d_particles_orientC.png" width="800px" class="center">}}

{{< highlight python >}}

box = ba.Particle(material, ba.FormFactorBox(10*nm, 1000*nm, 10*nm))
box.setRotation(ba.RotationZ(30.0*deg))
layout.addParticle(box)
layout.setInterferenceFunction(ba.InterferenceFunction1DLattice(40*nm, 30.0*deg))

{{< /highlight >}}

### Complete example

The complete example can be found [here]({{% ref-example "interference-functions/interference-1d-lattice" %}}).

### Interference function of 1D lattice in GUI

To Initialize `InterferenceFunction1DLattice` in the graphical user interface, the corresponding object has to be connected with ParticleLayout and the corresponding parameters (lattice length, rotation and parameters of decay function) have to be adjusted in the property editor.

{{< figscg src="interference_1d_gui.png" width="800px" class="center">}}

In the given example, an additional rotation module is attached to the box to provide a rotation around the z-axis and achieve the configuration of [Setup 3]({{% relref "#setup-3" %}})  from the example above.