<!--
.. title: Style
.. slug: style
.. date: 2020-09-18 08:25:57 UTC-07:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

Icepack is a community project and we gratefully accept contributions from anyone.
At the same time, we also want to keep the code as readable and maintainable as possible and that involves a bit of discipline.
The Python development team has published a very general set of guidelines for Python coding style called [PEP8](https://pep8.org/) and we try to conform to this as best we can.
There are specific considerations around coding style for scientific software that we’ll try to address too.

### Tooling

There are tools like black or YAPF for automatically formatting code.
We sometimes use these tools on individual code patches, but we don' apply them to the entire code base because they're often too rigid.

Other tools will merely point out potential problems and allow you to either ignore or fix them according to your judgment.
For example, [flake8](https://flake8.pycqa.org/en/latest/) can detect things like importing a module or a symbol but not actually using it, not putting the recommended amount of spacing around class or function definitions, and so forth.
A common feature of these tools is that they spit out loads of warnings for perfectly innocuous code, so using them effectively means figuring out how to make them less annoyingly pedantic.
The incantation we use for flake8 is:

```shell
flake8 --ignore=E741,E501,W504 ./
```

The `--ignore` flag removes a few warning types that we don't care about.
While flake8 looks mostly for stylistic problems, the tool [pylint](https://github.com/PyCQA/pylint) goes much further.
Pylint will suggest things like refactoring repeated code, splitting up long functions into smaller ones, and so forth.
The pylint invocation that we've found works best is

```shell
pylint --disable=invalid-name,non-ascii-name,attribute-defined-outside-init,invalid-unary-operand-type ./
```

This form disables several warning types that we don't consider helpful.
For example, both pylint and flake8 suggest that single-character identifier names like `i` and `j` are ambiguous.
But if you were writing code to do linear algebra, the variable names `i` and `j` match perfectly the symbols that are commonly used for the row and column of a matrix in numerical linear algebra textbooks.

### Naming

An old quote that's become folklore by now: "There are only two hard things in computer science, cache invalidation and naming things."

Throughout icepack, we employ two different guiding principles for how to name identifiers.
Some code is meant to be read by everyone – glaciologists, curious oceanographers, or us, the maintainers of the project.
For example, everyone will need to call the diagnostic and prognostic solve routines for some flow solver.
In these parts of the code base it’s critical to use English names that clearly and succinctly indicate the role of the object, like `velocity`, `thickness`, `viscosity`, `solve`, and so forth.

Other parts of the code are only meant to be read by someone who is familiar with the physics and mathematics.
**Mathematical code should look as much like the mathematics as possible.**
The internal details of what makes up the viscous part of the action functional for a particular ice flow model is a good example.
If you are reading that code, you should know that it will involve quantities like the strain rate tensor, and you should be familiar with the fact that this field is usually denoted with a Greek letter epsilon in most books on continuum mechanics.
In these parts of the code, we freely use single-character identifiers like `u` for velocity, as long as they match what appears in textbooks.
We will even sometimes use Greek letters like `ε` or `φ` where appropriate.
(Most text editors include shortcuts for inserting these symbols.
For example, in vim, you can insert a Greek letter `φ` by entering insert mode, typing `ctrl + k`, and then typing `f`.
In a Jupyter notebook, you can start typing `\phi` and then hit the tab key.)
These are never to be used in the public user interface, but they can make the code more mnemonic and familiar once you know the mathematics.
The kind of code where you would write like this will be written once, debugged twice, and read hundreds or thousands of times.
Make it look like the math we all know and love, and it’ll be that much easier to pair up with your preexisting conceptions of what that code is for.
