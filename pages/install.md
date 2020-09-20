<!--
.. title: Install
.. slug: install
.. date: 2020-09-14 13:40:48 UTC-07:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

This page will tell you how to install icepack and its main dependency, the [Firedrake](https://firedrakeproject.org) package.
The installation procedure for Firedrake is a little unusual compared to a typical Python package.
If you run into difficulties installing Firedrake, please consult their [website](https://firedrakeproject.org/download.html#system-requirements), which includes a debugging guide and other information on system requirements.
For other problems, you can always [get in touch](/contact/) for more assistance.
For more explanation, see below.

### Quick start

Install Firedrake, building PETSc along the way:

```shell
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-install
python3 firedrake-install --install icepack
```

Activate the Firedrake virtual environment:

```shell
source <path/to/firedrake>/bin/activate
```

Run one of the icepack unit tests to make sure it works:

```shell
cd $VIRTUAL_ENV/src/icepack
pytest -s test/ice_shelf_test.py
```

Your icepack installation lives in the directory `$VIRTUAL_ENV/src/icepack`.

### Run the demos

Install the mesh generator [gmsh](http://gmsh.info/).
Binaries are available on their website, or you can use your system package manager.
On MacOS,

```shell
brew install gmsh
```

On Debian, Mint, or Ubuntu:

```shell
sudo apt-get install gmsh
```

Now make a Jupyter kernel for firedrake:

```shell
pip3 install ipykernel
python3 -m ipykernel install --user --name=firedrake
```

Run the demo notebooks:

```shell
cd $VIRTUAL_ENV/src/icepack/demo
```

### Comments

Most python projects use the simple `python setup.py install` formula to build and install everything.
Firedrake is appreciably more complex -- it consists of several dependent sub-packages along with a complete PETSc installation -- and thus has its own custom build process.
Rather than install the project in your system python package directory, Firedrake's install script builds it inside an isolated [*virtual environment*](https://docs.python.org/3/tutorial/venv.html).
Python virtual environments were created to solve problems of conflicting package versions possibly breaking installed libraries.
Rather than install every Python package globally, you can create an isolated virtual environment for one particular package.
This environment includes a Python executable and all of the package's dependencies.
Virtual environments can be activated and deactivated for a particular shell session.
The added layer of isolation keeps one package from breaking other packages on the system or doing anything that's both undesirable and hard to roll back.

However, it does introduce an annoying layer of bureaucracy -- you have to manually activate the virtual environment every time you want to use it by invoking:

```shell
source <path/to/virtual/environment>/bin/activate
```

Again, activating a virtual environment affects only the current shell session and doesn't do anything permanent.

You can save yourself the trouble of remembering where the activate script lives by adding a function like this to your `.bashrc` or `.bash_profile`:

```shell
firedrake-env() {
    source </absolute/path/to/virtual/environment>/bin/activate
}
```

When you type `firedrake-env` at the terminal, the firedrake virtual environment will be activated.
If you find yourself using lots of different virtual environments, you might also like [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

Firedrake uses the library [PETSc](https://www.mcs.anl.gov/petsc/) for many of its internal data structures (meshes, vectors, matrices).
PETSc has loads of optional features, chiefly interfaces to other computational libraries.
Some of these features are mandatory for firedrake.
The Firedrake install script will build its own PETSc installation with the right configuration, but this could create problems if you already do have PETSc installed on your system.
In that case, you will need to unset `$PETSC_DIR` and `$PETSC_ARCH` while installing Firedrake and every time you activate the virtual environment.
You can add an extra line to the `firedrake-env` command above to unset these variables if you want to keep a pre-existing PETSc installation.
While installing Firedrake will fail with an error if you have a pre-existing PETSc installation, trying to run a script that uses Firedrake will instead crash with a segmentation fault if you have not first unset the PETSc environment variables.

To run all of the demos, you'll need to have the mesh generator gmsh.
Gmsh will take a description of the outline of some domain in 2D and calculate a triangulation of the interior.
Since the shape of most real glaciers is very irregular and thus can't easily be represented by a rectilinear grid, a tool like gmsh is indispensible.
Gmsh is available through the package managers of most operating systems or as a binary executable from the project website.
