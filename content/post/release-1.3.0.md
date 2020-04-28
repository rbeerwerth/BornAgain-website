+++
title = "New release of BornAgain: version 1.3"
date = "2015-07-31T08:30:10+02:00"
description = "BornAgain 1.3 has been released"
draft = false
comments = false
authors = ["pospelov"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### BornAgain 1.3 has been released
{{< /alert >}}

This time we have been working on a deep refactoring of the machinery related to the positioning and rotation of particles. As a result `Particle`, `CoreShellParticle` and `ParticleComposition` can be rotated and translated inside layers in a similar way. We wrote a few tutorials explaining the latest changes.

**Summary of changes in the code:**

1. New functional test machinery to test all three domains simultaneously (C++, Pyton and GUI), covering more test cases in a more consistent way.
1. Windows installer: for GUI use, python installation is no longer required
1. GUI: added position/rotation to ParticleComposition and ParticleCoreShell and enabled adding ParticleComposition to another ParticleComposition
1. GUI: possibility to open project files from older releases
1. Various bugfixes

**New tutorials:**

1. [Particles positioning tutorial]({{< relref "documentation/scripting/particle-positioning/index.md" >}})
1. [Particles rotation tutorial]({{< relref "documentation/scripting/particle-rotation/index.md" >}})
1. [Particle composition tutorial]({{< relref "documentation/scripting/particle-composition/index.md" >}})
1. Working with sample parameters tutorial (*obsolete link*)
1. [Introduction to fitting]({{< relref "documentation/scripting/fitting/introduction" >}})
1. [Basic fitting tutorial]({{< relref "documentation/scripting/fitting/basic-fitting-tutorial/index.md" >}})

**API changes:**

1. Removed `depth` from `ParticleLayout::addParticle`. New interface provides for abundance, position and possible rotation

More details on our issue [tracker](http://apps.jcns.fz-juelich.de/redmine/versions/29).

As always, we very much welcome your comments and feedback!
