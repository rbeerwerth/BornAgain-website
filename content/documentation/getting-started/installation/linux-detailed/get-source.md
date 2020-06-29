+++
title = "Get the source"
weight = 20
+++

## Get the source

#### Source tarball

Download the [BornAgain source tarball]({{< ref-tarball >}}) and unpack it:
```bash
$ cd <some_directory>
$ tar xfz BornAgain-1.17.0.tar.gz
```

#### Github

You can also get access to the source code by cloning our public Git repository:
```bash
$ cd <some_directory>
$ git clone --recurse-submodules https://github.com/scgmlz/BornAgain.git
```

#### Why Git?

Our Git repository holds two main branches called `master` and `develop`. We consider the `master` branch to be the main branch where the source code of HEAD always reflects the latest stable release. Cloning the repository gives you the source code snapshot corresponding to the latest stable release. It also automatically sets up your local master branch to track our remote master branch, so you will be able to fetch changes from the remote branch at any time using the `git pull` command. Every update in the master branch corresponds to a new release.

The second branch, the `develop` branch, is a snapshot of the current development stage. This is where any automatic nightly builds are built from. The develop branch is always expected to compile, but could still contain known bugs that have not been fixed yet. To get the most recent features one can switch the source tree to it with the following git commands:
```bash
$ cd BornAgain
$ git checkout develop
$ git pull
```

