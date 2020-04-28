+++
title = "Interference functions"
weight = 50
+++

## Interference functions

The interference function in BornAgain is a key component to organize in-plane order of nanoparticles.

The interference function, being assigned to a ParticleLayout object, defines the way the scattering from particles is evaluated.

{{< highlight python >}}

particle = Particle(material, FormFactorSphere(radius))
interference = YourInterferenceFunction()
 
layout = ParticleLayout()
layout.addParticle(particle)
layout.setInterferenceFunction(interference)

{{< /highlight >}}

For very dilute distributions of particles, the particles are too far apart from each other to lead to any interference between the waves scattered by each of them. In this case the interference function is equal to 1. The scattered intensity is then entirely determined by the form factors of the particles distributed in the sample. To achieve such setup, the user has to leave the interference function unspecified or use

{{< highlight python >}}

layout.setInterferenceFunction(InterferenceFunctionNone())

{{< /highlight >}}

For particles located at some regular intervals, two major cases are possible.

### The regular lattice

The particles are positioned at regular intervals generating a layout characterised by its base lattice vectors a and b (in direct space) and the angle between these two vectors. This lattice can be two or one-dimensional depending on the characteristics of the particles. For example when they are very long, the implementation can be simplified and reduced to a "pseudo" 1D system.

### Paracrystals

Similarly to the interference function of the lattice, paracrystals are used to model the scattering from particles positioned at some regular intervals on a plane. However, the paracrystal model posesses only short range order. The disorder is cumulative at further distance. Paracrystals are considered as a transition between the regular lattice and a fully disordered state.

The following sections provide specific guidance and practical details on each of the interference functions available in BornAgain.

{{% children  %}}

