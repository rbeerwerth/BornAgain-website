+++
title = "Reflectometry: Fit honeycomb"
weight = 60
+++

### Reflectometry: Fit honeycomb lattice


In this example, we want to demonstrate how to fit a more complex sample.
For this purpose, we utilize the reflectometry data of an
artificial magnetic honeycomb lattice published by A.&nbsp;Glavic et al., in 
[this paper](https://doi.org/10.1002/advs.201700856)

The experiment was performed with polarized neutrons, but without polarization analysis.
Since the magnetization of the sample was parallel to the neutron spin, there is no spin flip
and we apply the scalar theory to this problem.
This is primarily done to speed up computations: when the polarized computational engine is utilized
the fitting procedure takes roughly three times as long.


#### Experimental data

The experimental data consists of four datasets that should be fitted simultaneously.
These datasets arise from the two polarization channels for up and down polarization of the incoming beam
and both of these channels are measured at two temperatures (300K and 150K).

All of this is measured on the same sample, so all parameters are assumed to be the same, 
except the magnetization being temperature dependent.
Therefore, we introduce a scaling parameter for the magnetization as the ratio of the 
magnetizations at 150K and 300K: $M_{s150} = M_{150K} / M_{300K}$.


#### Magnetization model

To model a magnetic material, one can assign a magnetization vector to any material, as is demonstrated 
in the [basic polarized reflectometry tutorial]({{% ref-example "polarized-reflectometry/basic-polarized-reflectometry" %}}).
When a non-vanishing magnetization vector is specified for at least one layer in a sample,
BornAgain will automatically utilize the polarized computational engine.
This leads to lower performance as the computations are more invovled.

In this example, the magnetization is (anti)parallel to the neutron spin and hence we instead parametrize 
the magnetic layers with an effective SLD that is the sum/difference of the nuclear and their magnetic SLD:

$$\rho_\pm = \rho_{\text{N}} \pm \rho_{\text{M}}$$

Here the $+$ is chosen for incoming neutrons with spin up and $-$ is chosen for spin down neutrons.


#### Computational model

We simulate this experiment by bulding a 6 layer model:
As usual the top layer is the vacuum and the bottom layer is a silicon substrate.
On top of the silicon substrate, we simulate a thin oxide layer, where we fit its roughness and thickness
The SLDs of these three layers are taken from the literature and kept constant.

Then we model the lattice structure with a three-layer model: two layers to account for density fluctuations
in $z$-direction and another oxide layer on top.
This lattice structure is assumed to be magnetic and we fit all of their SLDs, magnetic SLDs, 
thicknesses and roughnesses.
The magnetic SLD depends on the temperature of the dataset, according to the scaling described above, where
the $M_{s150}$ parameter is fitted.


All layers are modeled without absorption, i.e. no imaginary part of the SLD.
Ferthermore, we apply a resolution correction as described in [this tutorial]({{% ref-example "reflectometry/tofr-with-resolution" %}}) 
with a fixed value for $\Delta Q / Q = 0.018$.
The experimental data is normalized to unity, but we still fit the intensity, as is necessary due to the resolution correction.


#### Running a computation

In order to run a computation, we define some functions to utilize a common simulation function 
for the two spin channels and both temperatures:

{{< highlight python>}}
def run_Simulation_300_p( qzs, params ):
    return run_simulation(qzs, params, sign=1)

def run_Simulation_300_m( qzs, params ):
    return run_simulation(qzs, params, sign=-1)

def run_Simulation_150_p( qzs, params ):
    return run_simulation(qzs, params, sign=1, ms150=True)

def run_Simulation_150_m( qzs, params ):
    return run_simulation(qzs, params, sign=-1, ms150=True)
{{< /highlight >}}

Here, the given arguments specify whether we want to simulate a spin-up beam (`sign = 1`)
and whether the scaling of the magnetization should be applied (`ms150=True`).
For the latter, `true` means that a dataset at 150K is simulated while `false` 
corresponds to 300K and the scaling parameter is set to unity.

All four reflectivity curves are then computed using:

{{< highlight python>}}
q_300_p, r_300_p = qr( run_Simulation_300_p( qzs, paramsInitial ) )
q_300_m, r_300_m = qr( run_Simulation_300_m( qzs, paramsInitial ) )

q_150_p, r_150_p = qr( run_Simulation_150_p( qzs, paramsInitial ) )
q_150_m, r_150_m = qr( run_Simulation_150_m( qzs, paramsInitial ) )
{{< /highlight >}}

We choose some sensible initial parameters and these yield the following 
simulation result

{{< galleryscg >}}
{{< figscg src="Honeycomb_reflectivity_initial.png" width="350px" caption="Reflectivity with the initial parameters">}}
{{< figscg src="Honeycomb_sld_initial.png" width="350px" caption="SLD profile with the initial parameters">}}
{{< /galleryscg >}}

We have chosen the initial magnetization to be zero, hence there is only a single SLD curve for both spin directions.



#### Fitting

We fit this example by utilizing the differential evolution algorithm from [Scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html).
As a measure for the goodness of the fit, we use the relative difference:

$$\Delta = \sum_{j = 1}^4 \frac{1}{N_j} \sum_{i = 1}^N \left( \frac{d_{ji} - s_{ji}}{d_{ji} + s_{ji}} \right)^2$$

Here the sum over $i$ sums up the fitting error at every data point as usual and 
the sum over $j$ adds the contributions from all four datasets.
This is implemented in the `FitObjective::__call__` function and 
the `FitObjective` object holds all four datasets, and also performs the corresponding simulations.
In the function `run_fit_differential_evolution` this is dispatched to the differential evolution algorithm.

The given uncercainty of the experimental data is not taken into account.



#### Fit Result

As usual, the fit can be run with the following command:
{{< highlight python>}}
python3 Honeycomb_fit.py fit
{{< /highlight >}}
On a four-core workstation, the fitting procedure takes roughly 45 minutes to complete and we obtain the following result:

{{< galleryscg >}}
{{< figscg src="Honeycomb_reflectivity_fit.png" width="350px" caption="Reflectivity with the fit result">}}
{{< figscg src="Honeycomb_sld_fit.png" width="350px" caption="SLD profile with the fit result">}}
{{< /galleryscg >}}


As can be seen from the plot of the SLDs, the magnetization is indeed larger for the measurement at lower temperature, exactly as expected.

{{< highlightfile file="/static/files/python/fitting/ex03_ExtendedExamples/honeycomb/Honeycomb_fit.py" language="python" >}}

{{% filelink file="/static/files/python/fitting/ex03_ExtendedExamples/honeycomb/honeycomb_data.zip" name="Reference data" %}}

