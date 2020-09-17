<!--
.. title: Pull requests
.. slug: pull-requests
.. date: 2020-09-17 10:31:07 UTC-07:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

This page explains how you can submit new code or documentation to icepack.
We use the version control system git for managing the icepack source code and for keeping track of our work.
If this is your first experience using git, a good resource is Aaron Meurer's [tutorial](http://www.asmeurer.com/git-workflow/).
Version control with git can be challenging at first and we've all made loads of mistakes.
Please don't hesitate to [get in touch](/contact/) via Slack if you're running into challenges and want some help.

The general workflow for submitting new code or documentation to an open source project usually works something like this:

* **[Raise an issue](/issues/)** on the repository page describing what changes you'd like to make.
Here you'll discuss the scope of those changes with the other developers.
* **Create a fork** of icepack to your own GitHub account, then **create a branch** in your fork of the icepack repository.
Give the branch a name that clearly indicates what you're trying to achieve with this new code.
* **Implement your changes** in a series of commits, each of which roughly does one small, atomic thing at a time.
Keeping changes small helps the other developers easily digest each individual unit of work to provide the best feedback possible.
Give a clear description of that change in the commit message.
* **Create a [pull request](https://github.com/icepack/icepack/pulls)** on the project page.
In the pull request description, you'll start by saying something like "Resolves issue #X."
The issue will get automatically linked to the pull request.
In the remainder of the PR description, you can summarize *how* you went about fixing that bug, implementing that feature, etc.
* The other developers of the project will **review your code**.
They might request some changes from you.
*Code review involves a lot of back-and-forth*, especially for complicated patches or features.
This is totally normal!
* Some projects might ask you to *rebase* your branch either on top of upstream changes, or to make the commit history easier to digest later.
* Finally, another developer will **merge your pull request**.
