+++
title = "Particle composition"
weight = 45
+++

## Particle composition

This tutorial demonstrates how to construct complex shape particles.

All particles implemented in BornAgain are defined by their form factors,
their sizes and the materials they are made of.
The form factor library provides access to a list of about 20 elementary shapes.
A special `ParticleComposition` object allows to compose elementary particles into complex shapes
and treat the resulting object as a single particle:
it can be rotated, translated and included in the layer via a particle layout.
The scattering from such a particle will account for coherent interference between sub particles.

### Creating particle composition

The `ParticleComposition` object is created via one of its constructors.

```python
# creates an empty particle composition
composition = ParticleComposition()
 
# creates a composition made of a single particle at a given position
composition = ParticleComposition(particle, position = kvector_t(0,0,0))
 
# creates a composition and includes copies of a particle at specified positions
ParticleComposition(particle, positions = [pos1, pos2, ...])
```

The position of the particle defines the relative position
of the particle's reference point in the coordinate system of the particle composition.

`ParticleComposition` can be modified via following methods

```python
# add particle to the composition at specified position
composition.addParticle(particle, position = kvector_t(0,0,0))
 
# add copies of the particles at specified positions
composition.addParticles(particle, positions = [pos1, pos2, ...])
```

### Examples

In following plot we demonstrate the creation of 3 different compositions

{{< figscg src="tutorial_composition_examples.png" class="center">}}

The hollow cross-shape on the left is constructed by adding four copies of the same box
shaped particle at 4 different positions

```python
length, width, height = 10.0*nanometer, 10.0*nanometer, 3.0*nanometer
box = Particle(box_material, FormFactorBox(length, width, height))
 
positions = [kvector_t(length, 0, 0), kvector_t(0, -width, 0), kvector_t(-length, 0, 0), kvector_t(0, width, 0)]
composition = ParticleComposition(box, positions)
```

The stack of boxes at the center is constructed by placing 3 boxes made of different materials on top of each other.

```python
length, width, height = 10.0*nanometer, 10.0*nanometer, 5.0*nanometer
ff_box = FormFactorBox(length, width, height)
 
composition = ParticleComposition()
composition.addParticle(Particle(material1, ff_box), kvector_t(0, 0, 0))
composition.addParticle(Particle(material2, ff_box), kvector_t(0, 0, height))
composition.addParticle(Particle(material3, ff_box), kvector_t(0, 0, 2.0*height))
```

The full sphere on the right is composed of two truncated spheres,
each made of a different material. The bottom half is rotated first
by 180 degrees about the Y axis before adding it to the composition.

```python
radius = 16.0*nanometer
top_half = Particle(material1, FormFactorTruncatedSphere(radius, radius))
bottom_half = Particle(material2, FormFactorTruncatedSphere(radius, radius))
bottom_half.setRotation(RotationY(180.*degree))
 
composition = ParticleComposition()
composition.addParticle(top_half)
composition.addParticle(bottom_half)
```

### Positioning and rotation of a ParticleComposition

`ParticleComposition` object obeys the same rules as a `Particle`.
It's position and rotation can be changed through the `setPosition`, `applyTranslation`, `setRotation`, `applyRotation`
methods and it can be placed in a layer via `ParticleLayout`.

The plot below represents a 3 layer system with a 100-nm-thick middle layer.
A particle composition made of two semi-spheres is rotated by 90 degrees about the `Y`
axis and placed right at the center of the middle layer.
The corresponding Python code snippet follows.

{{< figscg src="tutorial-composition-in-the-layer.png" class="center" >}}

{{< highlight python "linenos=table">}}

# defining materials
mAmbience = HomogeneousMaterial("Air", 0.0, 0.0)
mMiddle= HomogeneousMaterial("Teflon", 2.900e-6, 6.019e-9)
mSubstrate = HomogeneousMaterial("Substrate", 3.212e-6, 3.244e-8)
mPart1 = HomogeneousMaterial("Part1", 1.245e-5, 5.419e-7)
mPart2 = HomogeneousMaterial("Part2", 1.245e-5, 5.419e-7)
 
# defining particle composition made of two half spheres
radius = 16.0*nanometer
top_half = Particle(mPart1, FormFactorTruncatedSphere(radius, radius))
bottom_half = Particle(mPart2, FormFactorTruncatedSphere(radius, radius))
bottom_half.setRotation(RotationY(180.*degree))
 
composition = ParticleComposition()
composition.addParticle(top_half)
composition.addParticle(bottom_half)
  
# building layers
air_layer = Layer(mAmbience)
 
thickness = 100*nanometer 
middle_layer = Layer(mMiddle, thickness)
layout = ParticleLayout()
layout.addParticle(composition, 1.0, kvector_t(0.0, 0.0, -thickness/2.),
                   RotationY(90.*degree))
middle_layer.addLayout(layout)
 
substrate = Layer(mSubstrate)
 
# building a multilayer 
multi_layer = MultiLayer()
multi_layer.addLayer(air_layer)
multi_layer.addLayer(middle_layer)
multi_layer.addLayer(substrate)

{{< /highlight >}}


