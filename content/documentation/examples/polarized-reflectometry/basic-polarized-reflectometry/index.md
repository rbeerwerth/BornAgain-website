+++
title = "Basic polarized reflectometry"
weight = 10
+++

### Specular reflectometry with polarized neutrons and a magnetic sample

This example shows how to perform a specular reflectometry simulation with polarized neutrons.
We show this for a sample that contains only a single magnetic layer on top of a substrate.
The magnetization and polarization are chosen to be (anti-)parallel, and hence, no
spin-flip is observed.
By rotation of either the magnetization or the polarization vector, one can generalize this example
to observe also the [spin-flip channels]({{% ref-example "polarized-reflectometry/polarized-spin-flip" %}}).

The construction of the sample is almost identical to the unpolarized cases, where the only difference is that the magnetization of a material can be specified:
{{< highlight python>}}
m_layer_mat = ba.MaterialBySLD("Layer", 1e-4, 1e-8,
                               ba.kvector_t(0, 1e8, 0))
{{< /highlight >}}
Here, we create a material with the usual specification of a name and the real and complex 
parts of the SLD.
In addition, the last argument defines the magnetization vector.
For this example, we chose a magnetization of magnitude $10^8 \text{A/m}$ along the positive $y$-axis.


In contrast to a normal unpolarized computation, the incoming beam polarization
as well as the analyzer must be specified when creating the simulation.
The polarization state of the incoming beam can be specified as follows:
{{< highlight python>}}
polarization = ba.kvector_t(0, 1, 0)
simulation.setBeamPolarization(polarization)
{{< /highlight >}}
Its polarization direction is specified as a regular Bloch vector on or inside the unit sphere.
Magnitudes of the Bloch vector smaller than one denote non-perfect polarization. 


The analyzer properties are similarly set:
{{< highlight python>}}
analyzer = ba.kvector_t(0, 1, 0)
simulation.setAnalyzerProperties(analyzer, 1.0, 0.5)
{{< /highlight >}}
The first argument specifies the direction of the analyzer, again by providing a 
Bloch vector with unit length. 
The second argument specifies the efficiency (magnitude of the Bloch vector). 
The third argument is the transmission of the analyzer, here $0.5$ corresponds to a perfect 
analyzer: half of an unpolarized incoming beam is not transmitted.
Therefore, this example corresponds to a perfect analyzer that is configured to probe 
the up-up channel.

In this example, setting up the beam polarization and the analyzer is done in the 
`run_simulation` function.
In order to simulate the two non-spin-flip channels (up-up and down-down), we have to perform the two calls

{{< highlight python>}}
results_pp = run_simulation(ba.kvector_t(0,  1, 0),
                            ba.kvector_t(0,  1, 0))
results_mm = run_simulation(ba.kvector_t(0, -1, 0),
                            ba.kvector_t(0, -1, 0))
{{< /highlight >}}


The resulting reflectivities are shown in this plot:

{{< galleryscg >}}
{{< figscg src="BasicPolarizedReflectometry.png" width="650px" caption="Reflectivity">}}
{{< /galleryscg >}}

As expected, we find the birefringent behavior and two different critical angles.
Since the magnetization of the layer is parallel to the neutron polarization, 
no spin-flip is observed. 
It is a good exercise to verify this claim by a short computation.

Here is the complete example:

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/BasicPolarizedReflectometry.py"  language="python" >}}

