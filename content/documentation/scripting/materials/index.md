+++
title = "Materials"
weight = 20
+++

## Materials

The refractive properties of a homogeneous `Material` can be specified
through two different functions:
* `HomogeneousMaterial`, based on the refractive index,
* `MaterialBySLD`, based on the scattering length density (SLD).

`HomogeneousMaterial` is equally suitable for X-rays or neutrons.
However, it does not account for the wave-length dependence of the refractive index.
This leads to incorrect results if there is too much spread in the incoming wavelength,
as is regularly the case in neutron time-of-flight experiments.

`MaterialBySLD` is intended for neutron experiments with significant wavelength spread.
Refractive indices as function of wavelength are computed internally from constant SLDs.

### Material by refractive index

A `Material` can be created through

{{< highlight python >}}

magnetization = ba.kvector_t(1.0, 0.0, 0.0)
<material> = ba.HomogeneousMaterial("name", delta, beta, magnetization)

{{< /highlight >}}

where `name` is the arbitrary name of the material associated with its complex refractive index $n = 1 - \delta + i\beta$.
The `magnetization` argument is a 3D vector (in A/m).
The return value `<material>` is later used when referring to this particular material.

`magnetization` can be omitted in material construction. It is assumed to be zero then:

{{< highlight python >}}

<material> = ba.HomogeneousMaterial("name", delta, beta)

{{< /highlight >}}

### Material by scattering length density

A `Material` can also be created through

{{< highlight python >}}

<material> = ba.MaterialBySLD("name", sld_real, sld_imag, magnetization)

{{< /highlight >}}

or, omitting `magnetization` again,

{{< highlight python >}}

<material> = ba.MaterialBySLD("name", sld_real, sld_imag)

{{< /highlight >}}

Here `sld_real` and `sld_imag` are the real and imaginary parts
of the material scattering length density (SLD) according to the following convention:

$$SLD = sld\_\{real\} - i \cdot sld\_\{imag\}$$

SLD values for a wide variety of materials can be calculated
with numerous online SLD-calculators, e.g. these ones:

* [sld-calculator.appspot.com](https://sld-calculator.appspot.com/)
* [SLD calculator by NIST](https://www.ncnr.nist.gov/resources/activation/)

The first of these returns values in inverse square angstroms,
which are also the input units for `MaterialBySLD`.
Thus the SLD values found with the calculator
can be directly copied and pasted into a BornAgain script.

### Default = Vacuum

Both `HomogeneousMaterial` and `MaterialBySLD` can be created with empty constructors:

{{< highlight python >}}

<material> = ba.HomogeneousMaterial()
<material2> = ba.MaterialBySLD()

{{< /highlight >}}

In this case the "default" material is created, i.e. a material with the name `vacuum`, zero SLD/refractive index and zero magnetization.

### Restrictions and Limitations

{{< alert theme="warning" >}}
Although `MaterialBySLD` and `HomogeneousMaterial` are interchangeable in the case of neutron experiments with fixed wavelength,
they must not be used together in one sample.
Otherwise an exception will be thrown:
```bash
terminate called after throwing an instance of 'std::runtime_error'
  what():  Error in Simulation::prepareSimulation(): non-default materials of several types in the sample provided
```
{{< /alert >}}

{{< alert theme="warning" >}}
`MaterialBySLD` does not account for causes of damping other than nuclear absorption.
In particular, incoherent and inelastic scattering are neglected.
Usually, such extra damping would change the imaginary part of the refractive index
only little compared with the real part;
neglecting it therefore should have no big effect upon simulation results.
{{< /alert >}}
