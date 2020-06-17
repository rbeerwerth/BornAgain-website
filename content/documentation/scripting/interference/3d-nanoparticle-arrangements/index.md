+++
title = "3D particle assemblies"
weight = 55
+++

# 3D Particle Assemblies

3D nanoparticle arrangements obtained using different techniques are complex, but quite frequent kinds of samples being studied with GISAS. Depending on the properties of the particular sample you may choose one of 2 ways to represent a 3D particle arrangement in a BornAgain simulation:

- [Particle compositions arranged in a lattice]({{% relref "#pcomposition" %}})
- [Mesocrystal]({{% relref "#mesocrystal" %}})

Below you will find a detailed description of each option.

{{< notice note >}}
For simplicity this tutorial uses a spherical detector. This is a good approximation, but for the real-life cases we recommend to use rectangular detectors. See the [Detector types]({{% relref "documentation/scripting/detectors" %}}) tutorial for detailed explanations about various detector types in BornAgain.

We also neglect [detector resolution]({{% relref "documentation/examples/beam-and-detector/detector-resolution" %}}) and [beam divergence]({{% relref "documentation/examples/beam-and-detector/beam-divergence" %}}) in this tutorial. However, we recommend to consider them if you want to compare simulation results to experimental data.

All Python code in this tutorial assumes **Python3** and may not work with Python2.
{{< /notice >}}

## Particle compositions arranged in a lattice
{{% anchor "pcomposition" %}}

{{< figscg src="3d_np_view.png" class="center">}}

Let's take a case of spherical particles arranged in a cubic lattice with the following parameters:
```python
particle_radius = 2.5*nm
lattice_length = 10.0*nm
height = 50.0*nm
```

One can easily create such a structure either in GUI or in Python using the following steps:

**Create a particle composition**

```python
# Defining Form Factors
ff_sphere = ba.FormFactorFullSphere(particle_radius)

# Defining composition of particles at specific positions
particle_composition = ba.ParticleComposition()

# compute number of particles in the vertical direction
n = int((height - 2.0*particle_radius) // lattice_length)

# add particles to the particle composition
for i in range(n+1):
    particle = ba.Particle(m_particle, ff_sphere)
    particle_position = kvector_t(0.0*nm, 0.0*nm, i*lattice_length)
    particle.setPosition(particle_position)
    particle_composition.addParticle(particle)
```

If you work in GUI, you will need to add each particle manually. See the [Particle composition]({{% relref "documentation/scripting/particles/particle-composition" %}}) tutorial for more details.

**Arrange created compositions in a lattice.**

For this example we will use a 2D square lattice.

```python
# Defining Interference Function
interference = ba.InterferenceFunction2DLattice(lattice_length, lattice_length, 90.0*deg, 0.0*deg)
interference_pdf = ba.FTDecayFunction2DCauchy(500.0*nm, 500.0*nm, 0.0*deg)
interference.setDecayFunction(interference_pdf)

# Defining Particle Layout and adding Particles
layout = ba.ParticleLayout()
layout.addParticle(particle_composition, 1.0)
layout.setInterferenceFunction(interference)
```

See the [Interference functions]({{% relref "documentation/scripting/interference" %}}) tutorial for more details on interference functions available in BornAgain.

### Disorder

Perfectly ordered nanoparticle arrangements are rare. For better match between simulated and experimentally observed GISAS patterns, you may wish to introduce some disorder. The most frequent kinds of disorder for nanoparticle arrangements are:

- Position variance and
- Rotational distribution

**Position variance**

{{< galleryscg >}}
{{< figscg src="3d_np_gisas.png" width="350px" caption="No position variance">}}
{{< figscg src="3d_np_gisas_posvar.png" width="350px" caption="Position variance 0.3 nm$^2$">}}
{{< /galleryscg >}}

Position variance characterizes the uncertainty of the particle position in the lattice. It will broaden and smear out the interference peaks as shown in the example figure above.

{{< notice note >}}
Pay attention, that in this case the whole particle composition is considered as a single "particle". Thus, position variance is only in **2D**. Be sure that this is the desired behavior for the system you simulate.
{{< /notice >}}

 You can set the position variance using the following Python code:

```python
interference.setPositionVariance(var)
```

where `var` is a floating point number. More details you will find in the [2D lattice]({{% relref "documentation/scripting/interference/lattice2d" %}}) tutorial.

**Rotational distribution**

Often, the particle arrangement over the sample is not uniform, but consists of domains rotated with respect to each other. This will influence the number and positions of interference peaks in the observed GISAS pattern.

If you assume a uniform rotational distribution of the domains, you can consider it in the simulation using the following Python code:

```python
interference.setIntegrationOverXi(True)
```

or by activating a corresponding checkbox in the GUI. Pay attention, this setting **will slow down the simulation dramatically**.

If you suggest that domains in your sample have a preferred orientation, you can create the rotational distribution manually. For this purpose you will need to modify the Python code as follows. First, we introduce the lattice rotations dictionary

```python
# lattice rotations dictionary, consists of pairs "xi: weight"
# sum of the weights must be less or equal to 1
rotations = {0.0: 0.7, 45.0: 0.3}
```

In this example we consider two lattice rotations: $\xi=0^{\circ}$ with weight 0.7 and $\xi=45^{\circ}$ with weight 0.3. Pay attention, BornAgain requires that the **sum of layout weights to be less than or equal to 1**. To add these layouts to the multilayer, we modify the Python code as follows:

```python
for xi in rotations.keys():
    # Defining Interference Function
    interference = ba.InterferenceFunction2DLattice(lattice_length, lattice_length, 90.0*deg, xi*deg)
    interference_pdf = ba.FTDecayFunction2DCauchy(500.0*nm, 500.0*nm, 0.0*deg)
    interference.setDecayFunction(interference_pdf)

    # Defining Particle Layout and adding Particles
    layout = ba.ParticleLayout()
    layout.addParticle(particle_composition, 1.0)
    layout.setInterferenceFunction(interference)
    layout.setWeight(rotations[xi])

    # Adding layouts to layers
    l_air.addLayout(layout)
```

In the GUI you should create and add all the layouts manually. This approach makes sense if you have just a few rotations.

{{< galleryscg >}}
{{< figscg src="3d_np_gisas_integration_over_xi.png" width="350px" caption="Uniform rotational distribution">}}
{{< figscg src="3d_np_gisas_latrot.png" width="350px" caption="Two lattice rotation angles">}}
{{< /galleryscg >}}

Figures above show the influence of both considered rotational distributions on the GISAS pattern.

Alternatively, you can consider to use distributions available in BornAgain. See the [Particle distribution]({{% relref "documentation/scripting/particles/particle-distribution" %}}) tutorial for more information. Pay attention, that in this case you should apply the chosen distribution to the parameter `Interference2DLattice/BasicLattice/Xi`. See the corresponding [tutorial example]({{% relref "documentation/examples/interference-functions/interference-2d-lattice-sum-of-rotated" %}}) for details.

If your particle composition is not symmetrical, you may need to rotate your particles as well. See the [Particle rotation]({{% relref "documentation/scripting/particles/particle-rotation" %}}) tutorial for details.

Complete Python scripts for this part of tutorial

* {{< icon fa-save fa-lg  fa-fw>}} <a href="particle_composition.py">particle_composition.py</a>
* {{< icon fa-save fa-lg  fa-fw>}} <a href="particle_composition_rotational_distribution.py">particle_composition_rotational_distribution.py</a>


## Mesocrystal
{{% anchor "mesocrystal" %}}

{{< figscg src="meso_view.png" class="center">}}

Another and more flexible way to represent a 3D particle arrangement is as a **mesocrystal**. It can be easily created in both, GUI and Python. The complete Python script to create a mesocrystal you can find in the [Mesocrystal]({{% relref "documentation/examples/complex-shapes/meso-crystal" %}}) tutorial example.

In the present tutorial, we consider a mesocrystal with the following parameters

```python
# parameters of 3D particle arrangement
particle_radius = 2.50*nm
lattice_length = 10.0*nm

# mesocrystal size
meso_height = 50.0*nm
meso_width = 500.0*nm
meso_length = 500.0*nm
```

Mesocrystal can be created in the following steps.

**Create particles that form the base of the mesocrystal**

```python
# Spherical particles, form the base of the mesocrystal
ff_sphere = ba.FormFactorFullSphere(particle_radius)
sphere = ba.Particle(m_particle, ff_sphere)
```

**Create lattice**

```python
# mesocrystal lattice (cubic lattice for this example)
lattice_a = ba.kvector_t(lattice_length, 0.0, 0.0)
lattice_b = ba.kvector_t(0.0, lattice_length, 0.0)
lattice_c = ba.kvector_t(0.0, 0.0, lattice_length)
lattice = ba.Lattice(lattice_a, lattice_b, lattice_c)
```

**Create a mesocrystal**

```python
# crystal structure
crystal = ba.Crystal(sphere, lattice)

# mesocrystal
meso_ff = ba.FormFactorBox(meso_length, meso_width, meso_height)
meso = ba.MesoCrystal(crystal, meso_ff)

layout = ba.ParticleLayout()
layout.addParticle(meso)
```

### Size of the mesocrystal

The size of the mesocrystal influences the GISAS pattern dramatically. This is especially well seen for small mesocrystals. Unless you know size of your mesocrystals from other techniques, we recommend to vary it to find the one that matches the experimental data the best.

{{< galleryscg >}}
{{< figscg src="meso_box_w050nm.png" width="350px" caption="Mesocrystal of $W=L=50$ nm">}}
{{< figscg src="meso_box_w100nm.png" width="350px" caption="Mesocrystal of $W=L=100$ nm">}}
{{< figscg src="meso_box_w250nm.png" width="350px" caption="Mesocrystal of $W=L=250$ nm">}}
{{< figscg src="meso_box_w500nm.png" width="350px" caption="Mesocrystal of $W=L=500$ nm">}}
{{< /galleryscg >}}

In the figures above, you can see the GISAS pattern for a Box-shaped mesocrystal of different sizes in lateral direction. For simplicity, we take width $W$ and length $L$ of the mesocrystal equal. As you can see, small mesocrystals cause a lot of peaks coming from the mesocrystal shape. These peaks "vanish" for large mesocrystals, because the intensity starts to oscillate so fast, that we are not able anymore to observe them. You can also see, that the shape of the "structure" peaks is also affected.

{{< notice note >}}
Pay attention, that instrument resolution and beam divergence can smear out the observed peaks even for smaller mesocrystals.
{{< /notice >}}

### Shape of the mesocrystal

The shape of the mesocrystal is also a very important parameter that influences the GISAS pattern. To vary the shape you can choose any of the particle form factors available in BornAgain. See the example on available [particle form factors]({{% relref "documentation/examples/embedded-particles/all-formfactors" %}})

{{< galleryscg >}}
{{< figscg src="meso_cylinder.png" width="350px" caption="Cylinder">}}
{{< figscg src="meso_truncated_sphere.png" width="350px" caption="Truncated Sphere">}}
{{< figscg src="meso_gauss.png" width="350px" caption="Gauss">}}
{{< figscg src="meso_lorentz.png" width="350px" caption="Lorentz">}}
{{< /galleryscg >}}

The figures above show the GISAS patterns for different shapes of mesocrystals. The width of all mesocrystals is $100$ nm. Form factors `FormFactorGauss` and `FormFactorLorentz` are presently not available in GUI. However, they can be used from Python:

```python
meso_ff = ba.FormFactorGauss(meso_width, meso_height)
```

or

```python
meso_ff = ba.FormFactorLorentz(meso_width, meso_height)
```

### Position variance

Position variance describes the displacement of the nanoparticle around the lattice point in **3D**. The larger the position variance, the stronger will be the attenuation of the peak intensity along $Q_z$. This can be seen in the figures below.

{{< galleryscg >}}
{{< figscg src="meso_dw_01.png" width="350px" caption="Position variance $0.1$ nm$^2$">}}
{{< figscg src="meso_dw_05.png" width="350px" caption="Position variance $0.5$ nm$^2$">}}
{{< figscg src="meso_dw_1.png" width="350px" caption="Position variance $1$ nm$^2$">}}
{{< figscg src="meso_dw_2.png" width="350px" caption="Position variance $2$ nm$^2$">}}
{{< /galleryscg >}}

This setting is presently not available in GUI. It can be used from Python as follows

```python
crystal = ba.Crystal(sphere, lattice)
# crystal.setDWFactor(0.5)  # for BornAgain versions 1.16 and below
crystal.setPositionVariance(0.5)  # for newer BornAgain versions
```

### Interference function

While representing a 3D nanoparticle arrangement as a mesocrystal, you might come up with a question whether you need an interference function. The answer depends on the size of your mesocrystal, distance between mesocrystals and resolution of the instrument where the measurements are performed.

Let's take the mesocrystal of width $W=100$ nm and distance between two mesocrystals $D=300$ nm. In this case, to be able to resolve interference peaks you will need an instrument resolution of at least:

$$\Delta Q = \frac{2\pi}{300}\approx\\;0.02\\; nm^{-1} \approx \\; 0.002 \\; \unicode{x212B}^{-1}$$


## Large particles (aliasing problem)

Often you need rather large mesocrystals to represent a 3D nanoparticle arrangement. In this case, the intensity will oscillate over each detector bin with high frequency. Thus, the analytical computation with sampling points in the bin centers will cause artifacts in the simulated GISAS pattern. This is shown in the figures below.

{{< galleryscg >}}
{{< figscg src="meso_box_w500nm_nomc.png" width="350px" caption="Analytical computation">}}
{{< figscg src="meso_box_w500nm.png" width="350px" caption="Monte-Carlo integration">}}
{{< /galleryscg >}}

The way to avoid this problem implemented in BornAgain is Monte-Carlo integration over the detector bin. You can switch it on in both, GUI (checkbox in the `Simulation` view) and in Python

```python
simulation.getOptions().setMonteCarloIntegration(True, n)
```

where `n` is a number of points for Monte-Carlo integration. For more details see the [Large particle formfactor]({{% relref "documentation/examples/complex-shapes/large-particles-formfactor" %}}) tutorial.


Download the complete Python script {{< icon fa-save fa-lg  fa-fw>}} <a href="mesocrystal.py">mesocrystal.py</a>

## Diffuse scattering

Besides of Bragg peaks, measured GISAS patterns often contain diffuse scattering. This is a sign of some kind of disorder in the sample. Which kind of disorder it is exactly, depends on the sample production technique. Here we can list some frequent types:

* **Loose nanoparticles.** This is frequent for self-assembled 3D nanoparticle arrangements. These nanoparticles can also have size distributions or a positional distribution along the $Z$ axis (`PositionZ`). To add loose particles, you will need to create a separate `ParticleLayout` and add it to the same layer as the mesocrystal with an appropriate weight.  For more information about particle distributions, see the [particle distribution]({{% relref "documentation/scripting/particles/particle-distribution" %}}) tutorial.

{{< notice note >}}
Pay attention, that relative weights of layouts as well as `TotalParticleSurfaceDensity` in each layout will affect the relative scattering intensities caused by particles of each particle layout. You can set these parameters either in GUI or using the following Python code

```python
layout = ba.ParticleLayout()
layout.addParticle(meso)
layout.setTotalParticleSurfaceDensity(1.0e-04)    # or any other reasonable number between 0 and 1
layout.setWeight(0.5)                             # or any other reasonable number between 0 and 1
```
{{< /notice >}}

*  **Rotational distribution** can cause smearing out and displacement of Bragg peaks. You can easily rotate a mesocrystal in GUI by applying `Rotation` as `transformation`. In Python, you would need to use the following code

```python
meso = ba.MesoCrystal(crystal, meso_ff)
meso_rotation = ba.RotationZ(45.0*deg)
meso.setRotation(meso_rotation)
```
This example rotates the mesocrystal around $Z$ axis by 45 degrees. You can also apply a rotational distribution in a way similar to the one described above in the [Particle compositions arranged in a lattice]({{% relref "#pcomposition" %}}) section.

* **Interface roughness** influences the peak intensities. See the tutorial example on [correlated roughness]({{% relref "documentation/examples/layered-structures/correlated-roughness" %}}) for more details about interface roughness.

{{< notice note >}}
Pay attention, the more disorder you add to your sample model, the more **slow and resource-consuming** will be the simulation.
{{< /notice >}}


## General recommendations

* Start with a simplest model. If you have simple and well-ordered system, use `particle composition`. If you observe signs of disorder in experimental data, use `mesocrystal`. Important is at first to build a simplest possible model that matches peak positions.

* If you have heterogeneous nanoparticle arrangements, first check the contrast of all the particles to the medium. If the SLD of some particles does not differ noticeably from the ambient SLD, don't simulate them. It will allow for a simpler model and will save you computation time. The same approach we recommend for core-shell particles.

* If a simulation does not reproduce all the peaks observed in experimental data, try to add a rotational distribution. For the beginning keep it as simple as possible.

* If particles in 3D arrangements are densely packed, use averaged materials. It might have a strong influence on the GISAS pattern in the range of small $Q_z$. This can be done either by choosing `Average Layer Material` in `Simulation` view in GUI or with the following Python code:

```python
simulation.getOptions().setUseAvgMaterials(True)
```

See also tutorial examples on [Hemispheres in Averaged Layer]({{% relref "documentation/examples/miscellaneous/half-spheres-in-average-top-layer" %}}) and [Cylinders in Averaged Layer]({{% relref "documentation/examples/miscellaneous/cylinders-in-average-layer" %}}).

* Peak shapes and intensities can be influenced by a lot of different parameters, starting from disorder in 3D particle arrangement and finishing by instrument resolution, beam divergence and background. To find out which factor is important for your case, you should investigate the influence of each of them one by one.


## Exercise

Find appropriate sample and instrument parameters to match the simulation with the fake experimental data presented in the figure below

{{< figscg src="meso_4plots.png" class="center">}}

Download files needed to produce this image:

* {{< icon fa-save fa-lg  fa-fw>}} <a href="mesocrystal_4plots.py">mesocrystal_4plots.py</a>

* {{< icon fa-save fa-lg  fa-fw>}} <a href="fake_data.npy">fake_data.npy</a>
