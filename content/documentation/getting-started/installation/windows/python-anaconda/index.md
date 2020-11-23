+++
title = "Install Python with the Anaconda installer (recommended)"
weight = 10
+++

## Install Python with the Anaconda installer (recommended)

In this tutorial we explain how to install Python together with all possible science-related packages
using the Anaconda Python distribution and how to run BornAgain in the `conda` environment.

### Download the Anaconda installer

Download the Anaconda distribution for Windows from the [Official website](https://www.anaconda.com/distribution/).
Please make sure, that

+ you are downloading the Windows version,
+ you are downloading the 64-bit version,
+ your Anaconda Python version major number is the same as the version of Python specified in the BornAgain installer name.

This means, that for BornAgain installed using the installer with the name `{{% recommended-wininstaller %}}` 
you need `Anaconda Python {{% recommended-python %}} 64-Bit version`.

{{< figscg src="anaconda-install-step0.PNG" class="center" width="450px" caption="Anaconda website download page">}}

### Run the Anaconda installer

{{< figscg src="anaconda-install-step1.PNG" class="center" width="450px" caption="Run the installer">}}

{{< figscg src="anaconda-install-step2.PNG" class="center" width="450px" caption="Agree with installation option 'Just Me'">}}

{{< figscg src="anaconda-install-step3.PNG" class="center" width="450px" caption="Agree with the default installation folder">}}

{{< figscg src="anaconda-install-step4.PNG" class="center" width="450px" caption="Agree with advanced options defaults">}}

Push the `Install` button, which will start a lengthy installation process.

### Select to install the VS code editor

Anaconda nowadays comes with a nice free code editor from Microsoft and we recommend to install it during the next installation step.
An editor provides Python code highlighting and is extremely handy in Python code development, as well as for any script-related or code-related activity (e.g. Latex, web development, etc).

{{< figscg src="anaconda-install-step5.PNG" class="center" width="450px">}}

Push the button `Install Microsoft VSCode` and after this installation is complete you are basically done.

{{< figscg src="anaconda-install-step6.PNG" class="center" width="450px">}}

{{< alert theme="info" >}}
In this scenario you have installed Anaconda to your local home directory and you didn't change
any system variables. This approach has the advantage that you can't break any other software and/or Python installations existing on your system.

The disadvantage is that your Anaconda is not integrated with the Windows installation. You will have to use the `Anaconda command prompt` and `Anaconda navigator`
to have the correct Python set up. Please see below.
{{< /alert >}}

### Validate Anaconda + BornAgain installation

To validate that BornAgain is working together with the installed Anaconda, launch `Anaconda Prompt` from the Start menu.
Just click `Start menu` and start to type `Anaconda...` unless `Anaconda Prompt` appears in the options already.

{{< figscg src="anaconda-running-step1.PNG" class="center" width="450px">}}

A new Anaconda command shell will appear. To validate the BornAgain installation, start to type

+ `python` to start the Python interpreter
+ `import bornagain` as the first command
+ `print(bornagain.GetVersionNumber())` to print the BornAgain version number on the screen.

{{< figscg src="anaconda-running-step2.PNG" class="center" width="450px">}}

If no errors will come up, and you also see the BornAgain version number printed on the screen, your installation is working.

### Running the BornAgain examples

To run a BornAgain example from the command line, launch `Anaconda Prompt` and
type (or copy-and-paste) the command below to see a scattering image appearing on the screen.

```
python C:/BornAgain-{{< release-string >}}/Examples/python/simulation/ex01_BasicParticles/CylindersAndPrisms.py
```

{{< figscg src="anaconda-running-step3.PNG" class="center" width="450px">}}

The used path implies, that BornAgain was installed to the default location. If this was not the case, you will have to adjust the path to the BornAgain Python example accordingly.

{{< alert theme="info" >}}
`Tip:` while typing long commands in the command shell you can push the `TAB` key and Windows will attempt to autocomplete long directory names.
{{< /alert >}}

This kind of manual launching is not very convenient for regular usage and should be considered rather as yet another validation step.

### Running BornAgain examples using the VSCode editor

To run BornAgain scripts in a convenient manner, one has to use one of the Python integrated development environments (`Spyder`, `PyCharm`, `VSCode`). 
Our own choice is to use `VSCode` - a light-weighted but powerful free code editor from Microsoft.

To run the VSCode editor one has to start it using `Anaconda navigator`. Start `Anaconda navigator` from the Windows start menu, and then start `VSCode` editor from
the navigator.

{{< figscg src="anaconda-running-step4.PNG" class="center" width="450px">}}

The Anaconda navigator is an important component of the Anaconda eco-system. In the given example it not only starts the `VSCode` editor, but also defines the correct environment variables to make `VSCode` work correctly in the `conda` environment.

{{< alert theme="info" >}}
Always use the `Anaconda navigator` to start `VSCode` in the correct environment.
{{< /alert >}}

### Add BornAgain examples to VSCode

By default, the `VSCode` editor opens a welcome screen. 
Add the folder with the BornAgain Python examples to the workspace
by clicking `Add workspace folder` as shown in the screenshot below.

{{< figscg src="anaconda-running-step5-vscode.PNG" class="center" width="450px">}}

Choose the directory with the BornAgain Python examples at `C:/BornAgain-{{< release-string >}}/Examples/python`

{{< figscg src="anaconda-running-step6-vscode.PNG" class="center" width="450px">}}

Choose any example and run it in terminal using the right mouse button.

{{< figscg src="anaconda-running-step7-vscode.PNG" class="center" width="450px">}}

The script will be executed in a terminal embedded in `VSCode` and a scattering image will appear on the screen after the simulation has completed.

{{< figscg src="anaconda-running-step8-vscode.PNG" class="center" width="450px">}}

### Troubleshooting

If you are experiencing problems in running a BornAgain Python script, please make sure that

+ the BornAgain installation version matches the Anaconda Python version.
+ You are running the BornAgain scripts from the Anaconda command prompt.
+ You are running the `VSCode` editor from the `Anaconda navigator`.
+ You do not have any other Python installed on the system.

### Caveat

Anaconda is a rolling release which allows to switch between various Python versions, update/remove packages using the `conda` environment, create isolated Python 
virtual environments and so on. It is also possible to setup a Python IDE, like `PyCharm` to work together with Anaconda.
The description of the necessary configuration steps goes far beyond this tutorial and interested users are suggested to proceed with
[Anaconda documentation](https://docs.anaconda.com/anaconda/navigator/tutorials).

