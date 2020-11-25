+++
title = "Reflectometry: Fit Pt layer"
weight = 50
+++

### Reflectometry: Fit Pt layer



In this example, we want to demonstrate how to fit experimental reflectivity data
that was obtained by a time-of-flight experiment with unpolarized neutrons.
The sample is a roughly 50&nbsp;nm thick platinum layer on top of a silicon substrate.

The experiment was performed by M. Fitzsimmons et al., and the resulting data is 
published in [this repository](https://doi.org/10.5281/zenodo.4072376).



#### Fit model

We describe the above experiment by a three-layer model, where as usual the top layer is 
the vacuum and the substrate layer is the silicon substrate.
On top of the silicon substrate, we place the platinum layer.
The materials of both layers are described by their SLD, where we use literature values
for both silicon as well as platinum and keep them constant throughout the fitting procedure.


The main parameters of the sample are stored in dictionary, where they are defined by a unique `name`
and the following six parameters are utilized:

* Beam intensity: `intensity`

  We explicitly fit the beam intensity, in order to compensate for possible experimental errors
  and to circumvent problems with the rather large variance in the reflectivity data at low $Q$-values. 

* Roughness on top of the Pt layer: `r_pt/nm`

* Roughness on top of the Si substrate: `r_si/nm`

* Thickness of the Pt layer: `t_pt/nm`

* The relative $Q$-resolution: `q_res/q` ([c.f.]({{% ref-example "reflectometry/tofr-with-resolution" %}}))

* A $Q$-offset: `q_offset`

  This global offset is introduced to account for uncertainties in the angle at which the measurement is performed.


Due to saturation of the detector it is possible that the intensity at low $Q$-values (i.e. at high count rates) 
is underestimated. 
Furthermore, there is a rather large variance in the data that also leads to a rather bad fit in this region.
Therefore, we neglect the data in the low $Q$-region by choosing a cutoff at $Q_{\text{min}} = $&nbsp;0.18.
This value is selected by hand after performing several fits and visually selecting a good result.

##### $Q$-offset

Currently, BornAgain does not have an API support for an offset of the $Q$-axis.
Therefore, we need to shift the $Q$-axis before performing a simulation
{{< highlight python>}}
q_axis = q_axis + parameters["q_offset"]
{{< /highlight >}}

This shift then needs to be counter-transformed when returning the results in the `qr(result)` function
{{< highlight python>}}
q = numpy.array(result.result().axis(ba.Axes.QSPACE)) - q_offset
{{< /highlight >}}

##### Initial parameters

In order to successfully fit this example, we chose some sane starting values and 
the example code, that is fully given below, can be run with the following command:
{{< highlight python>}}
python3 Pt_layer_fit.py fit
{{< /highlight >}}
This performs a simulation with the initial parameters and yields the following result:

{{< galleryscg >}}
{{< figscg src="Pt-Layer-initial.png" width="550px" caption="Reflectivity with the initial parameters before fitting">}}
{{< /galleryscg >}}

Immediately afterwards the fit is performed.


#### Fit result


In order to run the fitting procedure, the following command can be issued:

{{< highlight python>}}
python3 Pt_layer_fit.py fit
{{< /highlight >}}

We need to allow a few seconds computational time and BornAgain should compute the following result

{{< galleryscg >}}
{{< figscg src="Pt-Layer-final.png" width="550px" caption="Reflectivity with the parameters obtained from our fit">}}
{{< /galleryscg >}}


If the `fit` keyword is omitted from the command line
{{< highlight python>}}
python3 Pt_layer_fit.py
{{< /highlight >}}
a simulation is performed with our fit results and one should obtain the result shown above.



{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/pt-layer/Pt_layer_fit.py" language="python" >}}

{{% filelink file="/static/files/python/fitting/ex03_ExtendedExamples/pt-layer/RvsQ_36563_36662.txt.gz" name="Reference data" %}}

