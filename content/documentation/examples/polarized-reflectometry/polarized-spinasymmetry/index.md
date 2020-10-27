+++
title = "Spin-Asymmetry Example"
weight = 40
+++

### Spin-Asymmetry Example from NIST
 
 
This example shows how to simulate the magnetic layer described on the NIST homepage in the [Magnetically Dead Layers in Spinel Films](https://www.nist.gov/ncnr/magnetically-dead-layers-spinel-films) example.
In particular, we want to show how to use BornAgain in order to simulate the spin asymmetry.
The sample simulated in this example is very similar to the previous examples introduced in this section.
It just consists of a magnetic layer on top of a substrate.
During these tutorial we neglect the magnetically dead layer that forms below the magnetic layer, as there is currently no API in BornAgain to support such a scenario out of the box.


In this first example, we utilize parameters that are deduced from a fit to the data provided on the Nist homepage.
How to perform the fit is described in the 
[extended example]({{% ref-example "polarized-reflectometry/polarized-spinasymmetry-fit" %}}).



#### Spin Asymmetry 


The spin asymmetry is defined as

$$S = \frac{R^{++} - R^{- -}}{R^{++} + R^{- -}}$$

Therefore, we only need to perform a normal polarized simulation for the up-up and down-down channels and then compute
the spin asymmetry.

Given the experimental data, the measured spin asymmetry is calculated in the same way.
In addition, the error is computed by:

$$\Delta S = \frac{\sqrt{ 4 {R^{++}}^2 \Delta {R^{- -}}^2 + 4 {R^{- -}}^2 \Delta {R^{++}}^2 }}{ \left( R^{++} + R^{- -}\right)^2 } $$

This is performed in the function `plotSpinAsymmetry`.



#### Further Corrections

We also apply a resolution correction, as described in the [ToF - Resolution effects]({{% ref-example "reflectometry/tofr-with-resolution" %}}) example.

Furthermore, we introduce an offest in the $Q$-axis, in order to accomodate for experimental uncertainties 
in the measurement of $\theta$.
For this purpose, the provided $Q$-axis is shifted in the function `get_simulation`:

{{< highlight python>}}
q_axis = q_axis + parameters["q_offset"]
{{< /highlight >}}



#### Data Processing

After loading the experimental data, we scale the q-axis in order to obtain inverse nm as are the default units in BornAgain.
Furthermore, the reflectivity data is scaled such that its maximum is unity


#### Simulation Result


{{< galleryscg >}}
{{< figscg src="SpinAsymmetry1.png" width="350px" caption="Reflectivity">}}
{{< figscg src="SpinAsymmetry2.png" width="350px" caption="Spin Asymmetry">}}
{{< /galleryscg >}}

Here is the complete example:

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/PolarizedSpinAsymmetry.py"  language="python" >}}




