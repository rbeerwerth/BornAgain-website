+++
title = "Magnetic particles"
weight = 55
+++

## Magnetic particles

This tutorial demonstrates how to include particles with non-zero magnetization.

As an example we are going to use magnetic spherical particles embedded in the substrate of a simple 2-layer system. We will simulate this sample with a polarized beam and use polarization analysis to focus on the spin-flip channel.

### Creating materials with magnetization density

Magnetic materials in BornAgain are defined by their refractive index, as for non-mangetic materials, and the magnetization density vector, given in units of A/m. The following code first defines the magnetization density vector and then creates a material with this magnetization.

{{< highlight python >}}

# Magnetization of the particle's material (A/m)
magnetization_particle = ba.kvector_t(0.0, 0.0, 1e7)
particle_material = ba.HomogeneousMaterial("Particle", 2e-5, 4e-7,
                                           magnetization_particle)

{{< /highlight >}}

### Using the magnetic material for a particle

A magnetic material can be used just as a non-magnetic one when defining particles or layers. For the spherical particle of this example, we use the following code to define it.

{{< highlight python >}}

# spherical magnetic particle
sphere_ff = ba.FormFactorFullSphere(5*nm)
sphere = ba.Particle(particle_material, sphere_ff)

{{< /highlight >}}

### Defining a polarized beam and polarization analysis

When magnetic materials are present, some of the scattering may appear as spin-flip scattering. This contribution to the scattering can be isolated during an experiment by using a polarized beam and using polarization analysis at the detector.

The polarization state of the beam is fully defined by its Bloch vector, which points in the preferred direction of the neutron's spin and whose size determines if the neutron is in a mixed or pure state. In this example, we will define a pure state for the neutron, with spin pointing in the positive z-axis.

{{< highlight python >}}

# define the beam polarization state
beampol = ba.kvector_t(0.0, 0.0, 1.0)
simulation.setBeamPolarization(beampol)

{{< /highlight >}}

Polarization analysis is defined in BornAgain by the direction along which the spin will be analyzed, the efficiency of the analyzer and the total transmission.

In this example, we will define the analysis to be in negative z-direction to gain information on the spin-flip channel. We set the efficiency to 1 and the total transmission to 0.5.

{{< highlight python >}}

# define the polarization analysis properties
analyzer_dir = ba.kvector_t(0.0, 0.0, -1.0)
simulation.setAnalyzerProperties(analyzer_dir, 1.0, 0.5)

{{< /highlight >}}

### Complete example

The full example embeds the previously defined spherical particle inside the substrate and simulates the spin-flip channel along the z-axis.

{{< figscg src="MagneticSpheres.png" width="500px" class="center" caption="The figure shows the intensity map produced by the script below." >}}

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/MagneticSpheres.py" language="python" >}}
