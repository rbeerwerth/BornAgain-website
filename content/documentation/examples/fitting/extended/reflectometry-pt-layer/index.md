+++
title = "Reflectometry: Fit Pt Layer"
weight = 50
+++

## Reflectometry: Fit Pt Layer

We fit the Pt layer, actual data by M. Fitzsimmons et al., obtained from 
[this repository](https://doi.org/10.5281/zenodo.4072376)


initial parameters yield

{{< galleryscg >}}
{{< figscg src="Pt-Layer-initial.png" width="550px" caption="Reflectivity with the initial parameters before fitting">}}
{{< /galleryscg >}}


Little time for fitting


{{< galleryscg >}}
{{< figscg src="Pt-Layer-final.png" width="550px" caption="Reflectivity with the parameters obtained from our fit">}}
{{< /galleryscg >}}




{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/pt-layer/Pt_layer_fit.py" language="python" >}}

{{% filelink file="/static/files/python/fitting/ex03_ExtendedExamples/pt-layer/RvsQ_36563_36662.txt.gz" name="Reference data" %}}

