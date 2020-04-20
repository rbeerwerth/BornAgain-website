+++
title = "Manual Python installation (advanced)"
weight = 20
+++

## Manual Python installation  (advanced)

In this instruction we explain how to install Python and all the necessary Python packages
to be able to run BornAgain simulations via Python scripting.

We advertise this as an instruction for advanced users. However, it provides a much more lightweigth and cleaner environment than the bulky Python installation using Anaconda explained [here]({{% relref "documentation/getting-started/installation/windows/python-anaconda" %}}).


## Download Python from the official web site

Download and install Python {{% recommended-python %}} 64-bit version from [official site](https://www.python.org/download). 

This is actually the most complicated step since the
default download button leads to a download of the 32-bit version which will not work with BornAgain.
To download the correct version, click on the `Windows` link marked on sthe creenshot below.

{{< figscg src="python-download1.PNG" class="center" width="450px">}}

On the new page you will find a list of `Windows` installers. Select the `Windows x86-64 executable installer`. Make sure that you are in
the section corresponding to Python {{% recommended-python %}}.

{{< figscg src="python-download2.PNG" class="center" width="450px">}}


## Run the installer

Run the installer. Please select `Add Python 3.7 to PATH` at the bottom of the screen and then push `Install Now`.

{{< figscg src="python-install-step2.PNG" class="center" width="450px">}}

Adding Python to the PATH is an important step to be able to use Python from the command shell and various code editors.

## Install the required Python packages

BornAgain requires `matplotlib` and `numpy` to be installed in site-packages of your Python distribution.
Start a Windows command shell by typing `cmd` in the Windows `Start menu`.

{{< figscg src="python-install-step3.PNG" class="center" width="450px">}}

In the new opened window type

```
pip install matplotlib numpy
```

`Pip` is a package manager which is used in the Python world to manage packages in an existing Python installation.
The command `pip install matplotlib numpy` starts the installation of the `matplotlib` library for plotting and the `numpy` library for matrix manipulation.

{{< figscg src="python-install-step4.PNG" class="center" width="450px">}}

{{< alert theme="info" >}}
If Windows complains that the `pip` command is not found on the system, this means that you have forgotten to add Python to the PATH as explained above.
{{< /alert >}}

When the installation is complete the window should look like the screenshot below.

{{< figscg src="python-install-step5.PNG" class="center" width="450px">}}

At this point Python and all the required dependencies are successfully installed.

{{< alert theme="info" >}}
In this scenario you have installed Python to your local home directory and _you have added_
Python to the system PATH. This approach has the advantage that your Python is integrated with the Windows installation and
you can use it from any Windows command shell or use it together with any integrated development environment, like `VSCode` or `PyCharm`. 

The disadvantage is that this approach can be safely used only if you have a single Python installation on your system. The setup of multiple Python versions on a system goes far beyond the scope of this tutorial.
{{< /alert >}}


### Validate Python and BornAgain installation

To validate that BornAgain is working nicely together with the installed Python,
start a Windows command shell by typing `cmd` in the Windows `Start menu`.
To validate the BornAgain installation, type 

+ `python` to start the Python interpreter
+ `import bornagain` as a first command
+ `print(bornagain.GetVersionNumber())` to print the BornAgain version number on the screen.

{{< figscg src="python-install-step6.PNG" class="center" width="450px">}}

If no errors are displayed and you also see the BornAgain version number printed on the screen, your installation is correct.


### Running BornAgain examples

To run a BornAgain example from the command line, launch a command shell again and
type (or copy-and-paste) the command below to see a scattering image appearing on the screen.

```
python C:/BornAgain-{{< release-string >}}/Examples/python/simulation/ex01_BasicParticles/CylindersAndPrisms.py
```

{{< figscg src="python-install-step7.PNG" class="center" width="450px">}}

The used path implies that BornAgain was installed to the default location. If this was not the case, you will have to adjust the path to the BornAgain Python example accordingly.

{{< alert theme="info" >}}
`Tip:` while typing long commands in the command shell you can push the `TAB` key and Windows will attempt to autocomplete long directory names.
{{< /alert >}}

This kind of manual launching of Python scripts is not very convenient for regular usage and should be considered rather as another validation step.

### Running BornAgain examples using a Python IDE

We have provided  two more step-by-step tutorials to explain how to run BornAgain examples in a convenient manner using one of two integrated development environments.

+ [Using the VSCode editor.]({{% relref "documentation/getting-started/installation/windows/python-original/python-vscode" %}})
+ [Using the PyCharm IDE.]({{% relref "documentation/getting-started/installation/windows/python-original/python-pycharm" %}})
