+++
title = "Experiment at GALAXI"
weight = 30
+++

## Experiment at GALAXI

This is an example of a real data fit. We use our own measurements performed at the laboratory diffractometer [GALAXI](http://www.fz-juelich.de/jcns/jcns-2//DE/Leistungen/GALAXI/_node.html) in Forschungszentrum Jülich. 

{{< galleryscg >}}
{{< figscg src="FitGALAXIData_setup.jpg" width="350px" caption="Real-space model">}}
{{< figscg src="FitGALAXIData.png" width="350px" caption="Fit window">}}
{{< /galleryscg >}}

* The file `sample_builder.py` contains a sample description.
* The sample represents a 4 layer system (substrate, teflon, hmdso and air) with Ag nanoparticles placed inside the hmdso layer on top of the teflon layer.
* The sample is generated with the help of a `SampleBuilder`, which is able to create samples depending on parameters defined in the constructor and passed through to the `create_sample` method.
* The nanoparticles have a broad log-normal size distribution.

{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/experiment_at_galaxi/sample_builder.py" language="python" >}}

<hr>

* The file `fit_galaxi_data.py` contains the parts related to detector initialization, simulation setup, importing of the data and finally the fit engine setup.
* The rectangular detector is created to represent the PILATUS detector from the experiment (line 19).
* In the simulation settings the beam is initialized and the detector is assigned to the simulation. A region of interest is assigned at line 39 to simulate only a small rectangular window. Additionally, a rectangular mask is added to exclude the reflected beam from the analysis (line 40).
* The real data is loaded from a tiff file into a histogram representing the detector's channels.
* The `run_fitting()` function contains the initialization of the fitting kernel: loading experimental data, assignment of fit pair, fit parameters selection (line 62).

{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/experiment_at_galaxi/fit_galaxi_data.py" language="python" >}}
