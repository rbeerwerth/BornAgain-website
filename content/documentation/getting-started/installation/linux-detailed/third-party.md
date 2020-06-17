+++
title = "Install third-party software"
weight = 10
+++

## Install third-party software

Required software:

* `Compiler with full C++-14 support (e.g. gcc>= 5.0 or clang>=3.4)`
* `cmake (>= 3.14)`
* `boost library (>= 1.60)`
* `fftw3 library (>= 3.3.1)`
* `gsl (GNU scientific library, >= 1.15)`
* `libtiff library (>=4.0.2)`
* `python3, python3-devel, python3-numpy, python3-matplotlib`
* `Qt5 (>=5.4; required modules are listed below)`

All required packages can be easily installed on most Linux distributions using the system's package manager. Below are a few examples for several selected operating systems. Please note, that other distributions (Fedora, Mint, etc) may have different commands for invoking the package manager and slightly different names of packages (like `boost` instead of `libboost` etc). Besides that, the installation should be very similar.

<!-- Nav tabs -->
<ul class="nav nav-tabs" id="OperationSystemTab" role="tablist">
  <li class="nav-item">
    <a class="nav-link active" id="home-tab" data-toggle="tab" href="#Ubuntu" role="tab" aria-controls="ubuntu" aria-selected="true">Ubuntu (Focal)</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="profile-tab" data-toggle="tab" href="#OpenSuse" role="tab" aria-controls="opensuse" aria-selected="false">OpenSuse</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="messages-tab" data-toggle="tab" href="#CentOS" role="tab" aria-controls="centos" aria-selected="false">CentOS/Redhat</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="messages-tab" data-toggle="tab" href="#MacOS" role="tab" aria-controls="macos" aria-selected="false">MacOS</a>
  </li>
</ul>

<!-- Tab panes -->
<div class="tab-content id="OperationSystemTabContent">
  <div class="tab-pane active" id="Ubuntu" role="tabpanel" aria-labelledby="ubuntu-tab">
    <p><ul><li>Install required packages:
<pre><code>$ sudo apt-get install build-essential git cmake libgsl-dev libfftw3-dev python3 python3-dev python3-numpy python3-matplotlib libtiff5-dev libboost-dev libboost-filesystem-dev libboost-program-options-dev libboost-regex-dev libboost-iostreams-dev qt5-default libqt5designercomponents5 qttools5-dev libqt5svg5-dev libqt5opengl5-dev</code></pre></li>
</ul></p>
  </div>
  <div class="tab-pane" id="OpenSuse" role="tabpanel" aria-labelledby="opensuse-tab">
    <p><ul><li>Install required packages:
<pre><code>$ sudo zypper install gcc-c++ git-core cmake gsl-devel libboost_*-devel fftw3-devel \
  python3-devel python3-numpy-devel python3-matplotlib libtiff-devel</code></pre></li>
    <li>Install Qt5
<pre><code>$ sudo zypper install libqt5-qtbase-devel libqt5-qttools-devel libqt5-qtsvg-devel</code></pre></li></ul></p>
  </div>
  <div class="tab-pane" id="CentOS" role="tabpanel" aria-labelledby="centos-tab">
    <p/>
    <p>CentOS 7 and Redhat 7 ship with gcc-4.8.5, which does not fully support C++ 14. This instruction thus also explains how to get a newer compiler on your system.</p>
    <p><ul><li>Install extra packages:
    <pre><code>$ sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm</code></pre></li>
    <li>Install BornAgain dependencies:
    <pre><code>$ sudo yum -y install make cmake3 gcc-c++
$ sudo yum -y install fftw-devel boost-devel gsl-devel libtiff-devel
$ sudo yum -y install python3-devel numpy
$ sudo yum -y install qt5-qtbase-devel qt5-qttools-devel qt5-qtsvg-devel</code></pre></li>
    <li>Install 'devtoolset' with additional development tools.<br/>
    See
<a href="https://www.softwarecollections.org/en/scls/rhscl/devtoolset-4">Devtoolset-4</a>
 for more details.
    <pre><code>$ sudo yum install centos-release-scl  # if you are on CentOS</code></pre>or
    <pre><code>$ sudo yum-config-manager --enable rhel-server-rhscl-7-rpms # if you are on RHEL</code></pre></li>
    <li>Install newer compiler:
    <pre><code>$ sudo yum install devtoolset-4-gcc-c++</code></pre></li>
    <li>Enable the new compiler (you will have to run this command for every new terminal):
    <pre><code>$ scl enable devtoolset-4 bash</code></pre></li>
    <li>Make sure, that gcc gives you version 5.0 or higher:
    <pre><code>$ g++ --version</code></pre></li>
    </ul></p>
  </div>
  <div class="tab-pane" id="MacOS" role="tabpanel" aria-labelledby="macos-tab">
    <p/>
    <p>MacOS comes with no package manager, but fortunately there are several free and well maintained package managers that significantly simplify the installation of third-party open-source software. Here, we provide recepies for <a href=https://brew.sh/>Homebrew</a> and <a href=https://www.macports.org/>MacPorts</a>.</p>
    <h4>Important note</h4>
    <p>Homebrew installs all packages in <pre>/usr/local</pre>, while MacPorts prefers the <pre>/opt/local</pre> folder. Depending on your package manager selection, the corresponding path has to be specified explicitly during the BornAgain CMake configuration as explained in <a href=../build-and-install>Build and install BornAgain<a>.</p>
    <h4>Homebrew</h4>
    <p>Install Homebrew as explained <a href=https://brew.sh/>here</a> and then install all BornAgain dependencies by running the following command:
    <pre><code>brew install git cmake fftw gsl python boost libtiff eigen qt5 &&
pip3 install matplotlib numpy
</code></pre>
    </p>
    <p>Finally, add Qt to your path environment variable:
    <pre><code>$ export PATH=/usr/local/opt/qt5/bin/:$PATH</code></pre></p>
    <h4>Macports</h4>
    <p>Install Macports by downloading and running the installer from <a href=https://www.macports.org/install.php>here</a>. Then install all BornAgain dependencies by running the following command:
    <pre><code>$ sudo port install git cmake fftw-3 gsl py3-matplotlib py3-numpy \
  tiff boost qt5-mac</code></pre>
    </p>
  </div>
</div>
