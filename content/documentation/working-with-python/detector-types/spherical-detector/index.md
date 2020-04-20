+++
title = "Spherical detector"
weight = 10
+++

## Spherical detector

This shape of detector represents a portion of a sphere, defined by the range of $\phi$ and $\alpha$ angles as shown in the plot below. The sphere has its center located at the origin of the sample coordinate system.

{{< figscg src="spherical_detector.png" width="500" class="center">}}

A GISAS or off-specular simulation creates a spherical detector by default. To set its parameters the method `setDetectorParameters` should be used

```python
setDetectorParameters(n_phi, phi_min, phi_max, n_alpha, alpha_min, alpha_max)
"""
Sets detector parameters using angle ranges
 
n_phi     : number of phi-axis bins
phi_min   : low edge of first phi-bin
phi_max   : upper edge of last phi-bin
n_alpha   : number of alpha-axis bins
alpha_min : low edge of first alpha-bin
alpha_max : upper edge of last alpha-bin
"""
```

All angles are expressed in radians. For convenience, a special `deg` multiplier can be used to define the detector range directly in degrees. For example, the following code snippet

```python
simulation = GISASSimulation()
simulation.setDetectorParameters(20, -1.0*deg, 1.0*deg, 10, 0.0*deg, 1.0*deg)
```

will create a detector plane with a total number of bins equal to 200 and with a fixed bin size equal to `0.1*deg` along both directions

{{< figscg src="phi_alpha_plane.png" width="600" class="center">}}

Here, the vertical and horizontal lines denote bin boundaries while blue dots show the bin centers. During the simulation, the bin intensity will be calculated for values of $\phi_f$ and $\alpha_f$ corresponding to the bin centers and then normalized to the bin area.

{{< alert theme="info" >}}
**Note**

`GISASSimulation` has a special setting to calculate the intensity in a bin as the 2D integral along the detector bin area. This mode will be explained elsewhere.

{{< /alert >}}

### Alternative way to create SphericalDetector

The detector can be initialized separately and then later assigned to the simulation object as shown in the script below. The results will be exactly the same as in the previous example

```python	
detector = SphericalDetector(20, -1.0*deg, 1.0*deg, 10, 0.0*deg, 1.0*deg)
simulation = GISASSimulation()
simulation.setDetector(detector)
```

### Spherical detector with variable bin size

It is possible to create a spherical detector with a non-equidistant binning. This is done by creating custom axes and using them as `SphericalDetector` initializers.

There are two basic axis types in BornAgain: `FixedBinAxis` and `VariableBinAxis`. Their signatures are shown in the code snippet below.

```python
FixedBinAxis(name, nbins, start, end)
"""
Constructs an axis with fixed bin size
 
name  : The name of the axis
nbins : Number of axis bins
start : Low edge of first bin
end   : Upper edge of last bin
"""
 
VariableBinAxis(name, nbins, bin_boundaries)
"""
Constructs an axis with variable bin size
 
name           : The name of the axis
nbins          : Number of axis bins
bin_boundaries : Array of size nbins+1 containing low-edges for each bin and upper edge of last bin.
"""
```

In the following example we create a `SphericalDetector` with two axes: an x-axis with variable bin size and a y-axis with fixed bin size. The code and resulting detector plane are shown below.

```python
nxbins = 13
xedges = [-1.0*deg, -0.7*deg, -0.5*deg, -0.3*deg, -0.2*deg, -0.1*deg, -0.025*deg, 0.025*deg, 0.1*deg, 0.2*deg, 0.3*deg, 0.5*deg, 0.7*deg, 1.0*deg]
xaxis = VariableBinAxis("my-x-axis", nxbins, xedges)
 
yaxis = FixedBinAxis("my-y-axis", 10, 0.0, 10.)
 
detector = SphericalDetector()
detector.setDetectorAxes(xaxis, yaxis)
 
simulation = GISASSimulation()
simulation.setDetector(detector)
```

{{< figscg src="phi_alpha_plane_variable.png" width="600" class="center">}}
