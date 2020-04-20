+++
title = "BornAgain hotfix: 1.7.1"
date = "2016-12-05T08:30:10+02:00"
description = "A bugfix release for BornAgain is now available"
draft = false
comments = false
authors = ["pospelov"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### A bugfix release for BornAgain is now available
{{< /alert >}}


This is a hotfix to the [Release-1.7]({{< relref "release-1.7.0.md" >}}).

**Change summary:**

1. Bug #1679: Remove leading U+FEFF from FindYamlCpp05.cmake
1. Bug #1682: hotfix: rm local version of FindBoost.cmake
1. Bug #1658: add qt5-svg as a dependency
1. Bug #1662: CMake: require Qt version 5.4
1. Bug #1687: LMA is incorrectly normalized
1. Bug #1692: GUI and Py: simulation crash when sample contains undefined material
1. Bug #1681: Fitting GUI: free parameter error
1. Bug #1661: FitSuite doesn't know about TestMinimizer
1. Bug #1639: GUI: crash if fitting parameter removed
