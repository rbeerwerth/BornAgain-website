+++
title = "New release of BornAgain: version 1.17"
date = "2020-06-17T8:30:10+02:00"
description = "BornAgain 1.17 has been released"
draft = false
comments = false
authors = ["wuttke"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### New release of BornAgain: version 1.17
{{< /alert >}}

This letter contains three announcements:
+ Publication of the BornAgain reference paper in J. Appl. Cryst.
+ Changes in development team
+ Release 1.17

## Reference paper ##

A comprehensive description of BornAgain has been published as an open-access
article in the Journal of Applied Crystallography:

> G. Pospelov, W. Van Herck, J. Burle, J. M. Carmona Loaiza, C. Durniak, J. M. Fisher, M. Ganeva, D. Yurov and J. Wuttke, BornAgain: software for simulating and fitting grazing-incidence small-angle scattering. J. Appl. Cryst. 53, 262-276 (2020)

> http://scripts.iucr.org/cgi-bin/paper?S1600576719016789, https://doi.org/10.1107/S1600576719016789

This is intended to be the canonical reference for many years to come;
please cite this article whenever refering to the BornAgain project.
Additionally, please continue to document the use of a specific software
version by an appropriate citation as suggested [here](https://www.bornagainproject.org/documentation/howto/cite).

## Change in development team ##

Walter Van Herck and Dmitry Yurov have left our group to reorient themselves
geographically or/and career-wise. Walter has been one of the two lead
developers since the start of the project in 2012. Dmitry joined in 2017
with funding from the European Spallation Source. We are very grateful to
Walter and Dmitry for their lasting contributions to BornAgain.

In the meantime two new research software engineers have joined the team,
Alexander Schober and Randolf Beerwerth. Alexander has been with the MLZ
Scientific Computing Group since 2018, and has so far worked on two data
reduction projects. He is now supporting Gennady in a deep overhaul of the
GUI, in view of its generalization to reflectometry. Randolf has been with
us since February 2020; he is currently working on the reflectometry core
and on polarization support.

## Release 1.17.0 ##

Today, BornAgain 1.17.0 has been released.

New Core functionality includes the Nevot-Croce roughness model, support
for switching between roughness models and reflectometry engines, and a few
new form factors (cantellated cubes, rectangular ripples). The API has changed
for ripples, as described in a new section of the form factor catalog.

Changes in the GUI mainly address visual issues on high-resolution displays.
This may result in some compatibility issues with previous versions.

Much of this release is devoted to internal consolidation and speedup.
- Standard reflectometry computations become ill conditioned at vanishing
transmissions. Previously, we addressed this issue with a bifurcation.
We have now implemented a new linear algorithm that is much faster for
samples with many layers.
- The spheroid form factor is now computed without numeric integration.
Thanks to Matt Thompson (Australian National University) for the suggestion.
- Continuous integration tests have been put under control of GitHub Actions,
and tentatively been moved to GitHub's own cloud service. This will reduce
waiting times, and thereby make development faster and smoother. Thanks to
Andrew Nelson (ANSTO) for insights from the GitHub Actions script he wrote
as part of his reflectometry software cross-validation efforts.

We have stopped distributing BornAgain for Python 2.7. We recommend switching to
the latest Python, 3.8. The CMake minimum required version has changed
to 3.14. The minimum supported MacOS version is now 10.13. For building under
Linux, we recommend Ubuntu 20.04 LTS Focal / Debian 11 bullseye.

There are three new examples:
+ [Specular simulation with different roughness models]({{< relref "documentation/examples/reflectometry/roughness-model/index.md" >}})
+ [Basic polarized reflectometry]({{< relref "documentation/examples/reflectometry/basic-polarized-reflectometry/index.md" >}})
+ [Reflectometry: Real life fitting]({{< relref "documentation/examples/fitting/extended/real-life-reflectometry/index.md" >}})

More details are in the CHANGELOG, the [issue tracker](http://apps.jcns.fz-juelich.de/redmine/versions/51), and the git history.

As always, we very much welcome your comments and feedback!
