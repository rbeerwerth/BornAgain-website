+++
title = "Without analyzer"
weight = 30
+++

### Polarized Reflectometry Without Analyzer

Starting from the [spin-flip tutorial]({{% ref-example "polarized-reflectometry/polarized-spin-flip" %}}), we 
want to remove the analyzer and perform a reflectivity simulation with incident polarized neutrons and no 
polarization analysis of the reflected beam.
All other parameters of the simulation remain unchanged.

Omitting the polarization analysis corresponds to summing up the spin-flip and non-spin-flip channels 
for both incident polarization states:
$$I^+ = I^{++} + I^{+-}
\hspace{2em}
I^- = I^{- -} + I^{-+}$$

In a script, these to polarization measurements can be computed according to:

{{< highlight python>}}
r_plus  = results_pp + results_pm
r_minus = results_mm + results_mp
{{< /highlight >}}

Here, `results_pp`, `results_mm` are the reflectivities in the non-spin-flip channels computed by calling

{{< highlight python>}}
q, results_pp = run_simulation(ba.kvector_t(0,  1, 0),
                               ba.kvector_t(0,  1, 0))
q, results_mm = run_simulation(ba.kvector_t(0, -1, 0),
                               ba.kvector_t(0, -1, 0))
{{< /highlight >}}

and the spin-flip channels are computed by

{{< highlight python>}}
q, results_pm = run_simulation(ba.kvector_t(0,  1, 0),
                               ba.kvector_t(0, -1, 0))
q, results_mp = run_simulation(ba.kvector_t(0, -1, 0),
                               ba.kvector_t(0,  1, 0))
{{< /highlight >}}


However, this approach has the disadvantage that it requires to perform four simulations in order to compute the two reflectivity curves.
Instead, BornAgain supports the direct computation of the two channels for incident polarized neutrons without polarization analysis.
This can simply be achieved by not specifying any analyzer when setting up the `simulation` object and hence omitting the line 

{{< highlight python>}}
simulation.setAnalyzerProperties(analyzer, 1.0, 0.5)
{{< /highlight >}}

In this example, this is achieved by calling the `run_simulation` function for up and down polarization of the incident neutron beam:

{{< highlight python>}}
q, results_p = run_simulation(ba.kvector_t(0,  1, 0))
q, results_m = run_simulation(ba.kvector_t(0, -1, 0))
{{< /highlight >}}

The attached script computes the two channels with both approaches and plots the results.
It is then easy to check that they are identical.
This is the resulting plot that shows the computed reflectivity for up and down polarization of the incident neutrons:

{{< galleryscg >}}
{{< figscg src="PolarizedNoAnalyzer.png" width="650px" caption="Reflectivity">}}
{{< /galleryscg >}}




Here is the complete example:

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/PolarizedNoAnalyzer.py"  language="python" >}}

