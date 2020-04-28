+++
title = "Python API"
weight = 90
+++

## Python API


Simulation scripts interact with the BornAgain core library through an Application Programmer Interface (API). 
This API consists of numerous classes and their member functions. The primary API is written in the programming language C++. 
All important classes and their member functions are also available through a Python API. 

The [BornAgain C++ User API Reference](http://apps.jcns.fz-juelich.de/doxy/BornAgain/userapi.html), 
and the [Comprehensive BornAgain C++ API Reference](http://apps.jcns.fz-juelich.de/doxy/BornAgain/classes.html) 
are always up to date, since they are automatically extracted from the source code (which contains comment lines 
in the special `Doxygen` format in order to enable this self documentation). 

For the moment, we do not dispose of a similarly efficient documentation generator for Python. 
Therefore, Python users need to refer to the C++ API. 
Even though Python and C++ have different syntax, it is usually straightforward 
to infer from the C++ API how the corresponding Python method call will look like.
