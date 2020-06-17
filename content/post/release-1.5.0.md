+++
title = "New release of BornAgain: version 1.5"
date = "2016-02-15T08:30:10+02:00"
description = "BornAgain 1.5 has been released"
draft = false
comments = false
authors = ["pospelov"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### BornAgain 1.5 has been released
{{< /alert >}}

During this release we have worked on preparing the implementation of fitting in the GUI, and even if the fitting is not there yet, we are getting close.

**Summary of changes in the code:**

1. Core: interference function calculates particle densities automatically, when possible.
1. GUI: 1D interference function is now available.
1. GUI: new rectangular detector providing more accurate simulation of real life setup.
1. GUI: new mask editor allows to draw various shapes on top of intensity map to exclude it from the analysis.
1. GUI: Selection of axes (degrees, radians,number of bins, Q-space) for intensity data.
1. Note for Linux users: we have migrated to C++11 (minimal compiler version changed).
1. Note for Linux users: new dependency from Eigen library.
1. Compatibility issues: back compatibility with GUI's old project files is broken.
1. Various bugfixes.

**New tutorials:**

1. [How to setup PyCharm project](#)
1. [Detector types tutorial]({{< relref "documentation/scripting/detectors" >}})
1. [Accessing simulation results tutorial]({{< relref "documentation/scripting/accessing-simulation-results/index.md" >}})
1. [Importing experimental data]({{< relref "documentation/scripting/fitting/instrument-description" >}})

**New examples:**

1. [Rectangular detector]({{< relref "documentation/examples/beam-and-detector/rectangular-detector/index.md" >}})
1. [Real life fit example: experiment at GALAXI]({{< relref "documentation/examples/fitting/extended/experiment-at-galaxi/index.md" >}})
1. [Accessing simulation results]({{< relref "documentation/examples/miscellaneous/accessing-simulation-results/index.md" >}})
1. [Plotting with axes in different units]({{< relref "documentation/examples/miscellaneous/axes-in-different-units/index.md" >}})

**API changes:**

1. `FTDecayFunctions` introduced to use together with 1D and 2D lattices instead of former `FTDistributionFunctions`.
1. Use `InterferenceFunction1DLattice::setDecayFunction()` instead of former `InterferenceFunction1DLattice::setProbabilityDistribution()`

More details on our issue [tracker](http://apps.jcns.fz-juelich.de/redmine/versions/31).

As always, we very much welcome your comments and feedback!
