+++
title = "Importing experimental data"
weight = 34
+++

## Importing experimental data

The BornAgain I/O module supports only a few file formats: `ascii`, `tiff` and our own internal format. This might be not enough when it comes to the fitting of data obtained from some particular instrument.
However, we fully support fitting of the data presented in the form of `numpy` arrays.

The fitting workflow is as follows:

* The user imports the data into a numpy array.
* The user creates a simulation with a beam, sample and detector defined.
  * The number of detector pixels must match the shape of the numpy array.
  * The user creates a region of interest to simulate/fit only some selected rectangle on his experimental image.
* The user passes the simulation and numpy array to the fitting engine.

### Using the fabio library

In the code snippet below we show how to create a numpy array from a file in `edf` format using the [fabio](https://pypi.org/project/fabio/) library.

{{< highlight python >}}
import fabio

img = fabio.open("experimental_data.edf")
print(img.header)

data = img.data.astype("float64")
{{< /highlight >}}

Later in the code this data array can be used to setup a fitting job.

{{< highlight python >}}
import bornagain as ba

fit_objective = FitObjective()
fit_objective.addSimulationAndData(simulation_builder, data)
{{< /highlight >}}

### Using BornAgain's own I/O

The BornAgain I/O module supports a limited amount of file formats: `ascii`, 32-bits `tiff` and an internal text format `int`.
If the file name contains `.gz` or `.bzip2` extensions, the module considers them as compressed and performs uncompressing on-the-flight.

{{< highlight python >}}
import bornagain as ba

data = ba.IntensityDataIOFactory.readIntensityData("experimental_data.int.gz").array()
{{< /highlight >}}
