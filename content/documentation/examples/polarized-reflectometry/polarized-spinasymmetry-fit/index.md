+++
title = "Spin-Asymmetry Fit Example"
weight = 40
+++

### Fitting the Spin-Asymmetry Example from Nist

This example shows how to fit the parameters in the [spin-asymmetry example]({{% ref-example "polarized-reflectometry/polarized-spinasymmetry" %}}).

For this demonstration we choose initial parameters that are not too far from the fitting results. 
In particular, the magnetization is initially set to zero, such that the spin asymmetry identically vanishes.

With the initial parameters, we obtain:

{{< galleryscg >}}
{{< figscg src="SpinAsymmetryInitial1.png" width="350px" caption="Reflectivity">}}
{{< figscg src="SpinAsymmetryInitial2.png" width="350px" caption="Spin Asymmetry">}}
{{< /galleryscg >}}




#### Setup of the Fit

For fitting of reflectometry data covering several orders of magnitude use relative difference

$$\Delta = \frac{1}{N} \sum_{i = 1}^N \left( \frac{d_i - s_i}{d_i + s_i} \right)^2$$


This is supported by BornAgain by setting

{{< highlight python>}}
fit_objective.setObjectiveMetric("reldiff")
{{< /highlight >}}


The fitting of polarized reflectometry data proceeds similar to the lines presented in
[the tutorial on multiple datasets]({{% ref-example "fitting/advanced/multiple-datasets" %}}).
We need to add the reflectivity curves for the up-up and down-down channel 
to the fit objective:

{{< highlight python>}}
fit_objective.addSimulationAndData( SimulationFunctionPlusplus, 
                                                    rdata_pp, 1.0)
fit_objective.addSimulationAndData( SimulationFunctionMinusMinus, 
                                                    rdata_mm, 1.0)
{{< /highlight >}}

`SimulationFunctionPlusplus` and `SimulationFunctionMinusMinus` are two function objects that return a simulation result for 
the up-up and down-down channels, respectively.

The fit parameters are defined in the dictionary `startParams`, where they are defined as a triple of values `(start, min, max)`.
If no fit is performed the values obtained from our own fit are stored in `fixedParams` and are subsequently used
to simulate the system.

We want to fit the following parameters:

* `q_res`: Relative $Q$-resolution
* `q_offset`: Shift of the $Q$-axis.
* `t_Mafo`: The thickness of the layer
* `rhoM_Mafo`: The SLD of the layer
* `rho_Mafo`: The magnetic SLD of the layer
* `r_Mao`: The roughness on top of the substrate
* `r_Mafo`: The roughness on top of the magnetic layer


#### Fit Result

After running the fit using

{{< highlight python>}}
python3 PolarizedSpinAsymmetryFit.py fit
{{< /highlight >}}


we get the result

{{< galleryscg >}}
{{< figscg src="SpinAsymmetryFit1.png" width="350px" caption="Reflectivity">}}
{{< figscg src="SpinAsymmetryFit2.png" width="350px" caption="Spin Asymmetry">}}
{{< /galleryscg >}}


This result was already presented in the [spin-asymmetry]({{% ref-example "polarized-reflectometry/polarized-spinasymmetry" %}}) tutorial and 
can also be obtained by runnning the example without the fit option:

{{< highlight python>}}
python3 PolarizedSpinAsymmetryFit.py
{{< /highlight >}}


Here is the complete example:

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/PolarizedSpinAsymmetryFit.py"  language="python" >}}

