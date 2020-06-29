+++
title = "Reflectometry: Real life fitting"
weight = 40
+++

## Reflectometry: Real life fitting

In this example we are demonstrating how to perform in BornAgain a real-life reflectometry fitting job. To this fix ideas, we focus on fitting data from an X-ray reflectometer. The sample is composed of a thin silver nano-particle layer on top of a SiO2 layer and a silicon substrate. The nano-particle layer has negligible density and does not considerably affect the observed reflectometry signal.

The fitting proceeds as follows:

In a first stage, the whole range of experimental data is fitted and the data related to the instrument is fixed. Later on, only the right-hand part of the experimental data is fitted (i.e. the part of the reflectometry curve associated with bigger incident angles) and, finally, only the sample parameters are fitted. Only these last set of parameters affect the shape of the reflectometry curve at bigger incident angles.

A script performing this job is shown below in which the following parameters are fitted:

1. Beam intensity
2. Footprint correction factor
3. Beam angular divergence
4. Material concentration in the SiO2 layer
5. Thickness of SiO2 layer
6. Sample roughness


Be patient, since it takes some time to run.

{{% figure src="Figure.png" command="Resize" options="450x" caption="Figure obtained after running the script below" class="center" %}}


{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/specular/RealLifeReflectometryFitting.py" language="python" >}}

{{% filelink file="/static/files/python/fitting/ex03_ExtendedExamples/specular/mg6a_Merged.txt.gz" name="Reference data" %}}

