+++
title = "Accessing simulation results"
weight = 30
+++

## Accessing simulation results

In this tutorial we explain how to access GISAS simulation results,
how to plot the simulated detector 2D intensity map as a color map and
how to export the result into various formats.

### SimulationResult object

The detector intensity in BornAgain can be retrieved via special object of `SimulationResult` type.

```python

simulation = GISASSimulation()
simulation.setDetectorParameters(20, -1.0*deg, 1.0*deg, 10, 0.0*deg, 1.0*deg)
simulation.setSample(sample)
simulation.runSimulation()

result = simulation.result()
```

`SimulationResult` object allows

* Export of intensity data into `numpy` array.
* Immediate plotting of intensity data as color map using plot utils provided by BornAgain installation.
* Convertion of intensity data into one of supported external formats for the later processing in the software of user's choice.

### Export to numpy array

The user can convert a `SimulationResult` object into a numpy array and proceed
with it in the manner he is more comfortable with.
In the code snippet below the method `array()` returns a numpy array of the same shape as the detector pixel array.
The method `numpy.savetxt` from the numpy library saves the data to an ASCII file.

```python
arr = simulation.result().array()
numpy.savetxt("intensity.txt", arr)
```

### Plotting simulation results

BornAgain provides few convenient functions to plot simulation result as color map. Internally they are using not more than `matplotlib` routines.
The function `plot_simulation_result` makes a plot and holds the graphics, while `plot_colormap` makes the plot 
and let the program continue to allow more plots on same figure, for example.

The code snippet below gives few examples

```python
result = simulation.result()

# plot color map with automatic axes labels and min/max calculated
ba.plot_simulation_result(result)

# plot color map with custom labels and min/max defined.
ba.plot_colormap(result, zmin=1e-04, zmax=1e+05, xlabel="")
```

### Histogram2D object

It is possible to convert `SimulationResult` to BornAgain's `Histogram2D` object. It allows to perform
some additional data treatment tasks:

* Histogram clipping to draw only the region of interest
* Slicing of 2D histograms into 1D histograms
* Creation of relative difference histograms, and many other

In the code snippet below simulation results are converted to `Histogram2D` object with axes converted into Q-space,
then it is cropped to the region of interest, plotted and then saved to disk into BornAgain internal format.

```python
hist = simulation.result().histogram2d(units=ba.AxesUnits.QSPACE)
hist = hist.crop(-1.0, 0.5, 1.0, 1.0)
ba.plot_histogram(hist)
hist.save("result.int.gz")

```

Additional information can be found in the following pages:

* [Accessing simulation results example]({{% ref-example "miscellaneous/accessing-simulation-results" %}})
* [Plotting with axes in different units]({{% ref-example "miscellaneous/axes-in-different-units" %}})
* [SimulationResult C++ class reference](http://apps.jcns.fz-juelich.de/doxy/BornAgain/classSimulationResult.html)
* [Histogram1D C++ class reference](http://apps.jcns.fz-juelich.de/doxy/BornAgain/classHistogram1D.html)
* [Histogram2D C++ class reference](http://apps.jcns.fz-juelich.de/doxy/BornAgain/classHistogram2D.html)
