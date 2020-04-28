+++
title = "Particle positioning"
weight = 35
+++

## Particle positioning

This tutorial demonstrates how to include particles in various layers of a multi-layer system.

As an example we are going to use simple spherical particles and a 3-layer system consisting 
of a semi-infinite air layer, a middle layer with finite thickness and a semi-infinite substrate layer.

### Creating particles

All particles implemented in BornAgain are defined by their form factors,
their sizes and the materials they are made of.
While placing particles in layers it is important to know
the reference point of the particle and how the coordinate system
of  the surrounding layer is defined. The coordinate system 
for a full sphere is shown below. For all implemented shapes,
please refer to the User Manual (section "Particle form factors").

{{< figscg src="tutorial_positioning_fullsphere.png" class="center">}}

The following code will create a spherical particle of 10 nm radius, made of a material whose refractive index roughly corresponds to silver at 1 Angstrom wavelength.

```python
radius = 10.0
material = HomogeneousMaterial("Ag", 1.245e-5, 5.419e-7)
particle = Particle(material, FormFactorFullSphere(radius))
```

### Adding particles to a layer

To add particles in a layer, a special `ParticleLayout` object has to be defined.
This object holds information about the particles populating the layer,
their densities and their interference function. In the following code snippet we add
spherical particles with all default parameters to the layout,
create the air layer and then add the layout to this air layer.

```python
layout = ParticleLayout()
layout.addParticle(particle)
 
air_layer = Layer(air_material)
air_layer.addLayout(layout)
```

The general syntax of the `ParticleLayout::addParticle` method is the following:

```python
addParticle(particle, abundance=1.0, position=kvector_t(0, 0, 0), rotation = None)
"""
Adds particle to the layout with abundance, position and rotation defined.
 
particle  : A particle to add to the layout
abundance : Proportion of this type of particles normalized to the total number of particles contained in this layout
position  : Relative position of the particle's reference point in the coordinate system of parent layer
rotation  : Rotation of particle
"""
```

In this tutorial we are going to focus on the particle's positioning,
leaving the rotation for the next tutorial.
The parameter `position = kvector_t(x, y, z)` defines the relative position of the particle's
reference point in the coordinate system of the parent object.
Note that the `(x,y)` components of the vector are only relevant for defining the relative position(s)
of two or more different particles in a layer, while `z`-component defines the vertical position of the particle inside the layer.

The plot below represents a multi-layer with 3 layers: a semi-infinite air layer, a middle layer with a finite thickness and a semi-infinite substrate layer.

{{< figscg src="tutorial_positioning_in_the_layer2.png" class="center">}}

For each of these 3 layers the z-axis is pointing up. For the air layer,
the `z=0.0` coordinate corresponds to the interface between air and middle layer.
To place a particle in the air layer, normally positive values `z>=0.0` should be used.
For the middle layer (or every intermediate layer if the number of layers above 3)
as well as for the substrate, `z=0.0` corresponds to the top interface.
To place a particle in one of such layers, normally negative values `z<=0.0` should be used.
The following code snippet explains how to place particles in 7 different cases, as shown on the plot.

```python
# Particle (A) is flying in the air at 10nm distance.
air_layout.addParticle(particle, 1.0, kvector_t(0, 0, 10.0))
 
# Particle (B) is in the air layer, sitting right on the interface.
air_layout.addParticle(particle, 1.0, kvector_t(0, 0, 0.0))
 
# Particle (C) is in the middle layer, touching the interface
middle_layout.addParticle(particle, 1.0, kvector_t(0, 0, -2.0*radius))
 
# Particle (D) is in the middle layer, right in the center
middle_layout.addParticle(particle, 1.0, kvector_t(0, 0, -thickness/2.-radius))
 
# Particle (E) is in the middle layer, touching the bottom interface.
middle_layout.addParticle(particle, 1.0, kvector_t(0, 0, -thickness))
 
# Particle (F) is in the substrate, touching the interface
substrate_layout.addParticle(particle, 1.0, kvector_t(0, 0, -2.0*radius))
 
# Particle (G) is in the substrate, the particle's reference point is at a depth of 20nm
substrate_layout.addParticle(particle, 1.0, kvector_t(0, 0, -20.0))
```

### Complete example

The following code defines a 3-layer system with a 100-nm-thick middle layer.
Spherical particles of 10 nm radius are placed right in the center of the middle layer.
This corresponds to Particle (D) from the snippet above.
Note that in order to build the sample, we assume
that there is no coherent interference between the waves scattered by these particles.

{{< highlight python "linenos=table">}}

mAmbience = HomogeneousMaterial("Air", 0.0, 0.0)
mMiddle= HomogeneousMaterial("Teflon", 2.900e-6, 6.019e-9)
mSubstrate = HomogeneousMaterial("Substrate", 3.212e-6, 3.244e-8)
mParticle = HomogeneousMaterial("Ag", 1.245e-5, 5.419e-7)
 
particle = Particle(mParticle, FormFactorFullSphere(10.0*nanometer))
 
layout = ParticleLayout()
layout.addParticle(particle, 1.0, kvector_t(0.0, 0.0, -60.0*nanometer)
 
air_layer = Layer(mAmbience)
 
middle_layer = Layer(mMiddle, 100.0*nanometer)
middle_layer.addLayout(layout)
substrate = Layer(mSubstrate)
 
multi_layer = MultiLayer()
multi_layer.addLayer(air_layer)
multi_layer.addLayer(middle_layer)
multi_layer.addLayer(substrate)

{{< /highlight >}}

### Alternative ways of positioning particles

The position of a particle can be adjusted using the Particle's own `Particle::setPosition` method.
The following three code blocks produce the same results.

```python
# setting Particle position via layout
particle = Particle(mParticle, FormFactorFullSphere(10.0*nanometer))
layout.addParticle(particle, 1.0, kvector_t(0.0, 0.0, -60.0*nanometer))
 
# setting particle position via particle interface
particle = Particle(mParticle, FormFactorFullSphere(10.0*nanometer))
particle.setPosition(kvector_t(0.0, 0.0, -60.0*nanometer))
layout.addParticle(particle, 1.0)
 
# setting particle position via particle interface, and then applying additional translation via layout
particle = Particle(mParticle, FormFactorFullSphere(10.0*nanometer))
particle.setPosition(kvector_t(0.0, 0.0, -30.0*nanometer))
layout.addParticle(particle, 1.0, kvector_t(0.0, 0.0, -30.0*nanometer))
```
