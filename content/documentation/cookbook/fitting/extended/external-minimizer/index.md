+++
title = "External minimizer"
weight = 40
+++

## External minimizer

In this example we are demonstrating how to run a typical fitting task in BornAgain using a third party minimizer.

The BornAgain fit parameters and minimizer interface were developed with the idea to simplify the switch between our own minimization engines and other, possibly more advanced minimization libraries.
Particularly, we have been inspired by the [lmfit Python package](https://lmfit.github.io/lmfit-py/).

This makes the switch between the BornAgain and `lmfit` minimizers very easy.

**Using the BornAgain default minimizer**

{{< highlight python >}}
import bornagain as ba

params = ba.Parameters()
params.add('radius', value=7*nm, min=5*nm, max=8*nm)
params.add('length', value=10*nm, min=8*nm, max=14*nm)

result = ba.Minimizer().minimize(fit_objective.evaluate_residuals, params)
fit_objective.finalize(result)
{{< /highlight >}}

**Using the lmfit minimizer**

{{< highlight python >}}
import lmfit

params = lmfit.Parameters()
params.add('radius', value=7*nm, min=5*nm, max=8*nm)
params.add('length', value=10*nm, min=8*nm, max=14*nm)

result = lmfit.minimize(fit_objective.evaluate_residuals, params)
fit_objective.finalize(result)

print(result.params.pretty_print())
{{< /highlight >}}

The complete script for the `lmfit` based fitting is shown below.

{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/external_minimizer/lmfit_basics.py" language="python" >}}
