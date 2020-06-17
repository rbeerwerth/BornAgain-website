+++
title = "Installation on MacOS"
weight = 21
+++

## Installation on MacOS

For Mac OS X, we provide a 64-bit binary .dmg installer for High Sierra (10.13) or above and also support build and installation from source. To build BornAgain from source by yourself follow the 
[Installation on Linux]({{% relref "documentation/getting-started/installation/linux-detailed" %}}) section.

The rest of this section explains how to install BornAgain using the `.dmg` installer.

The BornAgain graphical user interface doesn't require any additional libraries to be installed on the system. You can start using the BornAgain application right after the installation. However, to use the framework via scripting you have to have a Python framework installed and configured as explained in the following sections.

To install and run BornAgain for the first time proceed with the following steps:

- [Installation on MacOS](#installation-on-macos)
  - [Run the BornAgain installer](#run-the-bornagain-installer)
  - [Install Python](#install-python)
  - [Configure Python for BornAgain](#configure-python-for-bornagain)
  - [Test the installation](#test-the-installation)

### Run the BornAgain installer

The BornAgain installer can be downloaded from [here]({{% relref "download#MacOS" %}}).
After downloading the installer, double click `.dmg` file to mount it, accept the license agreement and then drag the BornAgain icon onto the Applications shortcut icon.

{{< figscg src="installation_macdmg2.png" class="center">}}

Depending on your system's security settings you might not be able to open BornAgain directly from the Launchpad. In this case you will have to proceed first with the instruction [Open an app from an unidentified developer](http://support.apple.com/kb/PH14369).

At this point you can can already start working with the BornAgain GUI. The rest of tutorial explains how to setup BornAgain for Python.

### Install Python

The current version of BornAgain requires `python, matplotlib, numpy` to be installed on the system. This set of packages is known as the [SciPy](http://www.scipy.org/) stack and for most users the easiest way to install it is to download one of the free Python distributions, which includes all the key packages. The list of possible options is given on the [SciPy installation website](http://www.scipy.org/install.html). You can also directly install Python from their main website [Python](https://www.python.org/downloads/) and then use `pip` to install `matplotlib` and `numpy` as detailed on the [SciPy installation website](http://www.scipy.org/install.html).

{{< alert theme="warning" >}}
While Python comes pre-installed on OS X, it is always quite outdated and we do not recommend to use it together with BornAgain libraries.
{{< /alert >}}

{{% collapse title="More options" id="more-options-1" %}}
If your system is already equipped with [Homebrew](http://brew.sh/) (recommended) or [MacPorts](http://www.macports.org/) package managers, you can certainly make use of it and install Python with all the required modules from the terminal

For Homebrew users:
```
$ brew install python3
$ pip3 install matplotlib numpy
```

For MacPorts users (assuming Python version 3.6)

```
$ sudo port install py36-matplotlib py36-numpy
$ sudo port select --set python python36
```  
{{% /collapse %}}

### Configure Python for BornAgain

To make your Python installation aware of BornAgain, you have to install the BornAgain libraries into the `site-packages` of Python. 
This can be done by running the `bornagain_install_python.py` script from the application bundle. Assuming that BornAgain is installed in the 
`/Applications/BornAgain.app` folder, launch the Terminal application and run the following command:

```
$ python /Applications/BornAgain.app/Contents/libexec/BornAgain-{{< release-string-short >}}/bornagain_python_install.py
```

During the execution of the script, just select the default options by pressing the enter key.
This script will install the BornAgain libraries into the site-packages of the given Python interpreter.

Now check that the installation went successfully by typing

```
$ python -c "import bornagain"
```

If no error is displayed, the installation was successful.

{{% collapse title="More options" id="more-options-2"%}}
If your prefer to install the BornAgain libraries not to the site-packages folder of your Python interpreter, but to a custom folder, check 
the [following instruction]({{% relref "advanced-tips.md" %}}).
{{% /collapse %}}

### Test the installation

{{< figscg src="/img/bornagainapp_32.png" class="float-left">}} Use BornAgain icon from the Launchpad to start GUI.

<p style="clear: both;">

{{< figscg src="/img/python_icon_32.png" class="float-left">}}
Run an example from BornAgain installation directory by typing in the terminal.
<p style="clear: both;">

```
$ python /Applications/BornAgain.app/Contents/share/BornAgain-{{< release-string-short >}}/Examples/python/simulation/ex01_BasicParticles/CylindersAndPrisms.py
```

You should see a scattering image appearing on the screen.
