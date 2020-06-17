+++
title = "Depth-probe"
weight = 17
+++

## Depth-probe

A depth-probe simulation is an auxiliary simulation type, which helps to visualize
the total intensity as function of the beam incidence angle and the position in
the sample.

Here we will consider the intensity map produced by a neutron resonator composed of one Ti/Pt bilayer.

A more detailed description of this example can be found in the [Depth Probe Tutorial]({{% ref-tutorial "simulation-classes/depth-probe/index.md" %}}).

{{< figscg src="DepthProbeSimulation.png" width="500" class="center">}}

In the figure above, the $y$ axis corresponds to the position across the sample surface
(in nanometers), while the $x$ axis corresponds to the
incident angle $\alpha_i$. The script below provides a complete example of how to run a depth-probe simulation which produces the image above.

{{< highlightfile file="/static/files/python/simulation/ex07_Miscellaneous/DepthProbe.py" language="python" >}}
