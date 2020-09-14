.. title: Tutorials
.. slug: tutorials
.. date: 2020-09-09 20:58:16 UTC-08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. hidetitle: True

.. sidebar:: Tutorials
{}

This page is for you if you're just starting out with icepack and you want to learn how to use it.
These tutorials demonstate all of the functionality of the library that you will need to set up simulations of glacier flow.
These pages are rendered from Jupyter notebooks that come with the icepack source distribution under the ``demo/`` directory.
You can and should run all of this code yourself.

At this point, you should have a working installation of Firedrake and icepack, a Jupyter kernel for Firedrake, and you should be able to run the tutorial notebooks.
See the `install </install/>`_ page for instructions.

To understanding what's in these tutorials, you'll need to know a bit about glacier physics.
We'll expect that you're familiar with:

* mass, momentum, and heat transport
* the Stokes equations and simplified models
* Glen's flow law

Additionally, you should know going in that **all quantities are reported in units of megapascals - meters - years**.
We borrowed this slightly unconventional unit system from the package `Elmer/Ice <http://elmerice.elmerfem.org/>`_.
In this unit system, most of the physical constants and quantities that we care about live in a reasonable numerical range.
For example, the ice fluidity factor `A` in Glen's flow law is usually between 1 and 50.

The goal of the tutorials is to get you off the ground.
If you already have a good grasp of what icepack does and you want to use it to solve new and interesting problems, you can look at our collection of how-to guides.
Those pages will show you the ingredients for more realistic simulations that you might use in original research for publication in peer-reviewed journal articles.
