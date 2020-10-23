<!--
.. title: Maintenance
.. slug: maintenance
.. date: 2020-09-18 09:58:03 UTC-07:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

This page is to help you set up and maintain a development environment when hacking on a Python project like icepack.
Working collaboratively on software presents new challenges, like how to keep up to date with a rapidly evolving code base while also working on features that you're adding.

### Installation

The [installation instructions](/install/) are written for prospective users in order to help them get set up as quickly as possible.
If you're developing new code, you're going to have different needs.
For example, you might be working on more than one feature at the same time, or you might be testing icepack against different installations of Firedrake that have been configured differently.

The first thing you'll want to do is clone icepack into a separate directory and add your fork as a remote.

```shell
git clone git@github.com:icepack/icepack.git
cd icepack
git remote add \
    <your name> \
    git@github.com:<your GitHub username>/icepack.git
```

Next, you'll want to activate the virtual environment and install both icepack and the dependencies for building the documentation in editable mode:

```shell
source </path/to/firedrake>/bin/activate
pip3 install --editable </path/to/icepack>"[doc]"
```

The `--editable` flag guarantees that changes you make to the source code get seen automatically whenever you import icepack.
Without this flag, you'd have to reinstall again every time you made changes.
The flag `"[doc]"` at the end tells pip to also install the dependencies you'll need to build the icepack documentation.
This is part of a [general mechanism](https://setuptools.readthedocs.io/en/latest/references/keywords.html) of Python's setuptools for specifying optional dependencies.

In the unfortunate event that your Firedrake installation becomes unusable, for example because your operating system decided to upgrade Python out from under you, you can delete the entire Firedrake virtual environment and reinstall a fresh one without losing any changes you made to your branch of icepack.

### Editors and IDEs

Nearly every editor nowadays offers syntax highlighting for Python.
We recommend using an editor or IDE that has built-in support for autocompletion and linting.
For example, some of us use the [Spyder](https://www.spyder-ide.org/) IDE.
Sometimes you might need to do something special to make your editor understand that some code lives in a virtual environment, which is especially necessary for autocompletion.
Using Spyder again as an example, you can activate the virtual environment and install Spyder inside it achieve this effect.
If you're using emacs and the [jedi](https://jedi.readthedocs.io/en/latest/) plugin, you can customize the [arguments](http://tkf.github.io/emacs-jedi/latest/#jedi:server-args) to the jedi server in order to make it see your virtual environment.

### Rebasing

Icepack is actively developed by several people committing new code at the same time.
If you're working on a new feature, you might find that the master branch has been updated.
Sometimes the changes to the master branch might even include bug fixes that are useful or relevant to the feature you're working on.
In order to pull the latest changes into your branch, you can run the following commands:

```shell
git fetch origin master
git rebase origin/master
```

The git `rebase` command is a really powerful tool which you should read more about.
What it does is effectively rewrite the commit history to put the changes in your branch on top of any changes from the master branch.
The nice part about `rebase` as opposed to `merge` is that it won't create an unnecessary merge commit, unless there are conflicts to deal with.

The other important use of the rebase command is to clean up or otherwise alter the commit history of a branch you're working on.
This is best done through an *interactive* rebase:

```shell
git rebase --interactive HEAD~<number of commits>
```

Git will then fire up the text editor of your choice and present you with a list of the number of commits you selected.
You can then choose to `pick` those commits, `edit` the changes in that commit, `squash` two commits into each other, or change the order in which those commits were applied.
A typical use case might be to take a feature branch and squash any intermediate bug fixes onto the original commits that introduced that code in the first place.
Minor mistakes like these aren't relevant for the overall history, and it's easiest to review the patch with these changes squashed into the original commit.

Rather than describe all the things you can do with an interactive rebase, we'll instead refer you to a really well-written [guide](https://git-rebase.io/) on the subject.
If you do want to rebase some code and you're having trouble, please get in touch over [Slack](/contact/) and we can walk you through it.

The environment variable `$VISUAL` determines what editor gets opened whenever a command like `git rebase` needs one.
You can set this environment variable in your shell profile to select vim, emacs, Sublime Text, or whatever you prefer.
