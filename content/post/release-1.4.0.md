+++
title = "New release of BornAgain: version 1.4"
date = "2015-11-03T08:30:10+02:00"
description = "BornAgain 1.4 has been released"
draft = false
comments = false
authors = ["herck"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### BornAgain 1.4 has been released
{{< /alert >}}

This release provides an easier way to use `IntensityData` objects from Python and added new export formats for simulation data. Accompanied by a big refactoring, the new version also provides for better integration of new detector geometries. As a first application of this, a rectangular detector geometry has been defined in the core library.

**Summary of changes in the code:**

1. Improved usability of IntensityData objects (slicing, histogram filling, ...)
1. GUI: export of simulation results into tiff or ascii file
1. Core: rectangular detector added (not yet in GUI)
1. Core: simulation and fit with masks applied to the detector plane
1. Core: genetic algorithm implemented, no need to install ROOT framework anymore
1. Automatic normalization of detector pixel intensity when beam intensity > 0
1. Various bugfixes

**New examples:**

1. [Fitting with masks]({{< relref "documentation/examples/fitting/advanced/fit-with-masks/index.md" >}})
1. [Fitting along slices]({{< relref "documentation/examples/fitting/advanced/fit-along-slices/index.md" >}})
1. [Fitting two datasets]({{< relref "documentation/examples/fitting/advanced/multiple-datasets/index.md" >}})

**API changes:**
1. `Simulation::getIntensityData()::getArray()` returns a numpy array with numpy-standard row, column layout (no rotation is required anymore)
1. `FitSuite::addFitParameter(name, start_value, limits, step)` order of fit parameters changed

More details on our issue [tracker](http://apps.jcns.fz-juelich.de/redmine/versions/30).

As always, we very much welcome your comments and feedback!
