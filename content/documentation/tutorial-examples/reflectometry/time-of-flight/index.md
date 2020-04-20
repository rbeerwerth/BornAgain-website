+++
title = "Time of Flight Reflectometry"
weight = 30
+++

### Time of Flight Reflectometry 

This short tutorial quickly illustrates the setup of a Time of Flight (TOF) Reflectometry simulated experiment. 

Setting up a TOF simulation boils down to specifying the range of values spanned by the $q_z$ vector, rather than the range spanned by the angle $\theta$ of the beam:

``` python
    qzs = np.linspace(0.01, 1.0, scan_size)  # qz-values
    scan = ba.QSpecScan(qzs)
    simulation = ba.SpecularSimulation()
    simulation.setScan(scan)
```



{{< galleryscg >}}
{{< figscg src="TimeOfFlightReflectometry.png" width="500px" caption="This figure shows the reflectometry signal obtained after running the TOF simulation of the script below." >}}
{{< /galleryscg >}}

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/TimeOfFlightReflectometry.py"  language="python" >}}
