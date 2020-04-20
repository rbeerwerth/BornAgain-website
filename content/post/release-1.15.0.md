+++
title = "New release of BornAgain: version 1.15"
date = "2019-02-25T8:30:10+02:00"
description = "BornAgain 1.15 has been released"
draft = false
comments = false
authors = ["herck"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### New release of BornAgain: version 1.15
{{< /alert >}}

This release was mainly focused on incorporating the feedback from the BornAgain
school in December 2018. We also added some specific features for user support and
continued on the way to providing specular reflectivity in BornAgain.

**This release has the following highlights:**

* Act on feedback from BornAgain school in December 2018: new features and corrections
* Support q-based specular simulations
* Implement features from specific user requests

**API changes:**

* Python: method getAlphaAxis renamed into coordinateAxis in SpecularSimulation
* Python: add axis() accessor in SimulationResult (to be used instead SimulationResult.data().getAxis())

**Other changes:**

* Numerous bug fixes

More details on our [issue tracker](http://apps.jcns.fz-juelich.de/redmine/versions/47).

As always, we very much welcome your comments and feedback!
