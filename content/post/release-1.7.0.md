+++
title = "New release of BornAgain: version 1.7"
date = "2016-11-15T08:30:10+02:00"
description = "BornAgain 1.7 has been released"
draft = false
comments = false
authors = ["herck"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### BornAgain 1.7 has been released
{{< /alert >}}
This release improves GUI support for fitting: The GUI allows now to import data, set region of interest, adjust detector settings, select fit parameters and run the fitting engine.

**API changes:**

1. Constructors of FormFactorGauss and FormFactorLorentz now take a length instead of a volume.
1. GUI project back-compatibility broken.

**Summary of other changes:**

1. GUI support for fitting experimental data extended: masking, region of interest, linking dataset to instrument, control parameters of fit engines.
1. Core: Specular peaks can be added to the GISAS image.
1. Manual: Chapter on scattering revised, chapter on assemblies extended. Started Part II = Reference.
1. Source repository migrated to [github](https://github.com/scgmlz/BornAgain).
1. Various bugfixes.

More details on our issue [tracker](http://apps.jcns.fz-juelich.de/redmine/versions/37).

As always, we very much welcome your comments and feedback!
