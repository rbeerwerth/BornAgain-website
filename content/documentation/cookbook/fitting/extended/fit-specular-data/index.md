+++
title = "Fitting reflectometry data"
weight = 10
+++

### Fitting reflectometry data

In this example we will fit reflectometry data obtained from `GenX` for the sample
previously used in
[reflectometry simulation tutorial]({{% ref-tutorial "simulation-classes/reflectometry" %}}).

The only fitting parameter of the simulation considered here is the thickness of the Ti
layers. The reference data was obtained under the following assumptions:

* All Ti layers have the same thickness
* Thickness value was $3 \, nm$

{{< galleryscg >}}
{{< figscg src="fit-specular-data.png" width="600px" caption="Fit window">}}
{{< /galleryscg >}}

The fit view produced by running the fitting script is shown in the picture.
The right-hand part of the view contains information about the current iteration
of the fitting process, the maximum relative difference $d_{r, max}$ between the
reference and the simulated data, and the current values of the fitting parameters.

One should note that in the current example the `BornAgain` built-in fitting engine and
default minimizer (namely, `Minuit`) was used to fit the data.

The minimizer can be selected by the `setMinimizer` command:

```python
minimizer = ba.Minimizer()
minimizer.setMinimizer("Genetic", "", "MaxIterations=30")
```

This code snippet replaces the default `Minuit` minimizer with the `Genetic` one, which is
recommended to use for complicated multi-dimensional fitting tasks.

### Further topics

A much more sophisticated example of fitting experimental reflectometry data with
`BornAgain` and an external minimizer can be
found in `Examples/python/fitting/ex03_ExtendedExamples/specular/RealLifeReflectometryFitting.py`
in the BornAgain directory.

### Complete script and data

{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/specular/FitSpecularBasics.py" language="python" >}}

{{% filelink file="/static/files/python/fitting/ex03_ExtendedExamples/specular/genx_interchanging_layers.dat.gz" name="Reference data" %}}
