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

### Workflow

The general workflow for submitting new code or documentation to an open source project usually works something like this:

* **[Raise an issue](/issues/)** on the repository page describing what changes you'd like to make.
Here we'll discuss the scope of those changes, what it is you're looking to accomplish, and why.
* **Create a fork** of icepack to your own GitHub account if you haven't done so already.
* **Create a branch** within your fork of the icepack.
Give the branch a name that clearly indicates what you're trying to achieve with this new code.
* **Implement your changes** in a series of commits, each of which roughly does one small, atomic thing at a time.
Keeping changes small helps the other developers easily digest each individual unit of work to provide the best feedback possible.
Give a clear description of that change in the commit message.
* **Create a [pull request](https://github.com/icepack/icepack/pulls)** on the project page.
In the pull request description, you'll start by saying something like "Resolves issue #X."
The issue will get automatically linked to the pull request.
In the remainder of the PR description, you can summarize *how* you went about fixing that bug, implementing that feature, etc.
* Our **[test suite](https://app.circleci.com/pipelines/github/icepack/icepack?branch=master)** will run your code with both an old and a new release of Python to make sure that it works properly.
If a test fails, that's totally ok!
We make mistakes all the time and rely on this test suite to catch them for us.
You can always add new commits that fix any problems you find to your branch and the test suite will run again.
* The other developers of the project will **review your code**.
They might request some changes from you.
*Code review involves a lot of back-and-forth*, especially for complicated patches or features.
This is totally normal!
* Some projects might ask you to *rebase* your branch either on top of upstream changes, or to make the commit history easier to digest later.
* Finally, another developer will **merge your pull request**.

The point of all this bureaucracy is to make sure that all the code we commit to the master branch of icepack is correct and ready for others to use.
The remaining pages in the [developers](/developers/) section of the documentation explain more about practices that we've found to be helpful for delivering high-quality, useful software.

### Changing the demos

If you're modifying one of the demos or adding a new demo, we'll ask that you take some steps to make sure that only the essential content of the Jupyter notebook gets tracked in version control.
We store only the un-executed form of the notebook with no outputs or plots in the icepack git repository, with the understanding that a user can always execute the notebook in order to see the results.
To remove any outputs or plots and restore a notebook to its original state, you can use [`nbstripout`](https://github.com/kynan/nbstripout) command:

```shell
pip3 install nbstripout
nbstripout icepack/demo/<name of demo>.ipynb
```

Jupyter notebooks have lots other unnecessary metadata that this command can remove for us.

### Coding style

We don't have a rigorously enforced coding style.
Nonetheless, we do use tools like flake8 and pylint to help us be consistent and clear in things like formatting, identifier naming, and overall code structure.
If you're not already familiar with these tools, please see the [style](/style/) section for more information.
Running flake8 and pylint on your code and making the suggested changes before making a pull request will help it get reviewed faster because we mostly won't have to address coding style.
