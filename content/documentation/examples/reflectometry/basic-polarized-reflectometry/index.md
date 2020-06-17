+++
title = "Basic polarized reflectometry"
weight = 100
+++

### Specular Reflectometry with Polarized Neutrons and a Magnetic Sample

This example shows how to perform a specular reflectometry simulation with polarized neutrons.
We show this for a sample that contains only a single magnetic layer on top of a substrate.
The magnetization and polarization are chosen to be (anti-)parallel, and hence, no
spin-flip is observed.
By rotation of either the magnetization or the polarization vector, one can generalize this example
to observe also the spin-flip channels.

The construction of the sample is almost identical to the normal unpolarized cases, where the only difference is that the magnetization of a material can be specified:
{{< highlight python>}}
m_layer_mat = ba.MaterialBySLD("Layer", 1e-4, 1e-8,
                               ba.kvector_t(0.0, 1e8, 0.0))
{{< /highlight >}}
Here, we create a material with the usual specification of a name and the real and complex 
parts of the SLD.
In addition, the last argument defines the magnetization vector.
For this example, we chose a magnetization of magnitude $10^8 \text{A/m}$ along the positive $y$-axis.


In contrast to a normal unpolarized computation, the incoming beam polarization
as well as the analyzer must be specified when creating the simulation.
The polarization state of the incoming beam can be specified as follows:
{{< highlight python>}}
polarization = ba.kvector_t(0.0, 1.0, 0.0)
simulation.setBeamPolarization(polarization)
{{< /highlight >}}
Its polarization direction is specified as a regular Bloch vector on or inside the unit sphere.
Magnitudes of the Bloch vector smaller than one denote non-perfect polarization. 


The analyzer properties are similarly set:
{{< highlight python>}}
analyzer = ba.kvector_t(0.0, 1.0, 0.0)
simulation.setAnalyzerProperties(analyzer, 1.0, 0.5)
{{< /highlight >}}
The first argument specifies the direction of the analyzer, again by providing a 
Bloch vector with unit length. 
The second argument specifies the efficiency (magnitude of the Bloch vector). 
The third argument is the transmission of the analyzer, here $0.5$ corresponds to a perfect 
analyzer: half of an unpolarized incoming beam is not transmitted.
Therefore, this example corresponds to a perfect analyzer that is configured to probe 
the up-up channel.
Currently, non-perfect analyzers are not supported. Therefore, it is strongly advised to only 
change the analyzer direction and to leave all other values unaltered.

{{< galleryscg >}}
{{< figscg src="BasicPolarizedReflectometry.png" width="650px" caption="Intensity image">}}
{{< /galleryscg >}}

This plot shows the resulting reflectivity in the up-up and down-down channel.
As expected, we find the birefringent behavior and two different critical angles.
Since the magnetization of the layer is parallel to the neutron polarization 
no spin-flip is observed. 
It is a good exercise to verify this claim by a short computation.

{{< notice note >}}
Please note, currently, it is not supported to add rough interfaces to any sample that contains magnetic materials.
Support for structural rougness in polarized computations is anticipated for the next BornAgain release.
{{< /notice >}}

Here is the complete example:

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/BasicPolarizedReflectometry.py"  language="python" >}}

