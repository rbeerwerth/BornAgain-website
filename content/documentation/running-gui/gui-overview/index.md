+++
title = "BornAgain GUI overview"
weight = 20
+++

## BornAgain GUI overview

The basic features of the interface are explained below.
   
   * [Welcome view]({{% relref "#welcome-view" %}}) 
   * [Instrument View]({{% relref "#instrument-view" %}}) 
   * [Sample View]({{% relref "#sample-view" %}}) 
   * [Simulation View]({{% relref "#simulation-view" %}}) 
   * [Jobs View]({{% relref "#jobs-view" %}}) 

### Welcome view

When you start BornAgain GUI, you will be presented with the Welcome View, where you can

   * Create new projects
   * Open recent projects


{{< figscg src="gui_welcomeview_l.png" width="800px" class="center" >}}

You can use the view selector located on the left vertical panel (1) to change to one of the following views.


|  |  |
|:--|:--|
| {{< figscg src="main_welcomeview.png" width="50px" class="center" >}} | Switch to Welcome View |
| {{< figscg src="main_instrumentview.png" width="50px" class="center" >}} | Define the instrument geometry: beam and detector parameters |
| {{< figscg src="main_sampleview.png" width="50px" class="center" >}} | Build the sample |
| {{< figscg src="main_importview.png" width="50px" class="center" >}} | Import experimental data to fit |
| {{< figscg src="main_simulationview.png" width="50px" class="center" >}} | Run a simulation |
| {{< figscg src="main_jobview.png" width="50px" class="center" >}} | Switch to see job results, tune parameters in real time, fit the data |
|  |  |


### Instrument View

The Instrument View is used to create new scattering instruments and adjust their settings. The view consists of the instrument selector located on the left (1) and the instrument settings window located on the right (2).

{{< figscg src="gui_instrumentview_l.png" width="800px" class="center">}}

On the instrument settings window (2) you can modify the settings of the currently selected instrument:

   * The name of the instrument
   * The beam parameters
   * The detector parameters
   * Parameters for polarization analysis
   * Background


### Sample View

The Sample View allows you to design the sample via a drag-and-drop interface. It consists of five main parts

   * The item toolbox (1) contains a variety of items for building a sample
   * The sample canvas (2) is used to assemble the sample
   * The sample tree view (3) represents the hierarchy of the objects composing the sample
   * The property editor (4) can be used to edit the parameters of the currently selected item
   * The script view (5) shows the automatically generated Python script


{{< figscg src="gui_sampleview_l.png" width="800px" class="center">}}

> The sample constructed in this figure comprises a substrate on which are deposited cylindrical particles. The interference between scattered waves is provided via the two-dimensional paracrystal interference function. The property editor shows the parameters of the currently selected cylindrical particles (radius and height of cylinders, their material, the particles position and abundance).

The sample is constructed by dragging items from the item toolbox (1), dropping them on the sample canvas (2), connecting the items of the appropriate types together and adjusting their properties, if necessary, using the property editor (4). In particular, the sample shown on this plot was constructed using the following steps:

   * A Multilayer item was taken from the item toolbox and placed on the sample canvas
   * Two layer items were taken from the item toolbox and placed on top of the multilayer
       * The materials of the top and bottom layers were changed from the default ones using the property editor
   * A ParticleLayout item was taken from the item toolbox, placed on the sample canvas and connected with the top layer
   * Cylinders were dropped on the sample canvas and connected with the ParticleLayout
       * The material of the particles was changed from the default one using the property editor
   * The interference function representing a 2D paracrystal was placed on the sample canvas and connected with the ParticleLayout item

{{< alert theme="info" >}}
**Note**

The sample canvas can have any number of multilayers. If this is the case, during the configuration of the simulation the user will have to choose which multilayer to simulate. The multilayer is considered as valid for the simulation, if it contains at least one layer.
{{< /alert >}}

### Simulation View

The Simulation View contains three important elements

   * The data selection box for selecting the instrument and the sample to simulate (1)
   * The Simulation Parameters box for changing the main simulation parameters (2)
   * The `Run Simulation` and `Export to Python Script` buttons (3)

{{< figscg src="gui_simulationview_l.png" width="800px" class="center">}}

The names of the defined instruments and samples are displayed in the Data Selection box (1). There, the user can select a combination for running a simulation.

Clicking on the `Run Simulation` button (3) immediately starts the simulation. When completed, the current view is automatically switched to the Jobs View showing the simulation results. This behaviour can be modified by changing Run Policy in (2).

### Jobs View

The Jobs View displays the results of the simulation. It has two different presentations called

   * [Job View Activity]({{% relref "#job-view-activity" %}})
   * [Real Time Activity]({{% relref "#real-time-activity" %}})

Job View Activity is shown by default.

#### Job View Activity

The layout of the Job View Activity consists of five elements

   * The jobs selector widget (1) for selecting the specific job to be displayed
   * The job properties widget (2) contains basic information about the currently selected job
   * The intensity data widget (3) shows the intensity data of the currently selected job
   * The toolbar (4) contains a set of control elements for the job selector and the intensity data widgets. In the right corner of the toolbar one can switch to the Projections widget.
   * A control element on the right of the bottom toolbar (5) allows switching between Job View, Real Time View and Fitting activities. 

{{< figscg src="gui_jobview_l.png" width="800px" class="center">}}

> The two completed jobs can be seen in the job selector widget (1), with job2 currently selected and displayed.

{{< alert theme="info" >}}
 The intensity image in widget (3) offers several ways of interaction:

   * Using the mouse wheel to zoom in and out
   * Dragging the color palette on the right of the image to change the min, max range of the z-axis
   * The toolbar (4) on top of the intensity data widget gives access to more options via Plot Properties (left button) and Projections (right control)
{{< /alert >}}

{{< figscg src="gui_jobview_proj_l.png" width="800px" class="center">}}

> The image represents the results of job2 with Projections (1) and Plot Properties (2) widgets switched On. The type of colorbar gradient is changed from the default `Jet` to `Cold`.

#### Real Time Activity

The second layout of the Job View is called the Real Time Activity. It can be switched on by selecting the appropriate item in the box located in the right corner of the bottom toolbar (1).

{{< figscg src="gui_jobview_realtime_l.png" width="800px" class="center">}}

> The layout of the Real Time View consists of the Intensity Data widget on the left (2), and an additional parameter tree located on the right (3).

The parameter tree represents all parameters that have been used during the construction of the scattering instrument and the sample. Each displayed parameter value can be adjusted using a slider. The simulation will run in the background and the Intensity Data widget will be constantly updated reflecting the influence of the given parameter on the simulation results.

{{< alert theme="info" >}}
**Note**

The Real Time View works smoothly only for simple geometries, when the simulation requires fractions of a second to run. For more complex geometries, demanding more CPU power, the user will see a progress bar and any movements of the slider will not have a direct influence on the Intensity Data widget. In this case the user may try to speed up the simulation by decreasing the number of detector channels in the Instrument View and submitting a new job by running the simulation from the Simulation View.

{{< /alert >}}


{{< alert theme="warning" >}}
**Important**

The jobs in the Jobs View are completely isolated from the rest of the program. Any adjustments of the sample parameters in the Sample View or the instrument parameters in the Instrument View won't have any influence on the jobs already completed or still running in the Jobs View. Similarly, any parameter adjustments made in the parameter tree (3) will not be propagated back into the Sample or Instrument Views.

{{< /alert >}}
