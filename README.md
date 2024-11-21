## Problem 1: Supercritical AZURV1

A homogeneous, mono-energetic, 1D-planar geometry system pulsed at a supercritical condition of $k=1.1$.

The simulation is run for 20 mean free times, during which the particle population grows by $\exp(2)=7.389$ times.
A semi-analytical reference solution for neutron flux space-time distribution, $\phi(x,t)$, is available.
The problem is based on the time-dependent analytical transport benchmark suite AZURV1[^1].

[^1]: Ganapol, Barray D., et al. "Homogeneous infinite media time-dependent analytical benchmarks." International Meeting on Mathematical Methods for Nuclear Applications. Vol. 41. No. 25. 2001. [[link]](https://www.osti.gov/biblio/975281)

## Problem 2: Time-dependent Kobayashi Dog-Leg

A mono-energetic, 3D shielding system, featuring a dog-leg vacuum channel surrounded by a shielding material.

The problem is based on an NEA steady-state fixed-source benchmark problem suite [^2].
The time-dependence is introduced by turning the fixed-source source into a histogram pulse.
The quantity of interest is the 4D flux distribution, $\phi(x,y,z,t)$, in a fine mesh of 60x100x60x100.

[^2]: Kobayashi, Keisuke, Naoki Sugimura, and Yasunobu Nagaya. "3D radiation transport benchmark problems and results for simple geometries with void region." Progress in nuclear energy 39.2 (2001): 119-144. [[link]](https://www.sciencedirect.com/science/article/abs/pii/S0149197001000075)

## Problem 3: SHEM-361 Delayed Supercritical Point Kinetics

An infinite homogeneous system of 361 energy groups pulsed at a delayed supercritical condition.

The multigroup cross-section data is generated from a light-water reactor pin cell homogenization with OpenMC[^3] using the [SHEM-361](https://docs.openmc.org/en/latest/pythonapi/mgxs.html) energy group structure.
A logarithmic time-mesh tally is used to observe both the prompt and delayed neutron flux responses.
A semi-analytical reference solution for neutron flux energy-time distribution, $\phi_g(t)$, is available.

[^3]: Paul K. Romano, Nicholas E. Horelik, Bryan R. Herman, Adam G. Nelson, Benoit Forget, and Kord Smith, “OpenMC: A State-of-the-Art Monte Carlo Code for Research and Development,” Ann. Nucl. Energy, 82, 90–97 (2015). [[link]](https://www.sciencedirect.com/science/article/abs/pii/S030645491400379X) [[repository]](https://github.com/openmc-dev/openmc)
