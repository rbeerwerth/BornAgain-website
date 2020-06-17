+++
title = "External minimizer: plotting"
weight = 40
+++

## External Minimizers: Plotting Fit Progress

In this example we are demonstrating how to run a typical fitting task in BornAgain using a third party minimizer while plotting the results. As in our [previous example](/documentation/examples/fitting/extended/external-minimizer), we use lmfit for sake of illustration.

To plot the fit progress, it is needed to use the lmfit iteration callback function. It will come handy to define the plotting callback function as a specialized class:

```Python
class Plotter:
    """
    Adapts standard plotter for lmfit minimizer.
    """
    def __init__(self, fit_objective, every_nth = 10):
        self.fit_objective = fit_objective
        self.plotter_gisas = ba.PlotterGISAS()
        self.every_nth = every_nth

    def __call__(self, params, iter, resid):
        if iter%self.every_nth == 0:
            self.plotter_gisas.plot(self.fit_objective)
```

An instance of this class is then passed to the lmfit minimization function:

```python
    plotter = Plotter(fit_objective)
    result = lmfit.minimize(fit_objective.evaluate_residuals, params, iter_cb=plotter)
```
The complete script to plot the fitting progress and the image produced by it are shown below.


{{% figure src="ExternalMinimizerWithPlotting.png" command="Resize" options="450x" caption="Plotting the fitting progress of external minimizers" class="center" %}}



{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/external_minimizer/lmfit_with_plotting.py" language="python" >}}
