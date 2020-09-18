<!--
.. title: Testing
.. slug: testing
.. date: 2020-09-17 16:48:40 UTC-07:00
.. tags: mathjax
.. category: 
.. link: 
.. description: 
.. type: text
-->

All of the physics solvers in icepack are subject to a battery of tests.
When you submit new code to icepack, either to add a new feature or to fix a bug, we'll ask you to write tests for that code as well.
If you're fixing a bug, clearly our existing test suite didn't catch it.
A good test for a bug fix is something that fails on the old broken code but succeeds on the new fixed code.
Writing tests for completely new code is harder and this page aims to offer some guidance.

The goal of a test suite is to check the correctness of the algorithms on simplified problems in the hopes of detecting errors in the implementation.
For example, for a floating ice shelf where the fluidity is constant and the ice thickness decreases linearly towards the ice front, the shallow shelf equations can be solved analytically.
To check that the diagnostic solver is working correctly, the numerically computed solution is compared against the exact solution, and a significant departure indicates a mistake.

**Designing effective tests for scientific software is difficult because the answers we get are only approximations.**
Our results never match analytical solutions perfectly, so at what point should a given mismatch be considered a failure?
This breakdown point can be calculated only for the simplest PDEs and spatial domains.

Instead, we know from finite element theory that the solutions should converge as $\mathcal{O}(\delta x^p)$ where $\delta x$ is the mesh spacing and $p$ is some exponent depending on the problem and discretization.
We can then take a sequence of meshes and do a log-log fit of the errors against $\delta x$ to check that this asymptotic behavior is indeed achieved.
But the asymptotic estimates never quite hold exactly.
For example, using piecewise linear finite elements and the backward Euler scheme to solve the mass transport equation should give errors that decrease as $\mathcal{O}(\delta x)$.
What if, instead, you find that the errors decay like $\delta x^{0.95}$?
Should that indicate failure, even if it suggests that the numerical solutions do get more accurate?
There isn't really a good answer for this – we just have to do our best and be as critical as we can.

Another difficult issue is *generalizability*.
Does the convergence of a solver on simplified problems imply that it will also perform well on harder problems?
When no analytical solution is available at all, how should one design a useful test?
The best we can hope for in this situation is to rely on mathematical properties of the solution, such as conservation laws or variational principles.
Rather than check against an analytical solution, these properties serve as sanity checks.
For example, given an approximate solution to the shallow shelf equations, one can take a random perturbation to it and check that this perturbation has a higher value of the action functional due to the minimization property.
