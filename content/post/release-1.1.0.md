+++
title = "New release of BornAgain: version 1.1"
date = "2015-04-22T08:30:10+02:00"
description = "BornAgain 1.1 has been released"
draft = false
comments = false
authors = ["herck"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### BornAgain 1.1 has been released
{{< /alert >}}

BornAgain 1.1 is now available for download.

Most of the efforts in this sprint have been devoted to porting more features from the core library to the GUI.

**Summary of changes in the code:**

1.  New form factor: truncated cube
1.  New features in graphical user interface:
    *   Beam divergence, detector resolution function
    *   `ParticleComposition` (particles composed from other particles)
    *   `ParticleDistribution` (particles with size distribution)
    *   Export of GUI simulation into a Python script

**API changes:**

1. `LatticeBasis` now is called a `ParticleComposition`
1. `Transform3D` object is removed in the favor of `RotationX`, `RotationY`, `RotationZ` and `RotationEuler` objects

More details on our issue [tracker](http://apps.jcns.fz-juelich.de/redmine/versions/27).

As always, we very much welcome your comments and feedback!
