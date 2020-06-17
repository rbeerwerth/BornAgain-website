+++
title = "Installation on Linux (short version)"
weight = 31
+++

## Installation on Linux (short version)

This page shortly explains how to build and install BornAgain from source on Linux systems.

#### Install third party software

* `Compiler with full C++-14 support (i.e. gcc>= 5.0)`
* `cmake (>= 3.14)`
* `boost library (>= 1.60)`
* `fftw3 library (>= 3.3.1)`
* `gsl (GNU scientific library, >= 1.15)`
* `libtiff library (>=4.0.2)`
* `python3, python3-devel, python3-numpy-devel, python3-matplotlib`
* `Qt5 (>=5.11)`

#### Get the source

Download the BornAgain source [tarball](http://apps.jcns.fz-juelich.de/src/BornAgain/BornAgain-{{< release-string >}}.tar.gz) or use the following git repository
  
```
$ git clone --recurse-submodules https://github.com/scgmlz/BornAgain.git
```

#### Build and install the framework

```
$ mkdir <build_dir>; cd <build_dir>;
$ cmake -DCMAKE_INSTALL_PREFIX=<install_dir> <source_dir>
$ make -j4
$ ctest -j4
$ make install 
```

#### For Python2 (not recommended)

```
$ cmake -DBORNAGAIN_USE_PYTHON3=OFF -DCMAKE_INSTALL_PREFIX=<install_dir> <source_dir>
```
