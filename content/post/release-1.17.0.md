+++
title = "New release of BornAgain: version 1.17"
date = "2020-06-17T8:30:10+02:00"
description = "BornAgain 1.17 has been released"
draft = false
comments = false
authors = ["pospelov"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### New release of BornAgain: version 1.17
{{< /alert >}}

We are glad to announce [BornAgain 1.17.0](https://www.bornagainproject.org/download/) release.

This release introduces the Nevot-Croce roughness model and provides a possibility to
switch between roughness models and reflectometry engines. Few new form factors have been added and
the form factor section of the manual has been revised. The GUI has been slightly refreshed
to address various visual issues on high DPI monitors. We have added support for polarized reflectometry.
It doesn't support roughness (neither magnetic nor structural) yet. 

The CMake minimum required version has been changed to 3.14, and for Linux users for smooth installation
the experience we recommend Ubuntu Focal.
The Minimum supported macOS version is now 10.13. We stop distributing BornAgain for Python 2.7 and
suggest our users switch to the latest Python 3.8. 

**Example highlights**

+ [Specular simulation with different roughness models]({{< relref "documentation/examples/reflectometry/roughness-model/index.md" >}})
+ [Basic polarized reflectometry]({{< relref "documentation/examples/reflectometry/basic-polarized-reflectometry/index.md" >}})
+ [Reflectometry: Real life fitting]({{< relref "documentation/examples/fitting/extended/real-life-reflectometry/index.md" >}})

**API changes:**

* Python: form factor ripples API changed.

**Other changes:**

+ Speed-up computations for samples with a large number of layers.
+ Add the Nevot-Croce roughness model and the possibility to switch between various models.
+ Add support for polarized reflectometry.
+ Update physical constants to 2020 CODATA recommended values.
+ FormFactors: add CantellatedCube.
+ FormFactors: speedup FormFactorFullSPheroid.
+ FormFactors: revise and extend ripple form factor family.
+ Fix HighDPI issues in GUI on various platforms.
+ Various bug fixes.

More details on our [issue tracker](http://apps.jcns.fz-juelich.de/redmine/versions/51).

As always, we very much welcome your comments and feedback!
