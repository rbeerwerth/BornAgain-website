+++
title = "Working with sample parameters"
weight = 30
+++

### Working with sample parameters

This example shows how to get an access to sample structure information and how to manipulate
sample parameters on already constructed sample. This can be useful for debugging and for quick simulations.

In BornAgain a sample is described by a hierarchical tree of objects.
For example, the tree representing a multilayer can be printed in a Python session by running.

{{< highlight python>}}

print(sample.treeToString())

{{< /highlight >}}

with subsequent output

```bash
MultiLayer ('CrossCorrelationLength':0 'ExternalFieldX':0 'ExternalFieldY':0 'ExternalFieldZ':0)
    Layer0
        ParticleLayout ('TotalParticleDensity':1)
            Particle0 ('Abundance':0.5 'PositionX':0 'PositionY':0 'PositionZ':0)
                Cylinder ('Radius':5 'Height':5)
            Particle1 ('Abundance':0.5 'PositionX':0 'PositionY':0 'PositionZ':0)
                Prism3 ('BaseEdge':5 'Height':5)
            InterferenceNone
    LayerInterface
    Layer1
```

The top MultiLayer object is composed of three children, namely Layer #0, Layer Interface #0 and <nobr>Layer #1</nobr>. 
The children objects might themselves also be decomposed into tree-like structures. 
For example, Layer #0 contains a ParticleLayout object, which holds information related to the two
types of particles populating the layer. All numerical values used during the sample construction (thickness of layers, size of particles, etc.) are part of the 
same tree structure. These values are registered in the sample parameter pool using the name composed of the corresponding nodes’ names.
A list of the names and values of all registered sample’s parameters can be displayed using the command

{{< highlight python "linenos=table,linenostart=66">}}

print(sample.parametersToString())

{{< /highlight >}}

The output will be:

```bash
'/MultiLayer/CrossCorrelationLength':0
'/MultiLayer/ExternalFieldX':0
'/MultiLayer/ExternalFieldY':0
'/MultiLayer/ExternalFieldZ':0
'/MultiLayer/Layer0/ParticleLayout/TotalParticleDensity':1
'/MultiLayer/Layer0/ParticleLayout/Particle0/Abundance':0.5
'/MultiLayer/Layer0/ParticleLayout/Particle0/PositionX':0
'/MultiLayer/Layer0/ParticleLayout/Particle0/PositionY':0
'/MultiLayer/Layer0/ParticleLayout/Particle0/PositionZ':0
'/MultiLayer/Layer0/ParticleLayout/Particle0/Cylinder/Radius':5
'/MultiLayer/Layer0/ParticleLayout/Particle0/Cylinder/Height':5
'/MultiLayer/Layer0/ParticleLayout/Particle1/Abundance':0.5
'/MultiLayer/Layer0/ParticleLayout/Particle1/PositionX':0
'/MultiLayer/Layer0/ParticleLayout/Particle1/PositionY':0
'/MultiLayer/Layer0/ParticleLayout/Particle1/PositionZ':0
'/MultiLayer/Layer0/ParticleLayout/Particle1/Prism3/BaseEdge':5
'/MultiLayer/Layer0/ParticleLayout/Particle1/Prism3/Height':5
```

These values can be accessed/changed during run time. For example, the height of the cylinders populating
the first layer can be changed from the current value of 5 nm to 10 nm by running the command

{{< highlight python "linenos=table,linenostart=80">}}

sample.setParameterValue(
        "/MultiLayer/Layer0/ParticleLayout/Particle0/Cylinder/Height",
        10.0*nm)

{{< /highlight >}}

Wildcards `*` can be used to reduce typing or to work on a group of parameters. In the example below, the first command will change the height of all cylinders in the same way,
as in the previous example.

{{< highlight python "linenos=table,linenostart=97">}}

sample.setParameterValue("*/Cylinder/Height", 10.0*nm)

{{< /highlight >}}

The line below will change simultaneously both, the height and the half-side length of prisms.

{{< highlight python "linenos=table,linenostart=98">}}

sample.setParameterValue("*/Prism3/*", 10.0*nm)

{{< /highlight >}}

Example below demonstrates how to create a sample with fixed parameters and then change these parameters on the fly during runtime. 
Four simulations are performed one after another. Parameters of the sample are adjusted in between using different matching criteria.

{{< galleryscg >}}
{{< figscg src="SampleParametersIntro.png" width="600px" caption="Intensity images">}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/SimulationParameters.py" language="python" >}}
