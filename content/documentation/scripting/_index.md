+++
title = "Python scripting"
weight = 40
+++

## Introduction to Python scripting

The Python API enables users to run simulations and fits
from the high-level programming language Python. This can
be done either in interactive sessions (possibly in a Jupyter
notebook) or by executing a script. Once Python and
BornAgain are installed on a computer, the simple command
```
import bornagain as ba
```
in a Python session or script is
sufficient to make all the functionality of BornAgain available
through function calls with the prefix `ba`.

The [examples]({{% relref "documentation/examples" %}})
section of this online documentation comprises numerous example
scripts. For each script, the implemented model is explained
and the obtained simulation result is shown. The same scripts
are also contained in the BornAgain source tree. Typically,
users will start from some example script and then gradually
adapt it to their own needs.
To get started with scripting it is also possible to build a
model in the graphical user interface (GUI) and export it as
a Python script.

Scripting is more versatile than the GUI and provides functionality
that is not yet available in the GUI, or never will be. For instance,
one can
* set up arbitrarily complicated combined and constrained fits;
* batch process huge data sets;
* react to a simulation or fit outcome through control clauses;
* extend the functionality of the BornAgain core, for instance
  by adding particle form factors or correlation functions.

The user creates a Python script with a sample description and
simulation settings. The user then runs the simulation by executing the script in the Python interpreter and assesses the simulation results using the graphics or analysis library of his choice, e.g. `Python+numpy+matplotlib`.

{{< figscg src="nodes_pycharm_ide.png" width="500" class="center">}}

At this point we assume that the framework is installed as explained in the
[Installation instructions]({{% relref "documentation/getting-started/installation" %}})
and that the user is able to run Python examples from the installation directory.
In the next sections we go through a complete example of simulation and fitting using BornAgain.

{{% children %}}
