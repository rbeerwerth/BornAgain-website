+++
title = "Minimizer settings"
weight = 40
+++

## Minimizer settings

The BornAgain minimizer interface was developed with the following ideas in mind:

+ Provide an interface which looks more or less familiar for users of other Python minimization packages.
+ Enable the use of our minimizer for optimization problems outside the BornAgain context.
+ Allow the usage of other, possibly more advanced minimization libraries, for BornAgain fits.

Particularly, we have been inspired by the [lmfit Python package](https://lmfit.github.io/lmfit-py/),
so the BornAgain setup looks very similar.
In the code snippet below we give an example of finding the minimum of the [Rosenbrock function](https://en.wikipedia.org/wiki/Rosenbrock_function)
using the BornAgain minimizer with default settings.

{{< highlight python >}}
def rosenbrock(params):
    x = params["x"].value
    y = params["y"].value
    tmp1 = y - x * x
    tmp2 = 1 - x
    return 100 * tmp1 * tmp1 + tmp2 * tmp2

params = ba.Parameters()
params.add("x", value=-1.2, min=-5.0, max=5.0, step=0.01)
params.add("y", value=1.0, min=-5.0, max=5.0, step=0.01)

minimizer = ba.Minimizer()
result = minimizer.minimize(rosenbrock, params)
print(result.toString())

{{< /highlight >}}

The rest of the page gives additional details on

+ [Fit parameter setup](#fit-parameters-setup)
+ [List of available minimization algorithms](#list-of-available-minimization-algorithms)
+ [Additional minimizer settings](#additional-minimizer-settings)
+ [Third party minimizers](#third-party-minimizers)

### Fit parameter setup

The BornAgain `Parameters` class allows to define a collection of fit parameters which will be varied during the fit.
Each fit parameter should have a unique name, starting value and possible bounds on its value.

{{< highlight python >}}
params = ba.Parameters()
params.add("a", value=-1.2)
params.add("b", value=-1.2, min=0.0)
params.add("c", value=-1.2, min=-5.0, max=5.0, step=0.01)
params.add("d", value=1.0, vary=False)
{{< /highlight >}}

It is not possible to use mathematical expressions to constrain these value, as it is done
in the more advanced
[parameter machinery](https://lmfit.github.io/lmfit-py/parameters.html)
of `lmfit` package.

### List of available minimization algorithms

The BornAgain minimizer is a wrapper around a variety of minimization engines
from [ROOT](https://root.cern.ch) and [GSL](https://www.gnu.org/software/gsl/doc/html/index.html) libraries.
They are listed in the table below. By default, `Minuit2/Migrad` will be used and no additional configuration needs to be done.

| Minimizer name| Algorithm | Description |
|:--|:--|:--|
| [Minuit2](http://seal.web.cern.ch/seal/documents/minuit/mnusersguide.pdf)                                                     | Migrad          | Variable-metric method with inexact line search, a stable metric updating scheme, and checks for positive-definiteness. According to the [Minuit users guide](http://seal.web.cern.ch/seal/documents/minuit/mnusersguide.pdf) [ch. 5.1.1], this is the best minimizer for nearly all functions|
|                                                                                                                               | Simplex         | Simplex method of Nelder and Mead usually, slower than `Migrad`, rather robust with respect to gross fluctuations in the function value, gives no reliable information about parameter errors. |
|                                                                                                                               | Combined        | Minimizes with `Migrad`, but switches to `Simplex` if `Migrad` fails to converge. |
|                                                                                                                               | Scan            | Not intended to minimize, just scans the function, one parameter at a time, retains the best value after each scan. |
|                                                                                                                               | Fumili          | Optimized method for least square and log likelihood minimizations. |
| [GSLMultiMin](https://www.gnu.org/software/gsl/doc/html/multimin.html)                                                        | ConjugateFR     | Fletcher-Reeves conjugate gradient algorithm. |
|                                                                                                                               | ConjugatePR     | Polak-Ribiere conjugate gradient algorithm. |
|                                                                                                                               | BFGS            | Broyden-Fletcher-Goldfarb-Shanno algorithm |
|                                                                                                                               | BFGS2           | Improved version of `BFGS`. |
|                                                                                                                               | SteepestDescent | Follows the downhill gradient of the function at each step. |
| [GSLLMA](https://www.gnu.org/software/gsl/doc/html/nls.html?highlight=levenberg%20marquardt%20algorithm#levenberg-marquardt)  |                 | Levenberg-Marquardt Algorithm |
| [GSLSimAn](https://www.gnu.org/software/gsl/doc/html/siman.html?highlight=simulated%20annealing%20algorithm)                  |                 | Simulated Annealing Algorithm |
| [Genetic](https://root.cern.ch/download/doc/tmva/TMVAUsersGuide.pdf)                                                        |                 | Genetic Algorithm |
| Test                                                        |                 | Single-shot minimizer |

To change the minimize engine and its algorithm one has to use

{{< highlight python >}}
minimizer = ba.Minimizer()
minimizer.setMinimizer("GSLMultiMin", "BFGS2")
{{< /highlight >}}

### Additional minimizer settings

There are a number of minimizer options that can be changed.
The commands below print the detailed info about the available minimizers, their options and the default option values.

{{< highlight python >}}
# prints info about available minimizers
print(ba.MinimizerFactory().catalogueToString())

# prints detailed info about available minimizers and their options
print(ba.MinimizerFactory().catalogueDetailsToString())
{{< /highlight >}}


<p>
  <a class="btn btn-secondary" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    Click to expand command output
  </a>
</p>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
  ```
--------------------------------------------------------------------------------
Minuit2             | Minuit2 minimizer from ROOT library
--------------------------------------------------------------------------------
Algorithm names
Migrad              | Variable-metric method with inexact line search, best minimizer according to ROOT.
Simplex             | Simplex method of Nelder and Meadh, robust against big fluctuations in objective function.
Combined            | Combination of Migrad and Simplex (if Migrad fails).
Scan                | Simple objective function scan, one parameter at a time.
Fumili              | Gradient descent minimizer similar to Levenberg-Margquardt, sometimes can be better than all others.
Default algorithm   | Migrad

Options
Strategy            | 1    Minimization strategy (0-low, 1-medium, 2-high quality)
ErrorDef            | 1    Error definition factor for parameter error calculation
Tolerance           | 0.01 Tolerance on the function value at the minimum
Precision           | -1   Relative floating point arithmetic precision
PrintLevel          | 0    Minimizer internal print level
MaxFunctionCalls    | 0    Maximum number of function calls

--------------------------------------------------------------------------------
GSLMultiMin         | MultiMin minimizer from GSL library
--------------------------------------------------------------------------------
Algorithm names
SteepestDescent     | Steepest descent
ConjugateFR         | Fletcher-Reeves conjugate gradient
ConjugatePR         | Polak-Ribiere conjugate gradient
BFGS                | BFGS conjugate gradient
BFGS2               | BFGS conjugate gradient (Version 2)
Default algorithm   | ConjugateFR

Options
PrintLevel          | 0    Minimizer internal print level
MaxIterations       | 0    Maximum number of iterations

--------------------------------------------------------------------------------
GSLLMA              | Levenberg-Marquardt from GSL library
--------------------------------------------------------------------------------
Algorithm names
Default             | Default algorithm

Options
Tolerance           | 0.01 Tolerance on the function value at the minimum
PrintLevel          | 0    Minimizer internal print level
MaxIterations       | 0    Maximum number of iterations

--------------------------------------------------------------------------------
GSLSimAn            | Simmulated annealing minimizer from GSL library
--------------------------------------------------------------------------------
Algorithm names
Default             | Default algorithm

Options
PrintLevel          | 0    Minimizer internal print level
MaxIterations       | 100  Number of points to try for each step
IterationsAtTemp    | 10   Number of iterations at each temperature
StepSize            | 1    Max step size used in random walk
k                   | 1    Boltzmann k
t_init              | 50   Boltzmann initial temperature
mu                  | 1.05 Boltzmann mu
t_min               | 0.1  Boltzmann minimal temperature

--------------------------------------------------------------------------------
Genetic             | Genetic minimizer from TMVA library
--------------------------------------------------------------------------------
Algorithm names
Default             | Default algorithm

Options
Tolerance           | 0.01 Tolerance on the function value at the minimum
PrintLevel          | 0    Minimizer internal print level
MaxIterations       | 3    Maximum number of iterations
PopSize             | 300  Population size
RandomSeed          | 0    Random seed

--------------------------------------------------------------------------------
Test                | One-shot minimizer to test whole chain
--------------------------------------------------------------------------------
Algorithm names
Default             | Default algorithm
```
  </div>
</div>

For example, to run the `Minuit` minimizer with the `Migrad` algorithm, limit the maximum number of objective function calls and set the minimizer strategy parameter to a certain value
one can use

{{< highlight python >}}
minimizer.setMinimizer("Minuit2", "Migrad", "MaxFunctionCalls=50;Strategy=2")
{{< /highlight >}}

### Third party minimizers

BornAgain fitting can also be done using other minimization packages. A short list of some of them is given below:

+ [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
+ [lmfit](https://lmfit.github.io/lmfit-py/)
+ [bumps](https://bumps.readthedocs.io/en/latest/)

In [this example]({{% ref-example "fitting/extended/external-minimizer" %}}) we demonstrate how to use the `lmfit` minimizer for a typical fit of GISAS data.
