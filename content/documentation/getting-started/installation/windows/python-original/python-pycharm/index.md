+++
title = "PyCharm IDE"
weight = 20
+++

## Using the PyCharm IDE

In this tutorial we explain how to run BornAgain Python examples using `PyCharm` - a free and multi-platform Python integrated development environment, which enables one to work with Python code in a convenient manner.

At this point we assume that the user has already installed BornAgain and a Python distribution as explained in
[Python installation section]({{% relref "documentation/getting-started/installation/windows/python-original" %}}).

### Download and install PyCharm

Download the PyCharm installer from [here](https://www.jetbrains.com/pycharm/download/#section=windows).
Make sure you are installing the community edition, which is free.

{{< figscg src="python-pycharm-step2.PNG" class="center" width="450px">}}

Run the installer.

{{< figscg src="python-pycharm-step4.PNG" class="center" width="450px">}}

### Start PyCharm and create new project

Open `PyCharm` and select `Create New Project`:

{{< figscg src="python-pycharm-project1.PNG" class="center" width="450px">}}

The project `Untitled` will be created in the default projects directory. Click on `Project interpreter` to start configuring the Python interpreter.

{{< figscg src="python-pycharm-project2.PNG" class="center" width="450px">}}

Click on `Existing interpreter` and proceed with the interpreter selection.

{{< figscg src="python-pycharm-project3.PNG" class="center" width="450px">}}

In the new window, select `System interpreter`. This will let you select the system interpreter you have installed already
during the [Python installation]({{% relref "documentation/getting-started/installation/windows/python-original" %}}) phase.

{{< figscg src="python-pycharm-project5.PNG" class="center" width="450px">}}

The final window for project creation should look like the screenshot below.

{{< figscg src="python-pycharm-project6.PNG" class="center" width="450px">}}

Push `create project` button.

{{< alert theme="info" >}}
Up to now, we have configured `PyCharm` to work with the system interpreter directly. Please note that `PyCharm` has the possibility to run code in a so-called `virtual environment`. The detailed description of the configuration process can be found on the
[official web site](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html).
{{< /alert >}}


### Configure the project you've just created.

As soon as you push the `Create` button, you will be presented with the initial project view. The tree view on the left shows that your project consists of two parts: the `Untitled` directory for your python scripts (which is empty for the moment) and the `External Libraries ` directory (which is not relevant for us at this point).

{{< figscg src="python-pycharm-project7.PNG" class="center" width="450px">}}

Please also note, that `PyCharm` will automatically start with `indexing` (see the label and the progress bar at the bottom of the screen). This is a one-time procedure in which `PyCharm` familiarizes itself with the project interpreter and its environment. This phase can last from several minutes up to half an hour, depending on the speed of your computer. During this phase you will not be able to run any of the Python scripts.

Now, let's add the BornAgain examples to the project directory to be able to run and modify any of them at any time. Go to the `File/Settings` menu:

{{< figscg src="python-pycharm-project8.PNG" class="center" width="450px">}}

On the left, select `Project -> Project Structure` and then push the button `+ Add Content Root` on the right:

{{< figscg src="python-pycharm-project10.PNG" class="center" width="450px">}}

A new window will appear and now select the directory with the BornAgain Python examples and push the `OK` button.

{{< figscg src="python-pycharm-project11.PNG" class="center" width="450px">}}

Close the settings window. The final project should like shown below. 

{{< figscg src="python-pycharm-project13.PNG" class="center" width="450px">}}

Try to run any of the examples using the right mouse button.

{{< figscg src="python-pycharm-project14.PNG" class="center" width="450px">}}

You should see a scattering image appearing on the screen.

{{< figscg src="python-pycharm-project15.PNG" class="center" width="450px">}}

Congratulations, you successfully configured PyCharm to work with BornAgain!
