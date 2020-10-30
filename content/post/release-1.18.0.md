+++
title = "New release of BornAgain: version 1.18"
date = "2020-10-30"
description = "BornAgain 1.18 has been released"
draft = false
comments = false
authors = ["wuttke"]
tags = ["Release"]
categories = ["News"]
+++

{{< alert theme="success" >}}
#### New release of BornAgain: version 1.18
{{< /alert >}}

Today, BornAgain 1.18.0 has been released.

The most important change is improved numerics for the computation of reflection
and transmission of scalar or polarized beams. The new algorithms is numerically
stable even for arbitrarily many layers and for low overall transmission. For
rough interfaces, one can choose between a tanh scattering-length density profile
and the Névot-Croce approximation. There is a new documentation section with
[polarized reflectometry]({{< relref "documentation/examples/polarized-reflectometry" >}})
examples.

There are a few API changes. Some classes have been renamed for clarity or brevity:
- FootprintSquare, FootprintGauss, FormFactorHollowSphere, CosineRipple, SawtoothRipple.
- FormFactorGaussSphere now models a sphere, not an ellipsoid.
- FormFactorSphereLogNormalRadius is now positioned at the center, not at the bottom.
- In constructors that involve the Voigt function, the order of the arguments gamma
  and eta has been unified.

In examples, the material with refractive index 1 has been renamed from "air" to "vacuum".

As always, we very much welcome your comments and feedback!
