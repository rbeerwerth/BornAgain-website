+++
title = "Reflectometry: Fit Honeycomb"
weight = 60
+++

## Reflectometry: Fit Honeycomb

We fit the structure stuffs, actual data by A. Glavic et al., published in 
[this paper](https://doi.org/10.1002/advs.201700856)


initial parameters yield

{{< galleryscg >}}
{{< figscg src="Honeycomb_reflectivity_initial.png" width="350px" caption="Reflectivity with the initial parameters">}}
{{< figscg src="Honeycomb_sld_initial.png" width="350px" caption="SLD profile with the initial parameters">}}
{{< /galleryscg >}}


Allow some substantial time for fitting

{{< galleryscg >}}
{{< figscg src="Honeycomb_reflectivity_fit.png" width="350px" caption="Reflectivity with the fit result">}}
{{< figscg src="Honeycomb_sld_fit.png" width="350px" caption="SLD profile with the fit result">}}
{{< /galleryscg >}}




{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/honeycomb/Honeycomb_Fit.py" language="python" >}}

{{% filelink file="/static/files/python/fitting/ex03_ExtendedExamples/honeycomb/honeycomb_data.zip" name="Reference data" %}}

