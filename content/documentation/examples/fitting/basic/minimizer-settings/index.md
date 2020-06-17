+++
title = "Minimizer settings"
weight = 30
+++

## Minimizer settings

This example demonstrates how to change the minimizer algorithm and some of its settings. For example, the following lines

{{< highlight python >}}
minimizer = ba.Minimizer()
minimizer.setMinimizer("Minuit2", "Migrad", "MaxFunctionCalls=500;Strategy=2")
{{< /highlight >}}

will set the internal minimizer to "Minuit2", its internal algorithm to "Migrad" and then pass additional options, limiting the maximum number of calls and an internal minimization strategy.

The list of available minimizers and their options can be seen with

{{< highlight python >}}
print(ba.MinimizerFactory().catalogueDetailsToString())
{{< /highlight >}}


For more information, see the
[minimizer settings tutorial]({{% relref "documentation/scripting/fitting/minimizers/index.md" %}}).

{{< highlightfile file="/static/files/python/fitting/ex01_BasicExamples/minimizer_settings.py" language="python" >}}
