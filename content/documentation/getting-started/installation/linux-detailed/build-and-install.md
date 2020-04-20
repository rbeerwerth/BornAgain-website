+++
title = "Build and install BornAgain"
weight = 30
+++

## Build and install BornAgain

BornAgain comes with configuration files for the cross-platform build system [CMake](https://cmake.org/). Using CMake, it takes the following commands to build and install BornAgain:
```bash
$ mkdir <build_dir>
$ cd <build_dir>
$ cmake [<options>] <source_dir>
$ make -j4
$ ctest -j4
$ sudo make install
```

These steps shall now be explained in more detail.

#### Dedicated build directory

```bash
$ mkdir <build_dir>
$ cd <build_dir>
```

The build process must take place in a dedicated directory <build_dir>. After the installation is complete, <build_dir> can be safely removed.

#### CMake command for the build configuration

```bash
$ cmake -DCMAKE_INSTALL_PREFIX=<install_dir> <source_dir>
```

This command checks your system for the presence of the third party libraries necessary for compilation. In the case of a complex system setup, with libraries of different versions scattered across multiple places (/opt/local, /usr/local etc), you may want to help CMake in finding the correct library paths by running it with additional parameters:

```bash
$ cmake -DCMAKE_PREFIX_PATH=/opt/local -DCMAKE_INSTALL_PREFIX=<install_dir> <source_dir>
```

{{< alert theme="info" >}}
**Note for MacOS users**

MacOS users who have installed third party libraries using the MacPorts package manager have to use an additional key during the CMake configuration to specify the location of MacPort's libraries (e.g. `/opt/local`):
```
cmake -DCMAKE_PREFIX_PATH=/opt/local -DCMAKE_INSTALL_PREFIX=<install_dir> <source_dir>
```


**For Homebrew users**
```
cmake -DCMAKE_PREFIX_PATH=/usr/local -DCMAKE_INSTALL_PREFIX=<install_dir> <source_dir>
```
{{< /alert >}}

{{< alert theme="info" >}}
**Note for Python2 users**

Use additional CMake key during configuration
```
cmake -DBORNAGAIN_USE_PYTHON3=OFF -DCMAKE_INSTALL_PREFIX=<install_dir> <source_dir>
```
{{< /alert >}}

#### The compilation

```bash
$ make -j4
```

This command starts the compilation process with a maximum of 4 parallel threads. Depending on your CPU, you can increase this parameter (`-j[N]`) to decrease the compilation time.

#### Testing the build

```bash
$ ctest -j4
...
100% tests passed, 0 tests failed out of 61
Total Test time (real) = 31.14 sec
[100%] Build target check
```

Running the functional tests is an optional but recommended step. The command `ctest` will compile several additional tests and run them one by one. The option `-j[N]` uses up to `N` threads to run these tests in parallel. Every test contains the simulation of a typical sample and compares the result with a reference file. Having `100% tests passed` ensures that your local installation is correct.

#### Installing the framework
```bash
$ sudo make install
```

The last command copies the compiled libraries and usage examples into the installation directory `<install_dir>`, which has been specified earlier on during the CMake configuration.
