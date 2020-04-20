+++
title = "New release of BornAgain: version 1.8"
date = "2017-04-07T08:30:10+02:00"
description = "BornAgain 1.8 has been released"
draft = false
comments = false
authors = ["herck"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### BornAgain 1.8 has been released
{{< /alert >}}

This release improves support for fitting: all reasonable parameters can now be used for fitting, both in Python and the GUI.

BornAgain now also supports the graded layer approximation.
The user can choose to subdivide layers into a number of slices.
For each slice, the Fresnel coefficients will be calculated from the
averaged materials that take into account the particle content in the slice.
Related to this approximation, particles can now also be 
defined to cross layer interfaces.

**API changes:**

1. ParticleLayout: `addInterferenceFunction` -> `setInterferenceFunction`
1. GUI project back-compatibility broken.

**Summary of other changes:**

1. Fitting: all reasonable parameters can now be used for fitting.
1. GUI: plot settings are now persistent.
1. Graded layer approximation: simulations can now use the average refractive index as the background. Layers can be split into multiple slices with different average material, depending on the particle content.
1. Particles can now cross layer interfaces.
1. Import of Tiff data improved.
1. Lots of refactoring and bug-fixing. 

More details on our issue [tracker](http://apps.jcns.fz-juelich.de/redmine/versions/39).

As always, we very much welcome your comments and feedback!
