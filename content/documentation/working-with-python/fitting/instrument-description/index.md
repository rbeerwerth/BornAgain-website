+++
title = "Experiment description"
weight = 37
+++

## Experiment description

To successfully simulate and fit results of some real experiment it is important to have

+ A good guess about the sample structure and the initial values of the sample parameters.
+ Full information about the instrument geometry: size and exact orientation of the detector.
+ A 2D numpy array containing the intensities measured in the detector channels.

### Experiment

As an example we will use our own measurements performed  at the laboratory diffractometer [GALAXI](http://www.fz-juelich.de/jcns/jcns-2//DE/Leistungen/GALAXI/_node.html) in Forschungszentrum Jülich.

A complete example, containing less explanations but more code, can be found in
[Real life fit example: experiment at GALAXI]({{% ref-example "fitting/extended/experiment-at-galaxi" %}}).

Our sample represents a 3-layer system (substrate, teflon and air)
with Ag nanoparticles sitting on top of the teflon layer.
The PILATUS 1M detector was placed at a distance of 1730 mm from the sample.

{{< figscg src="./setup_galaxi_experiment.png" class="center" >}}

The results of the measurement are represented by the intensity image taken in certain conditions
(beam wavelength, inclination angle, detector position) and stored in a 32-bit tiff file. To be able to fit these data we have to

* prepare a description of the simulation
* load the experimental data in BornAgain's fitting engine

### Preparing the simulation description

From the experimental setup we know the following:

+ detector geometry: number of pixels, pixel size
+ detector orientation: perpendicular to the direct beam
+ detector position: distance to the sample, coordinates of direct beam hitting the detector plane

In BornAgain, we will represent this setup using the `RectangularDetector` object.
First, we create a detector corresponding to a PILATUS detector by providing the number of detector bins and the detector's size in millimeters:

{{< highlight python >}}

npx, npy = 981, 1043
pixel_size = 0.172  # in mm
width = npx*pixel_size
height = npy*pixel_size

detector = RectangularDetector(npx, width, npy, height)

{{< /highlight >}}

Then we define the position of the direct beam in local detector coordinates (i.e. millimeters) and set the detector perpendicular to the direct beam at a certain distance:

{{< highlight python >}}

detector_distance = 1730.0  # in mm

# position of direct beam in pixels, (0,0) corresponds to lower left corner of the image
beam_xpos, beam_ypos = 597.1, 323.4  # in pixels

# position of direct beam in local detector coordinates
u0 = beam_xpos*pixel_size  # in mm
v0 = beam_ypos*pixel_size  # in mm

detector.setPerpendicularToDirectBeam(detector_distance, u0, v0)

{{< /highlight >}}

See also the [Rectangular detector tutorial]({{% ref-tutorial "detectors/rectangular-detector/index.md" %}})
and [Rectangular detector example]({{% ref-example "beam-and-detector/rectangular-detector" %}}).

### Setting the region of interest

To speed-up the simulation and to avoid an influence from uninteresting areas on the fit flow it is often convenient to define a certain region of interest `roi`. In our example we set the `roi` to the rectangle with lower left corner coordinates (85.0, 70.0) and upper right corner coordinates (120.0, 92.0), where coordinates are expressed in native detector units
(`mm` for `RectangularDetector`)

```python
simulation.setRegionOfInterest(85.0, 70.0, 120.0, 92.)
```

{{< galleryscg >}}
{{< figscg src="./galaxi_imported_data.png" width="350px" class="center">}}
{{< figscg src="./galaxi_cropped_data.png" width="350px" class="center">}}
{{< /galleryscg >}}

The final simulation setup looks as follows:

{{< highlight python >}}

simulation = GISASSimulation()
simulation.setDetector(detector)  # this is our rectangular detector
simulation.setSample(sample)  # sample creation is not covered by this tutorial
simulation.setBeamParameters(1.34*angstrom, 0.463*degree, 0.0)
simulation.setBeamIntensity(1.2e7)
simulation.setRegionOfInterest(85.0, 70.0, 120.0, 92.)

{{< /highlight >}}

During the fit, only the part of the detector corresponding to the `roi` will be simulated and used for $\chi^2$ calculations.

### Importing the real data using Fabio library

The [Fabio library](https://github.com/silx-kit/fabio) provides a convenient way to import experimental data in the form of a `numpy` array.

```python
import fabio

img = fabio.open("galaxi_data.tif.gz")
data = img.data.astype("float64")
```

The main requirement is that the shape of the numpy array coincides with the number of detector channels (i.e. `npx, npy = 981, 1043` for given example).

### Running the fit

To run the fit, the user assembles all components - simulation description and experimental data file - using `FitObjective.addSimulationAndData`.
The complete example can be found in [Real life fit example: experiment at GALAXI]({{% ref-example "fitting/extended/experiment-at-galaxi" %}}).
