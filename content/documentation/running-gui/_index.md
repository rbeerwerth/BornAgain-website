+++
title = "Graphical user interface"
weight = 30
+++

## Running BornAgain through the GUI

BornAgain comes with a graphical user interface (GUI).
Based on the library Qt5, it has a native look and feel
under all three supported operating systems. It allows
users to view experimental and simulated data, to set up
and parameterize physical models, and to run fits.

A graphical sample editor allows users to assemble
multilayer models by drag and drop. Model components like
embedded particles or inter-particle correlation functions are
represented by boxes that are connected by flexible lines to
their parent components. Simultaneously, the real-space
structure of the sample, or any of its components, can be
shown in an interactive 3D visualization. This provides
users with feedback as to whether the model, constructed
in abstract terms in the sample editor, corresponds to their
actual intentions. Moreover, a real-space representation
can be helpful when communicating scientific results to
audiences that are not familiar with the reciprocal-space
thinking of scattering practitioners.

All model parameters can also be seen and set from a tree
view. To explore their impact upon the simulated GISAS
pattern, it is possible to modify parameter values with sliders.
Unless the model is excessively computing intensive, the
outcome view is kept up to date without noticeable delay.
All model and parameter choices made in an interactive
GUI session can be stored in XML and can be reloaded in
another GUI session. They can also be stored as a Python
script, which can then be run from the command line,
independently of the GUI. This helps users who reach the
limits of GUI functionality to get started with using BornAgain
from Python, since it is much easier to edit a given script
than to write one from scratch.

{{< alert theme="warning" >}}
**Backward compatibility**

We do not ensure that newer versions of BornAgain are able
to read older versions of GUI project files. Such backward
compatibility of project files will come at the earliest
with release 2.0.
{{< /alert >}}

{{% children  %}}
