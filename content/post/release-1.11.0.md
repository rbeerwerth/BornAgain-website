+++
title = "New release of BornAgain: version 1.11"
date = "2018-03-02T08:30:10+02:00"
description = "BornAgain 1.11 has been released"
draft = false
comments = false
authors = ["herck"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### BornAgain 1.11 has been released
{{< /alert >}}

{{< alert theme="info" >}}
Starting from this release, we are using Python3 as the default scripting platform in BornAgain.
Users can however choose between downloading a Python2 or Python3 based installer.
In the future, Python2 support will be discontinued.
We recommend all users to update their Python installation to version 3.x, if they haven't done so already.
{{< /alert >}}

**This release has the following highlights:**

1. Off-specular simulation is now supported in the GUI.
1. Support for materials defined by SLD.
1. Specular simulation implemented in core library.
1. New interface for simulation results now includes possible unit conversions.
1. Python API: retrieve minimizer catalogue.
1. Switched to Python 3.x as the default version.
1. GUI: extensive refactoring to improve maintainability.
1. GUI: possibility to add constant or Poisson background to simulations.
1. GUI: Fourier transform of simulation results.
1. GUI: beam polarization and polarization analysis are now supported.


**API changes:**

1. Detector axes units (e.g. `ba.IDetector2D.NBINS`) now accessed through AxesUnits (e.g. `ba.AxesUnits.NBINS`).
1. GUI project compatibility with previous versions is broken.


**Other changes:**

1. Documentation: large part of website has been migrated to Hugo website
1. Bugfix: BornAgain GUI no longer contains a limit on number of threads.
1. Numerous other bugfixes.

More details on our issue [tracker](http://apps.jcns.fz-juelich.de/redmine/versions/43).

As always, we very much welcome your comments and feedback!
