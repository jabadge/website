<!--
.. title: Physics
.. slug: physics
.. date: 2020-10-27 12:09:55 UTC-07:00
.. tags: mathjax
.. category:
.. link:
.. description:
.. type: text
.. hidetitle: True
-->

Here we'll give a brief overview of ice physics.
This won't be a substitute for reading a book or taking a class on the subject, but it should help explain some of the notation and variable names that you'll see in the demos and documentation.
I'll assume you're familiar with continuum mechanics and vector calculus.
In particular, we'll appeal to the idea of [control volumes](https://en.wikipedia.org/wiki/Control_volume) and conservation laws.
To get all the notation out of the way, here's a table of all the symbols that we'll use:

| Name                   | Symbol
| :----                  | ----:
| velocity               | $u$
| thickness              | $h$
| surface elevation      | $s$
| bed elevation          | $b$
| accumulation rate      | $\dot a$
| melt rate              | $\dot m$
| pressure               | $p$
| strain rate tensor     | $\dot\varepsilon$
| deviatoric stress      | $\tau$
| Glen flow law rate     | $A$
| Glen flow law exponent | $n$
| friction coefficient   | $C$
| outward normal vector  | $\nu$

These fields are all reported in units of megapascals - meters - years.
This unit system is a little unusual; we borrowed it from the package [Elmer/ICE](https://elmerice.elmerfem.org/).
It has the advantage of making certain physical constants, like the Glen flow law rate factor, live in a fairly sensible numerical range, whereas the values are often either gigantic or tiny in MKS units.


### Momentum conservation

J.D. Forbes in 1848 was the first Western scientist to correctly identify viscous deformation as the reason why glaciers flow.
In his original paper on the subject, Forbes has a wonderful quote about this realization:

> There is something pleasing to the imagination in the unexpected analogies presented by a torrent of fiery lava and the icy stream of a glacier.

Both lava and ice flow can be described by the exact same mathematics, and that mathematics is the *Stokes equations.*

The Stokes equations consist of three parts: a conservation law, a constitutive relation, and boundary conditions.
First, the *conservation law* states that the flux of stress across the boundary of a control volume $K$ cancels out exactly the body forces $f$:

$$\int_{\partial K}(\tau - pI)\cdot\nu\, ds + \int_Kf\, dx = 0.$$

The right-hand side is zero because we're assuming that the surface and body forces are roughly in balance and thus the acceleration that a fluid parcel experiences is negligible.
If we were to leave those terms in we would have the full Navier-Stokes equations.
When we apply the usual continuum mechanics arguments, we get a system of PDEs

$$\nabla\cdot\tau - \nabla p + f = 0.$$

To close this set of equations, we'll also need a *constitutive relation* between the deviatoric stress tensor and either the velocity or its gradient.
For a plain old viscous Newtonian fluid, the deviatoric stress and the strain rate tensor

$$\dot\varepsilon(u) \equiv \frac{1}{2}\left(\nabla u + \nabla u^\top\right)$$

are linearly proportional to each other.
But glacier ice is not a Newtonian fluid!
Glen and Nye showed through a series of laboratory experiments in the 1950s that ice is a *shear-thinning* material and that the strain rate is roughly a power-law function of stress:

$$\dot\varepsilon = A|\tau|^{n - 1}\tau$$

where $A$ is a temperature-dependent *rate factor*, $n \approx 3$ is the *flow law exponent*, and $|\tau|$ denotes the second invariant of a rank-2 tensor: $|\tau| \equiv \sqrt{\tau : \tau / 2}$.
The constitutive relation can be inverted to give an expression for the stress tensor in terms of the strain rate tensor, which again is the symmetrized gradient of the velocity.
By substituting this expression for the stress tensor into the conservation law, we arrive at a second-order quasilinear partial differential equation for the velocity field.

Finally, we have to know what conditions apply at the system boundaries.
At the ice surface, there is effectively zero stress:

$$(\tau - pI)\cdot\nu|_{z = s} = -p_0\nu$$

where $p_0$ is atmospheric pressure.
If we were explicitly modeling firn and snow, incorporating wind-blowing effects would be more of a problem.
At the ice base things get much more interesting because there are different boundary conditions in the normal and tangential directions.
In the normal direction, the ice velocity has to equal to the rate of basal melting:

$$u\cdot\nu|_{z = b} = \dot m.$$

In the tangential direction, frictional contact with the bed creates resistive stresses.
The relationship between resistive stresses and the ice velocity and other fields is the content of the *sliding law*.
One of the oldest proposed sliding laws, based on the theory of [*regelation*](https://en.wikipedia.org/wiki/Regelation), is due to work by Weertman in the 1960s.
Weertman sliding is a power-law relation between stress and sliding speed:

$$(\tau - pI)\cdot\nu|_{z = b} = -C|u|^{1/m - 1}u,$$

where $m$ is the *sliding exponent*.
In Weertman's theory, the sliding exponent is identical to the Glen flow law exponent $n$ because sliding occurs more through deformation within the ice.
The Weertman sliding law makes sense for glaciers flowing over hard beds, but several discoveries in the 1980s found that Antarctic ice streams more typically flow over soft, deformable sediments, with meltwater lubricating flow.
For these types of glaciers, sliding is more due to plastic failure within subglacial sediments.
Plastic sliding would imply that the basal shear stress is equal to the yield stress of the sediment regardless of the sliding speed, in which case the sliding exponent $m$ is equal to $\infty$.
The Schoof or regularized Coulomb friction law is a synthesis of the two types of sliding.

Rather than express the Stokes equations as one big nonlinear PDE, we assume in icepack that all of the diagnostic physics can be derived from an *action principle*.
The action principle states that the velocity and pressure that solve the Stokes equations are really also the critical point of a certain functional, called the action.
The action for the Stokes equations with the Weertman sliding law is

$$J = \int_\Omega\left(\frac{n}{n + 1}A^{-1/n}|\dot\varepsilon|^{1/n + 1} - p\nabla\cdot u - f\cdot u\right)dx + \frac{m}{m + 1}\int_{\Gamma_b}C|u|^{1/m + 1}ds.$$

We've found that expressing the diagnostic model through an action principle is advantageous because there are more and better numerical methods for solving constrained convex optimization problems than there are for general nonlinear systems of equations.
On top of that, an action principle is shorter to write down.


### Simplification

Nearly all terrestrial glacier flows have much wider horizontal than vertical extents.
By expanding the equations of motion in the aspect ratio $\delta = H/L$, it's possible to derive PDE systems that are much simpler than the Stokes equations.
Eliminating terms that scale like $\delta$, the vertical component of the momentum balance becomes

$$\frac{\partial}{\partial z}(\tau_{zz} - p) - \rho g = 0.$$

By integrating this equation in the vertical direction and using the fact that $\tau_{xx} + \tau_{yy} + \tau_{zz} = 0$, we can write the pressure as a function of the surface elevation and the horizontal components of the deviatoric stress tensor.
This leaves us with a 3D differential equation for the two horizontal components of the velocity.
The `HybridModel` class in icepack describes this system, known in the literature as either the *first-order* equations or the *Blatter-Pattyn* equations.
We can then depth-average them to arrive at a purely 2D system called the *shallow stream equations*.
To see all the details, you can consult the very excellent book by [Greve and Blatter](https://link.springer.com/book/10.1007/978-3-642-03415-2).
The `IceStream` class in icepack describes the depth-averaged system.

For completeness sake, we'll write down the action functional for the shallow stream equations.
Since the vertical component of the velocity and stress tensor has been eliminated, in 2D we have a new definition of the effective strain rate:

$$|\dot\varepsilon| \equiv \sqrt{\frac{\dot\varepsilon : \dot\varepsilon + \text{tr}(\dot\varepsilon)^2}{2}}.$$

For the full 3D velocity, the trace of the strain rate tensor is zero -- this is another way of restating the divergence-free condition, which we'll discuss below.
But the 2D strain rate of the depth-averaged velocity field can have non-zero divergence.
The action functional then becomes

$$J = \int_\Omega\left(\frac{n}{n + 1}hA^{-1/n}|\dot\varepsilon(u)|^{1/n + 1} + \frac{m}{m + 1}C|u|^{1/m + 1} + \rho gh\nabla s\cdot u\right)dx.$$

Note how the friction terms are no longer part of a boundary integral.
The optimality conditions for this functional also result in a nonlinear elliptic system of partial differential equations.
But the action is purely convex instead of having a saddle point structure like the Stokes equations.
Consequently, they're easier to solve numerically, as well as having fewer unknowns and being posed over a lower-dimensional domain.


### Mass conservation

The other piece of the puzzle that we've left out is the mass conservation equation.
Ice is roughly incompressible -- we're ignoring snow and firn here -- so this can succinctly be expressed as

$$\nabla\cdot u = 0.$$

Strictly speaking, this condition is implied by the action principle for the Stokes equations that we wrote down above.
It's a constraint for which the pressure acts as a Lagrange multiplier.
In principle, we could use the velocity field computed from the Stokes equations to move the upper and lower free surfaces of the ice, and this is exactly what Elmer/ICE does.
For depth-averaged or simplified 3D models, however, the vertical velocity is eliminated entirely, which makes this front-tracking approach more difficult.
Instead, we can integrate the divergence-free condition to arrive at the 2D equation

$$\frac{\partial}{\partial t}h + \nabla\cdot h\bar u = \dot a - \dot m$$

for the ice thickness, where $\bar u$ is the depth-averaged ice velocity.
(The derivation is a little subtle when you get into it and we're leaving out some of the details here.
If you want to see all of them, have a look at [Greve and Blatter](https://link.springer.com/book/10.1007/978-3-642-03415-2).)
This is a linear hyperbolic equation which, by itself, should strike fear into the heart.
Most applications use explicit timestepping schemes for hyperbolic problems.
These methods require some care in choosing both the spatial and temporal discretization in order to guarantee stability.
We've opted to instead use a more expensive implicit timestepping scheme because these are usually unconditionally stable.
The additional expense of an implicit scheme is minute compared to the overall cost of solving the diagnostic equations.


### Everything else

The momentum and mass conservation equations are the two main components of an ice flow model, but there are several other processes at work with their own governing equations.

* **Temperature**: the ice temperature is governed by the heat equation, and most importantly strain heating within the ice and at the bedrock interface are sources of heat.
The ice temperature partly determines the rate factor $A$ in Glen's flow law and the temperature gradient partly determines how much heat can be transported through the ice and how much has to be absorbed through the latent heat of melting.
The governing PDE is the heat equation and the class `HeatTransport3D` from icepack contains a description, together with some common simplifications for ice flow.
* **Damage**: while the dominant mode of ice movement is viscous flow, it's also a brittle material and can form fractures.
Fracture mechanics models that resolve individual cracks are impractically expensive to apply at glacier-wide scales but there are a number of phenomenological models.
The class `DamageTransport` from icepack contains a specification of the continuum damage mechanics model of [Albrecht and Levermann](https://doi.org/10.3189/2012JoG11J191).
* **Calving**: the end state of ice damage is the breaking off or *calving* of icebergs into the ocean.
This problem is especially challenging because it means that the geometry is now dynamic.
There is at present no widely-accepted physical model that predicts the rate of iceberg calving well for both Greenland- or Alaska-type events (low amplitude, high frequency) and for Antarctic-type events (high amplitude, low frequency).
* **Fabric**: we've assumed above that the Glen flow law is purely isotropic, but sustained deformation along one axis can give ice crystal grains a preferred orientation.
* **Hydrology**: meltwater at the ice base is ultimately transported along the hydraulic potential gradient and out the ice edge; the degree to which the subglacial hydrological system is *channelized* or *distributed* partly determines the sliding resistance.

The discussion above assumes that the inputs from the oceans and atmosphere are known and prescribed.
We've adopted this limited viewpoint in order to keep the scope of the project small, but the cryosphere has non-trivial feedbacks with the atmosphere, the oceans, and the landscape.
We welcome any contributions of new code to model other unresolved physical processes in glaciology or to couple glaciers to other parts of the earth system.


### References

We've omitted a lot of details above we also haven't even attempted to describe other areas of glaciology, such as the interpretation of ice cores and climate records.
[The Physics of Glaciers](https://www.elsevier.com/books/the-physics-of-glaciers/cuffey/978-0-12-369461-4) by Cuffey and Paterson is a great reference for getting a broader picture of the field.
For a focus on ice dynamics from a more mathematical perspective, [Dynamics of Ice Sheets and Glaciers](https://link.springer.com/book/10.1007/978-3-642-03415-2) by Greve and Blatter is a must-read.
[A First Course in Continuum Mechanics](https://doi.org/10.1017/CBO9780511619571) by Gonzalez and Stuart is a good read if you want to brush up more on fundamental physics.
