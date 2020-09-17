<!--
.. title: Issues
.. slug: issues
.. date: 2020-09-17 10:30:54 UTC-07:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

This page will explain our process for soliciting feedback on what changes to make to icepack.
**You can file bug reports and feature requests by [raising an issue](https://github.com/icepack/icepack/issues/) on the project repository.**
When you think that something about icepack needs changing, please don't hesitate to bring this to our attention.

If you do file an issue, we're happy to make the proposed changes, provided that they're within the scope of the library and we have the expertise to do it.
If you want to implement this change yourself, we gladly accept code contributions -- please see the page on [submitting pull requests](/pull-requests/) for more information.
If you want to add a new feature or fix a bug yourself but don't know how, please [get in touch](/contact/) over Slack or email.
In the long run, **it is a more worthwhile use of our time to teach you how you can write this code yourself than it is for us to write it ourselves**, even if we could have written faster.
People are a more valuable asset than code.

### Bug reports

We subject icepack to a battery of tests whenever changes are made in the hopes of making sure that all of the code works as it's supposed to.
Nonetheless, we do make mistakes.
If you think you've found a bug, please [file an issue](https://github.com/icepack/icepack/issues/) on the project page with a clear and concise description of the problem you're encountering.

The most helpful thing for us in quickly identifying and fixing bugs is to have access to the code that triggered the problem.
That way, we can test it on our own machines without a bunch of asynchronous back-and-forth.
If you want to make our lives even easier you can try to construct a *minimal failing example* (MFE).
This means taking the buggy script and cutting out as much code as possible while still triggering the problem.

It's very common that numerical solvers seem fine when tested on synthetic problems, only to fail spectacularly on real data.
If you do encounter a bug when solving problems with real data, we can only reproduce your test case with access to that data.
This is easiest when you use publicly available datasets, for example from [NSIDC](https://www.nsidc.org).

### Feature requests

We add new features to icepack regularly and we try to prioritize whatever we think will make the greatest difference to the glaciological community at large.
You can give us feedback on what new features are important to you by [raising an issue](https://github.com/icepack/icepack/issues/) on the project page with a description of what you'd like to see added.
For example, this might include:

* new physics solvers, like firn densification or fabric development
* new data analysis capability or quality-of-life features, like automatically generating a mesh from the Randolph Glacier Inventory
* new demonstrations, for example of how to model a particular type of physical system that isn't already included in the tutorials or how-to guides, or how to do common tasks in the analysis of simulation data

To help us understand the feature you'd like to see added, please include links to any relevant papers or to other packages that do implement this feature.

We welcome requests for new features as these help us gauge what's most important to the community.
If you see that someone has already made a feature request for something that you need as well, you can give a "thumbs up" to it on GitHub.
This might seem like just a silly and gratuitous use of emojis, but it's very helpful to us -- now we know that two people need the same thing!
At the same time, we have only a finite amount of time and energy.
We decide what to add next based on what we think will make the most difference to users and on how difficult or time-consuming we expect implementing that feature will be.
