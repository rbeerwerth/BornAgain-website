+++
draft = false
title = "Particle distribution"
weight = 40
+++

## Particle distribution

This tutorial gives an overview on how to draw a set of particles whose parameters 
follow a desired distribution.
To fix ideas, let's build the argument around cylindrical particles; 
In this case, the parameters will be *radius*, $r$; and *height*, $h$; the same reasoning 
should apply to other kinds of particles whose parameters differ 
(e.g. an Icosahedron does not have a parameter "radius").


{{< figscg src="cylinder_geometry.png" class="center">}}

### No distribution

In the case in which a particle distribution is not applied, all particles 
are identical; for cylindrical particles, this means having the same radius 
and the same height (the default value is $5 \, \rm{nm}$ for both).


{{< alert theme="info" >}}
One may say that applying no distribution for
a parameter of a set of particles is equivalent to applying a Dirac delta 
distribution to it.
{{< /alert >}}


### Adding irregularities to a set of identical particles

{{< figscg src="adding_irregularities.png" class="center">}}

Let's start with a concrete example. To create a **Gaussian** distribution for
the *radius* of cylindrical particles with the following properties,

   - Mean: $5.0 \, \rm{nm}$,
   - StdDev: $2.0 \, \rm{nm}$,
   - Number of samples: $5$,
   - Sigma Factor: $1.5$,
   - Limits: $(1.0 \, \rm{nm},9.0 \, \rm{nm})$,

one can roughly use the following <a name="recipe">recipe</a>:

{{< highlight python "linenos=table">}}
#Define Gaussian Distribution:
mean_length = 5.0*nm
stdDev_length = 2.0*nm
distribution = ba.DistributionGaussian(mean_length, stdDev_length)

#Carry out the actual value sampling:
parameter_to_modify = "/Particle/Cylinder/Radius"
number_of_samples = 5
sigma_factor = 2.0
limits = ba.RealLimits.limited(1.0*nm, 9.0*nm))
my_parameter_distribution = ba.ParameterDistribution(parameter_to_modify, 
                                                     distribution, 
                                                     number_of_samples, 
                                                     sigma_factor, 
                                                     limits)
    
#Create the particle distribution with the sampled values:
my_particle_distribution = ba.ParticleDistribution(my_particle,
                                                   my_parameter_distribution)
    
# Now we can add this distribution to the particle layout.
{{< /highlight >}}


#### Parameters of a particle distribution

One can choose among six different distributions in order to break the default
regularity of the parameters of the particles. At the same time, each
distribution offers several parameters to tweak:

-----------------------------------

1. <a href="https://en.wikipedia.org/wiki/Raised_cosine_distribution" target="_blank">**Cosine**:</a> 
 - Mean<sup>[1](#evidentMeaning)</sup>.
 - Sigma<sup>[1](#evidentMeaning)</sup>.
 - Number of samples<sup>[2](#numberOfSamples)</sup>.
 - Sigma Factor<sup>[4](#sigmaFactor)</sup>.
 - Limits<sup>[3](#limits)</sup>
 - Distributed parameter<sup>[5](#distributedParameter)</sup>
2. <a href="https://en.wikipedia.org/wiki/Discrete_uniform_distribution" target="_blank">**Gate**:</a> 
 - Min<sup>[1](#evidentMeaning)</sup>.
 - Max[<sup>1](#evidentMeaning)</sup>.
 - Number of samples<sup>[2](#numberOfSamples)</sup>.
 - Distributed parameter<sup>[5](#distributedParameter)</sup>
3. <a href="https://en.wikipedia.org/wiki/Normal_distribution" target="_blank">**Gaussian**</a> (default): 
 - Mean[<sup>1](#evidentMeaning)</sup>.
 - StdDev<sup>[1](#evidentMeaning)</sup>.
 - Number of samples<sup>[2](#numberOfSamples)</sup>.
 - Sigma Factor<sup>[4](#sigmaFactor)</sup>.
 - Limits<sup>[3](#limits)</sup>
 - Distributed parameter<sup>[5](#distributedParameter)</sup>
4. <a href="https://en.wikipedia.org/wiki/Log-normal_distribution" target="_blank">**Log Normal**:</a> 
 - Median<sup>[1](#evidentMeaning)</sup>.
 - ScaleParameter<sup>[1](#evidentMeaning)</sup>.
 - Number of samples<sup>[2](#numberOfSamples)</sup>.
 - Sigma factor<sup>[4](#sigmaFactor)</sup>.
 - Distributed parameter<sup>[5](#distributedParameter)</sup>
5. <a href="https://en.wikipedia.org/wiki/Cauchy_distribution" target="_blank">**Lorentz**:</a> 
 - Mean<sup>[1](#evidentMeaning)</sup>.
 - HWHM<sup>[1](#evidentMeaning)</sup>.
 - Number of samples<sup>[2](#numberOfSamples)</sup>.
 - Sigma factor<sup>[4](#sigmaFactor)</sup>.
 - Limits<sup>[3](#limits)</sup>
 - Distributed parameter<sup>[5](#distributedParameter)</sup>
6. <a href="https://en.wikipedia.org/wiki/Trapezoidal_distribution" target="_blank">**Trapezoid**:</a> 
 - Center<sup>[1](#evidentMeaning)</sup>.
 - LeftWidth<sup>[1](#evidentMeaning)</sup>.
 - MiddleWidth<sup>[1](#evidentMeaning)</sup>.
 - RightWidth<sup>[1](#evidentMeaning)</sup>.
 - Number of samples<sup>[2](#numberOfSamples)</sup>.
 - Limits<sup>[3](#limits)</sup>
 - Distributed parameter<sup>[5](#distributedParameter)</sup>

{{< alert theme="info" >}}
<a name="evidentMeaning">1</a>: The meaning should be evident from the name of the distribution.  
<a name="numberOfSamples">2</a>: The number of different equally spaced values to extract from the distribution.  
<a name="limits">3</a>: Limits can be set in order to avoid taking values outside a given range.  
<a name="sigmaFactor">4</a>: Sigma factor acts as a cutoff scale after which values are not taken into account.  
<a name="distributedParameter">5</a>: A string in the form "/Particle/ParticleType/Parameter".

{{< /alert >}}

BornAgain provides a function to print the list of available particle parameters and their corresponding values:
:
```python
>>print(my_particle.parametersToString())
'/Particle/Abundance':1
'/Particle/PositionX':0
'/Particle/PositionY':0
'/Particle/PositionZ':0
'/Particle/Cylinder/Radius':5
'/Particle/Cylinder/Height':5
```

-----------------------------------

#### Choosing a distribution

A ParticleDistribution is a set of particles in which a given particle
paramenter can take `numberOfSamples` different values.
These values are equally spaced between them and the relative number of
particles with a particular value is proportional to the height of the
chosen distribution.

{{< figscg src="different_distributions.png" class="center">}}

In order to prevent the extraction of unphysical values, one needs
to set limits. For instance, in order to avoid extracting negative 
values for the radius of a cylinder, one can easily set limits to
pass to the ParameterDistribution (line 10 on the [recipe snippet](#recipe) above):

```python
limits = ba.RealLimits.limited(1.0, 9.0))
```

---------------

#### Particle distributions through the GUI

The easiest way of generating a particle distribution from scratch is from the GUI.
After that, one can export the layout as a python script and tweak it to get the desired outcome:

{{< figscg src="distribution_from_GUI.png" class="center">}}

One must note, however, that some functionality is only present through the python API, 
for instance, `linkParameter` is not accessible through the GUI:

```python
# linkParameter allows the height of the cylinders
# to be scaled proportionally to their radii:
par_distr.linkParameter("/Particle/Cylinder/Height")
```

Further details and a complete working script are provided in the tutorial [Cylinders with size distribution](/documentation/examples/embedded-particles/size-distribution/).
