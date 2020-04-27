+++
title = "Fitting in the GUI"
weight = 30
+++

## Fitting in the GUI

This tutorial gives a brief overview of the fitting functionality in the GUI, introduced in Release-1.6 (June, 2016).

In the future the following tutorial will be revised to reflect the actual status of the fitting in the GUI.

As a first example, this tutorial will focus on fitting data simulated with BornAgain itself. More complex fitting examples will be considered in coming releases. This tutorial is organized as follows:

   * [Preparing the "experimental" data for fitting.]({{% relref "#1-preparing-data-to-fit" %}})
   * [Importing "experimental" data in BornAgain]({{% relref "#2-importing-the-experimental-data" %}})
   * [Setting up the fit job]({{% relref "#3-setting-up-the-fit-job" %}})
   * [Running the fit]({{% relref "#4-running-the-fit" %}})

{{< notice note >}}
Although this tutorial consideres GISAS data fitting, the steps described are
equally applicable to fitting reflectometry or off-specular data (after choosing
the appropriate type of instrument).
{{< /notice >}}

### 1. Preparing data to fit

Let's construct a simple sample - a two-layer system (air, substrate), with cylindrical particles sitting on top of the substrate. The height and radius of the cylindrical particles are both set to 5 nm.

{{< figscg src="tutorial_fitintro01_sample.png" width="800px" class="center" >}}

For the next step we switch to the Simulation View and simply run the simulation using the Default GISAS Instrument.

{{< figscg src="tutorial_fitintro02_simulation.png" width="800px" class="center" >}}

As soon as the simulation is complete, the interface automatically switches to JobView, which displays the simulated intensity map. This result can be saved as a file called `mydata.int` in BornAgain ASCII format (*.int). This file will be later used to import "experimental" data for the fitting.

{{< figscg src="tutorial_fitintro03_export.png" width="800px" class="center" >}}

### 2. Importing the "experimental" data

Switch to the Import View. At the beginning it is empty since there are no real data samples loaded yet. Push the "Import" button and select the file `mydata.int` you've created earlier.

{{< figscg src="tutorial_fitintro04_import.png" width="800px" class="center" >}}

The data will be loaded into BornAgain and presented in the Import Data view as shown below.

{{< figscg src="tutorial_fitintro05_import_orig.png" width="800px" class="center" >}}

### 3. Setting up the fit job

It is now time to setup our first fitting job. Switch back to the Simulation View. In the "Select Real Data" field select the name of the real dataset you've just imported. Now, the data selection box states, as shown below, that an instrument "Default GISAS" will be used together with the sample "example01", which represents the multilayer with cylinders that we've constructed in section 1, in order to fit the dataset "mydata". Click on the "Run Simulation" button to start the simulation.

{{< figscg src="tutorial_fitintro06_settingup.png" width="800px" class="center" >}}

Once the simulation is complete, the display is once again switched to the JobView mode. Our current job - "job2" - is now ready for fitting. Use the selector in the bottom right corner to switch the type of activity from "Job View Activity" to "Fitting Activity" (indicated in the figure below). By default, when real data was selected in Simulation view, the current view will already be switched to Fitting Activity.

{{< figscg src="tutorial_fitintro07_joview.png" width="800px" class="center" >}}

In the Fitting Activity view (below) the following elements are visible

   * (1) An intensity map of the selected "Real Data".
   * (2) A simulated intensity map of the job itself
   * (3) A relative difference map between (1) and (2)
   * (4) A plot showing how the fit is progressing
   * (5) A sample parameter tuning widget
   * (6) A window to display fitting parameters
   * (7) The presentation selector, which allows to switch quickly between views from current "Fit Data" to standard "Color Map"

{{< figscg src="tutorial_fitintro08_fitactivity.png" width="800px" class="center" >}}

As you may see, the relative difference map (3) shows that there is actually no difference between "experimental" and "simulated" data. This is normal, since our "experimental" data was generated using the same sample/instrument settings as the simulation. Or, in other words, at this point no fitting is required - our sample parameters perfectly describe the "experimental" data. In the following paragraph we are going to change that.

#### 3.1 Setting up the fit job (cont.)

Using the parameter tuning widget on the right we set new values for two sample parameters: the cylinder radius and the cylinder height. This leads to an automatic re-simulation and update of the views: the simulated intensity map has changed and doesn't coincide with the "experimental" data map anymore. The relative difference map also shows this difference.

{{< figscg src="tutorial_fitintro08_screwingup_orig.png" width="800px" class="center" >}}

These will be the initial conditions of our fitting. The real data was simulated using values for the cylinder's `height = radius = 5 nm`. The simulated intensity map is obtained for the cylinder's `height = radius = 10 nm`. We are going to define two fit parameters for the cylinder's radius and height. Our final goal is to find the original values, i.e. `height = radius = 5 nm`.

To create the fit parameters, drag-and-drop "radius" and "height" from the parameter tuning widget to the fit parameters widget below (indicated in the figure below).

{{< figscg src="tutorial_fitintro09_fitpar_orig.png" width="800px" class="center" >}}

Every fit parameter has the following fields

   * Fit parameter name
   * Fit parameter type (limited, free, fixed, etc)
   * Fit parameter starting value
   * Fit parameter limits
   * A long string showing to which sample parameter the given fit parameter is linked

Define the fit parameter limits: `min = 3 nm`, `max = 15 nm` and `starting value = 10 nm`.

### 4. Running the fit

Push the "Run" button at the bottom of the "Fit Parameters" view. The fitting should start. Using the slider at the bottom area one can change the rate of updating the plot. The plot below shows the view after the fitting was completed. The green histogram in the lower right corner shows how $\chi^2$ evolves as a function of the number of fit iterations.

{{< figscg src="tutorial_fitintro10_runfit.png" width="800px" class="center" >}}
