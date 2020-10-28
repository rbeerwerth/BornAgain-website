+++
title = "Spin-flip reflectivity"
weight = 20
+++

### Spin-Flip Reflectivity

In this section, we want to extend the [basic polarized reflectometry tutorial]({{% ref-example "polarized-reflectometry/basic-polarized-reflectometry" %}}) to simulate spin-flip reflectivity.
For this purpose, we want to parametrize the magnetization by the angle $\alpha$ between the magnetization and the spin of the incoming neutrons and its magnitude $\left| \mathbf{M} \right|$:
$$\mathbf M =  \left| \mathbf{M} \right| \left( \sin \alpha, \cos \alpha, 0\right)^\mathrm{T}$$
In practice, the construction of the magnetization vector in Python then proceeds as follows:
{{< highlight python>}}
magnetizationMagnitude = 1e8
angle                  = 30 * deg
magnetizationVector    = ba.kvector_t(
                magnetizationMagnitude * numpy.sin(angle), 
                magnetizationMagnitude * numpy.cos(angle), 
                0)
{{< /highlight >}}

In addition to the non-spin-flip channels, we simulate the Spin-Flip (up-down and down-up) channels 
with the following function calls

{{< highlight python>}}
results_pm = run_simulation(ba.kvector_t(0,  1, 0),
                            ba.kvector_t(0, -1, 0))
results_mp = run_simulation(ba.kvector_t(0, -1, 0),
                            ba.kvector_t(0,  1, 0))
{{< /highlight >}}

Running the full script, that is given below, we obtain the following simulation result:

{{< galleryscg >}}
{{< figscg src="PolarizedSpinFlip.png" width="650px" caption="Reflectivity">}}
{{< /galleryscg >}}

This plot shows the resulting reflectivity in all four channels.
The non-spin-flip channels (up-up and down-down) are similar to the result [without spin flip]({{% ref-example "polarized-reflectometry/basic-polarized-reflectometry" %}}).
As expected, both spin-flip channels are identical.

Here is the complete example:

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/PolarizedSpinFlip.py"  language="python" >}}

