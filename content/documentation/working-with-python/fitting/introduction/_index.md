+++
title = "Introduction"
weight = 10
+++

# Introduction

Fitting in BornAgain deals with estimating the optimum parameters in the numerical model (i.e. scattering simulation) 
by minimizing the difference between simulated and reference data. The features include

+ A variety of built in minimization algorithms.
+ Possibility to use external minimizers (bumps, lmfit, etc).
+ Choice over possible fitting parameters, their properties and correlations.
+ Full control over objective function calculations, including the use of different normalizations and assignments of different masks and weights to different areas of the reference data.
+ Possibility to fit simultaneously an arbitrary number of data sets.

{{< alert theme="info" >}}
The BornAgain fitting interface was redesigned in October, 2018 for better compatibility
with third party minimizers ([scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html), [lmfit](https://lmfit.github.io/lmfit-py/), [bumps](https://bumps.readthedocs.io/en/latest/)).
{{< /alert >}}

In the following explanations we will be mostly focused on GISAS data. However, all of the following is also applicable for specular and off-specular fits.

{{% children depth="2" %}}

