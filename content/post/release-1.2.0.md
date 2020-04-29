+++
title = "BornAgain release 1.2 with physics-centered manual"
date = "2015-06-10T08:30:10+02:00"
description = "BornAgain 1.2 has been released"
draft = false
comments = false
authors = ["pospelov"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### BornAgain 1.2 has been released
{{< /alert >}}

The main change this time is the recast user manual, available at [link](http://apps.jcns.fz-juelich.de/src/BornAgain/BornAgainManual-1.7.1.pdf).

The manual now fully concentrates on the theoretical background of BornAgain,
on the physical models and their implementation whereas the more mundane
questions of software usage are exclusively covered by the online [documentation]({{< relref "documentation" >}}).

The manual is still incomplete. Additional chapters will be published along with the next couple of software releases.

**Summary of changes in the code:**

1. Kernel: support for polarized neutron scattering with polarization/analysis along different axes (no longer restricted to z-axis).
1. GUI: new features in graphical user interface
   * GUI real time view us now saved in projects
   * Beam divergence can be exported to Python script
   * InstrumentView allows to change beam divergency with the help of fancy distribution viewer
   * JobView allows to normalize all selected jobs to the specific [min, max] to simplify intensity map comparison
1. Various bug fixes

**API changes:**

1. Renamed `Simulation` to `GISASSimulation` for consistency with other types of simulations.
1. Removed `ParticleInfo` completely from the public API: position information is now contained in the `Particle` class.

More details on our issue [tracker](http://apps.jcns.fz-juelich.de/redmine/versions/28).

As always, we very much welcome your comments and feedback!
