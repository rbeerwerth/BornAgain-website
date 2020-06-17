+++
title = "Installation on Windows"
weight = 10
+++

## Installation on Windows

We provide a 64-bit installer package which can be installed into 64-bit Windows 7, 8 and 10 systems.

The BornAgain graphical user interface doesn't require any additional libraries to be installed on the system. You can start using the BornAgain application right after the installation. However, to use the framework via scripting you have to have a Python framework installed. To install and run BornAgain for the first time proceed with the following steps:

- [Installation on Windows](#installation-on-windows)
  - [Use the BornAgain installer](#use-the-bornagain-installer)
  - [Install Python](#install-python)
  - [Troubleshooting](#troubleshooting)

### Use the BornAgain installer

The BornAgain installation package for Windows 7, 8 and 10 can be downloaded from [here]({{% relref "download#Windows" %}}). 
After downloading the installer, double click the `.exe` file and follow the instructions on the screen.

{{< figscg src="/img/bornagainapp_32.png" class="float-left">}} Use the BornAgain icon located on the desktop to start the GUI.
Please refer to [Using graphical user interface]({{% relref "documentation/running-gui" %}}) section for a basic overview of GUI functionality.
<p style="clear: both;">

### Install Python

To be able to run the BornAgain Python examples one has to have a Python interpreter installed on the system together with two additional packages: `matplotlib` and `numpy`.

This set of packages is known as the [SciPy](http://www.scipy.org/) stack
and for most users the easiest way to install it is to download one of the free Python distributions, which includes all the key packages.
The list of possible options is given on the [SciPy installation website](http://www.scipy.org/install.html).

For unexperienced users we recommend the [Anaconda Python Distribution](http://www.anaconda.com) as an all-in-one installer.

+ Please follow the [Install Python with the Anaconda installer]({{% relref "documentation/getting-started/installation/windows/python-anaconda" %}})
step-by-step instruction.

{{% collapse title="For advanced users" id="advanced-users" %}}
Advanced users might find it easier (and much faster) to install Python directly from their <a href="https://www.python.org/downloads">main website</a>
and then install the necessary dependencies `matplotlib` and `numpy` from the command line.
In this case, please follow our [Manual Python installation]({{% relref "documentation/getting-started/installation/windows/python-original" %}}) instruction.
{{% /collapse %}}

### Troubleshooting

If you are experiencing problems while running BornAgain Python scripts please refer to the following tutorial.

+ [Python troubleshooting]({{% relref "documentation/getting-started/installation/windows/python-troubleshooting" %}}).


