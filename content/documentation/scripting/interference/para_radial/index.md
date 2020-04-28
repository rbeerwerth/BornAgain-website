+++
title = "Radial paracrystal"
weight = 30
+++

## Interference function of radial paracrystal

The interference function of a radial paracrystal is used to model cumulative disorder of interparticle distances. It is called radial to stress the fact that it only takes into account the radial component of the scattering vector.

{{< figscg src="interference_para1d_simple.png" width="800px" class="center">}}

Each circle on the plot above represents the area where the probability to find a particle, given a particle at the origin, is above some arbitrary threshold. The growing size of the areas emphasizes the fact the our knowledge about next neighbor's location decreases with the distance to the origin.

The BornAgain user manual (Chapter 3.5, Paracrystal) details the theoretical model and gives some links to the literature.

### InterferenceFunctionRadialParaCrystal class

The radial paracrystal is parameterized by the position distribution of the nearest neighbor centered at the peak distance. On the plot below the half-width of this distribution is marked as $\omega$ and the center is marked with "Peak Distance". The probability distributions of finding other particles to the right  are deduced from accumulating position uncertanties of previous particles in the chain.

{{< figscg src="interference_para1d_b.png" width="800px" class="center">}}

To create the interference function of a radial paracrystal the following constructor has to be used.

{{< highlight python >}}

InterferenceFunctionRadialParacrystal(peak_distance, damping_length=0)
"""
peak_distance   Average distance to the next neighbor in nanometers
damping_length  The damping (coherence) length of the paracrystal in nanometers.
"""

{{< /highlight >}}

The parameter `damping_length` is used to introduce finite size effects by applying a multiplicative coefficient equal to `exp(-peak_distance/damping_length)` to the Fourier transform of the probability density of a nearest neighbor. `damping_length` is equal to 0 by default and, in this case, no correction is applied. On the plot above the damping length is provisionally depicted as an area contributing to the scattering.

### Probability Distribution

To account for next neighbor position uncertainty a probability distribution (Fourier transform of probability density) should be assigned to the interference function. This is done using the `setProbabilityDistribution(pdf)` method of the radial paracrystal interference function.

{{< highlight python >}}

iff = InterferenceFunctionRadialParacrystal(10.0*nm, 1000.0*nm)
iff.setProbabilityDistribution(FTDistribution1DCauchy(30.0*nm))

{{< /highlight >}}

The following distributions are available

{{< highlight python >}}

# Fourier transform of Cauchy-Lorentzian
FTDistribution1DCauchy(omega)

# Fourier transform of a Gaussian
FTDistribution1DGauss(omega)

# Fourier transform of a gate distribution
FTDistribution1DGate(omega)

# Fourier transform of a triangle distribution
FTDistribution1DTriangle(omega)

# Fourier transform of a pseudo-Voigt distribution: eta*Gauss + (1-eta)*Cauchy
FTDistribution1DVoigt(omega, eta)

{{< /highlight >}}

The parameter `omega` is used to set the half-width of the distribution in nanometers. In the case of the pseudo-Voigt distribution an additional dimensionless parameter `eta` is used to balance between the Gaussian and Cauchy profiles.

### Domain size

The interference function of a radial paracrystal provides a way to calculate the scattering from a finite portion of the paracrystal using the `setDomainSize`(nm) method. The resulting behaviour is similar to the case when `damping_length` is used (the difference in computation is explained in the user manual). In the code snippet below, the paracrystal is created without specifying the `damping_length`, and then the `setDomainSize` method is used to introduce the alternative mechanism for finite size corrections.

{{< highlight python >}}

iff = InterferenceFunctionRadialParacrystal(10.0*nm)
iff.setProbabilityDistribution(FTDistribution1DCauchy(30.0*nm))
iff.setDomainSize(10000*nm)

{{< /highlight >}}

### Particle density

During the simulation setup the particle density has to be explicitely specified by the user for correct normalization of overall intensity. This is done by using `ParticleLayout.setParticleDensity(density)` method. The density parameter is given here in "number of particles per square nanometer".

### Size space coupling

To be written

### Complete example

In the example below we collect together all the code related to the initialization of the interference function of a radial paracrystal.

{{< highlight python >}}

cylinder = ba.Particle(material, ba.FormFactorCylinder(5*nm, 5*nm))
interference = ba.InterferenceFunctionRadialParaCrystal(20.0*nm, 1e3*nm)
pdf = ba.FTDistribution1DGauss(7 * nm)
interference.setProbabilityDistribution(pdf)
# interference.setDomainSize(10000*nm)

layout = ba.ParticleLayout()
layout.addParticle(cylinder)
layout.setInterferenceFunction(interference)
layout.setParticleDensity(0.0001)

{{< /highlight >}}

The complete example can be found [here]({{% ref-example "interference-functions/interference-1d-radial-paracrystal" %}}).

### Radial paracrystal in GUI.

To Initialize InterferenceFunctionRadialParacrystal in the graphical user interface, the corresponding object has to be connected with ParticleLayout and the corresponding parameters (PeakDistance, DampingLength and parameters of probability density function) have to be adjusted in the property editor.

{{< figscg src="tutorial_interference_para1d_gui.png" width="800px" class="center">}}
