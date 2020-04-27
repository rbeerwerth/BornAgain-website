+++
title = "Material types"
weight = 20
+++

## Material types

The refractive properties of a homogeneous `Material` can be specified
through two different functions:
* `HomogeneousMaterial`, based on the refractive index,
* `MaterialBySLD`, based on the scattering length density.

### Material by refractive index

A `Material` can be created through

{{< highlight python >}}

magnetization = ba.kvector_t(1.0, 0.0, 0.0)
<material> = ba.HomogeneousMaterial("name", delta, beta, magnetization)

{{< /highlight >}}

where `name` is the arbitrary name of the material associated with its complex refractive index $n = 1 - delta + i \cdot beta$.
`magnetization` defines a 3D magnetization vector (in A/m).
The variable `<material>` is later used when referring to this particular material.

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

The first of aforementioned calculators provides SLD values in inverse square angstroms,
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

### Limitations

{{< alert theme="warning" >}}

Although `MaterialBySLD` and `HomogeneousMaterial` are interchangeable in the case of neutron experiments with fixed wavelength,
they must not be used together in one sample because of different behavior inside BornAgain. If they are, an exception will be thrown
by `Simulation` class:
```bash
terminate called after throwing an instance of 'std::runtime_error'
  what():  Error in Simulation::prepareSimulation(): non-default materials of several types in the sample provided
```

{{< /alert >}}

`HomogeneousMaterial` uses refractive index directly, thus it is equally suitable for simulations with X-ray or neutron
probe. On the other hand, refractive index does depend on beam wavelength, thus using `HomogeneousMaterial` can lead to incorrect simulation results in the case
of significant beam divergence in wavelength or when used for time-of-flight experiments.

`MaterialBySLD` is intended for the experiments with neutron probe and provides correct values of refractive index for a wide range
of wavelengths. For this reason, `MaterialBySLD` is recommended to use in the case of time-of-flight experiments or standard neutron experiments
with significant beam divergence in wavelength.

However, calculation of refractive index with `MaterialBySLD` in BornAgain neglects incoherent scattering cross-section, thus providing
incorrect $\Im(n)$ in the case of incoherent scattering term being larger or comparable with the absorption term:

$$\sigma\_\{abs\} \cdot \lambda \geq \sigma\_\{inc\} \lambda,$$

where $\lambda$ is the basic beam wavelength, $\sigma\_\{abs\}$ - absorption cross-section, $\sigma\_\{inc\}$ - incoherent scattering cross-section.

Even in this case `MaterialBySLD` can be used for simulations, since usually $sld\_\{imag\} \ll sld\_\{real\}$, and incorrect imaginary term of refractive index does not
significantly affect the simulation result.
