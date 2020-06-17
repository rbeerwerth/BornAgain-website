+++
title = "Considering uncertainties"
weight = 40
+++

## Taking uncertainties into account


In this example we are demonstrating how to allow for uncertainties during a Reflectometry fitting job. The sample to fit consists of twenty Titanium-Nickel bilayers. Assuming that all Titanium layers have the same thickness, the goal is to find that thickness.

The reference data was generated with GENX, setting the thickness of the Ti layers equal to 3 nm.

This example follows closely the tutorial on [Fitting reflectometry data](/documentation/examples/fitting/extended/fit-specular-data/). The main points to focus on here are the following: 

 - Added artificial uncertainties to the data being fitted
 - Use of the the $RQ^4$ view for plotting
 - Use of $\chi^2$ with $L_1$ normalization as the objective metric
 - Setting a genetic algorithm as the minimizer


{{% figure src="FitWithUncertainties.png" command="Resize" options="450x" caption="Fitting with uncertainties plot. Notice the $RQ^4$ scale of the Intensity axis" class="center" %}}

{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/specular/FitWithUncertainties.py" language="python" >}}

{{% filelink file="/static/files/python/fitting/ex03_ExtendedExamples/specular/genx_interchanging_layers.dat.gz" name="Reference data" %}}


