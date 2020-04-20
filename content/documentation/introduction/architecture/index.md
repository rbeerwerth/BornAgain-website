+++
title = "Architectural overview"
weight = 20
+++

## Architectural overview

BornAgain is an open source and a multi-platform framework available in Windows, MacOS and Linux. It is developed in C++ and provided with Python bindings. The overall size of the project is about 180k lines of code.

### The Big Picture

BornAgain is designed to be immediately useful for users with little experience in GISAS simulations while being flexible enough to fulfill requests of advanced users. The figure below represents the set of requirements and practices that have informed our architectural choices.

{{< figure src="nodes_atchitecture_requirements.png" >}}

### General Structure

The framework consists of two shared libraries written in C++, *libBornAgainCore* and libBornAgainFit, and a standalone Graphical User Interface. Thanks to the Python bindings the libraries can be imported into Python as external modules. The library libBornAgainCore defines the data structures and provides the algorithms needed to set up a sample model and to run a simulation. The library libBornAgainFit contains several minimization engines and interfaces to each of them, allowing the user to fit real data with the model previously defined.

{{< figure src="nodes_architecture1.png" >}}

BornAgain depends on a few external and well established open-source libraries: 
[boost](http://www.boost.org/), 
[GNU Scientific Library](http://www.gnu.org/software/gsl/), 
[Eigen](http://eigen.tuxfamily.org/), 
[Fast Fourier Transformation](http://www.fftw.org/) and 
[Qt5](http://www.qt.io/developers/) libraries. They must be installed on the system to run BornAgain on Unix platforms. In the case of Windows and MacOS they are added to the system automatically during the installation of BornAgain.

The fitting library includes a number of minimization algorithms from 
[ROOT Framework](http://root.cern.ch/) from High Energy Particle Physics and from [GNU Scientific Library](http://www.gnu.org/software/gsl/). This code is shipped with the library itself, so no external dependencies are involved.

### Working with BornAgain

In simple cases the user interacts with the framework through a Graphical User Interface.

{{< figure src="nodes_architecture2_640.png" class="center">}}

The advanced approach, allowing much higher levels of flexibility, consists in using BornAgain from Python. The user creates a Python script with a sample description and the simulation settings using the BornAgain API. The user then runs the simulation by executing the script in the Python interpreter. He assesses the simulation results using the graphics or analysis library of his choice, e.g. Python + numpy + matplotlib.

{{< figure src="nodes_architecture3_640.png" class="center">}}

### Object Oriented Approach in Simulation Description

BornAgain uses an object-oriented approach in the simulation description to achieve modularity and extensibility. The user defines the sample structure, the beam and the detector characteristics using building blocks -- classes -- defined in the core libraries of the framework. These building blocks are combined by the user into a hierarchical tree of objects representing the simulation.

For example, to simulate the scattering from a mixture of cylinders and prisms deposited on a substrate, the following tree of objects has to be created.

{{< figure src="nodes_architecture4.png" class="center">}}

The parent MultiLayer object represents the sample and contains three children: the semi-infinite air layer, the semi-infinite substrate layer, and the interface between them. The air layer contains the so-called ParticleLayout object, which holds information about the particles populating the layer and the interference between them. Each particle is fully defined via its children: the material the particle is made of and the form factor representing the particle's shape.

{{< alert theme="info" >}}

The object-oriented approach in software design allows the users to have a much higher level of flexibility in the sample construction. It also decouples the building blocks used in the internal calculations and thereby facilitates the creation of new models, with little or no modification to the existing code.

{{< /alert >}}

In practice, for the users working from the Graphical User Interface the sample construction involves the usage of a drag-and-drop editor, where items of certain types should be placed on the canvas and connected with each other in order to create the sample structure (see figure below, on the left). For the users working from Python, a script similar to the one shown on the right of the figure below has to be created.

{{< figure src="nodes_architecture5.png" class="center">}}

Both approaches are explained in details in the following sections of this documentation.


