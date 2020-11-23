+++
title = "Non-perfect polarizer + analyzer"
weight = 40
+++

### Polarized specular reflectometry with non-perfect polarizer and analyzer

In this example, we show how to perform a specular reflectometry simulation with polarized neutrons and 
both a non-perfect polarizer as well as analyzer.
The example is inspired by and performed with parameters close to the ones in [the paper by Devishvili et al.](https://doi.org/10.1063/1.4790717).
This example is a saturated iron film on top of a MgO substrate.
On top of the iron layer is a thin Pd cap layer.


We don't explain the whole script in detail here, it combines all concepts that were introduced before
in the polarized reflectometry section.
Instrument resolution is simulated as explained in the 
[ToF - Resolution effects example]({{% ref-example "reflectometry/tofr-with-resolution" %}}).
Furthermore, a constant background is added:

{{< highlight python>}}
simulation.setBackground( ba.ConstantBackground( 1e-7 ) )
{{< /highlight >}}

For a more detailed explanation we refer to the example on 
[adding a constant background]({{% ref-example "beam-and-detector/constant-background" %}}).

The values for the efficiency of the polarizer and analyzer are taken from the above mentioned paper by 
[Devishvili et al.](https://doi.org/10.1063/1.4790717):

{{< highlight python>}}
polarizer_efficiency = 0.986
analyzer_efficiency  = 0.970
{{< /highlight >}}

These values are used to initialize the polarizer and analyzer:

{{< highlight python>}}
simulation.setBeamPolarization(polarization * polarizer_efficiency)
simulation.setAnalyzerProperties(analyzer, analyzer_efficiency, 0.5)
{{< /highlight >}}

This setup is then utilized to simulate the four reflectivity channels

{{< highlight python>}}
results_pp = run_simulation(polarization = ba.kvector_t(0, 1, 0), 
                            analyzer     = ba.kvector_t(0, 1, 0), 
                            polarizer_efficiency = polarizer_efficiency,
                            analyzer_efficiency  = analyzer_efficiency )
results_mm = run_simulation(polarization = ba.kvector_t(0, -1, 0), 
                            analyzer     = ba.kvector_t(0, -1, 0), 
                            polarizer_efficiency = polarizer_efficiency,
                            analyzer_efficiency  = analyzer_efficiency )

results_pm = run_simulation(polarization = ba.kvector_t(0,  1, 0), 
                            analyzer     = ba.kvector_t(0, -1, 0), 
                            polarizer_efficiency = polarizer_efficiency,
                            analyzer_efficiency  = analyzer_efficiency )
results_mp = run_simulation(polarization = ba.kvector_t(0, -1, 0), 
                            analyzer     = ba.kvector_t(0,  1, 0), 
                            polarizer_efficiency = polarizer_efficiency,
                            analyzer_efficiency  = analyzer_efficiency )
{{< /highlight >}}

The computed reflectivity looks like this:

{{< galleryscg >}}
{{< figscg src="/files/simulated/PolarizedNonperfectAnalyzerPolarizer.png" width="650px" caption="Reflectivity">}}
{{< /galleryscg >}}

Due to the different values for the polarizer and analyzer efficiency, we obtain
different reflectivity curves for the two spin-flip channels.
As one can verify, these results are in good agreement with the measurement as well as the
simulations presented by [Devishvili et al.](https://doi.org/10.1063/1.4790717)


Here is the complete example:

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/PolarizedNonperfectAnalyzerPolarizer.py"  language="python" >}}




