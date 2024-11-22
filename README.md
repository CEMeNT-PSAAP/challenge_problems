## Problem 1: Supercritical AZURV1

A homogeneous, mono-energetic, 1D-planar geometry system pulsed at a supercritical condition of $k=1.1$.

The simulation is run for 20 mean free times, during which the particle population grows by $\exp(2)=7.389$ times.
A semi-analytical reference solution for neutron flux space-time distribution, $\phi(x,t)$, is available.
The problem is based on the time-dependent analytical transport benchmark suite AZURV1[^1].

[^1]: B. D. Ganapol, R. S. Baker, J. A. Dahl, R. E. Alcouffe, "Homogeneous Infinite Media Time-Dependent Analytical Benchmarks." International Meeting on Mathematical Methods for Nuclear Applications, 41:25, 2001. [[link]](https://www.osti.gov/biblio/975281)

## Problem 2: Time-dependent Kobayashi Dog-Leg

A mono-energetic, 3D shielding system featuring a dog-leg vacuum channel surrounded by a shielding material.

The problem is based on an NEA steady-state fixed-source benchmark problem suite [^2].
Time dependence is introduced by turning the fixed source source into a histogram pulse.
The quantity of interest is the 4D flux distribution, $\phi(x,y,z,t)$, in a fine mesh of 60x100x60x100.

[^2]: Keisuke Kobayashi, Naoki Sugimura, and Yasunobu Nagaya, "3D Radiation Transport Benchmark Problems and Results for Simple Geometries with Void Region." Progress in Nuclear Energy, 39:2, 119-144 (2001). [[link]](https://www.sciencedirect.com/science/article/abs/pii/S0149197001000075)

## Problem 3: SHEM-361 Delayed Supercritical Point Kinetics

An infinite homogeneous system of 361 energy groups pulsed at a delayed supercritical condition.

The multigroup cross-section data is generated from a light-water reactor pin cell homogenization with OpenMC[^3] using the [SHEM-361](https://docs.openmc.org/en/latest/pythonapi/mgxs.html) energy group structure.
A logarithmic time-mesh tally is used to observe both the prompt and delayed neutron flux responses.
A semi-analytical reference solution for neutron flux energy-time distribution, $\phi_g(t)$, is available.

[^3]: Paul K. Romano, Nicholas E. Horelik, Bryan R. Herman, Adam G. Nelson, Benoit Forget, and Kord Smith, “OpenMC: A State-of-the-Art Monte Carlo Code for Research and Development,” Annals of Nuclear Energy, 82, 90–97 (2015). [[link]](https://www.sciencedirect.com/science/article/abs/pii/S030645491400379X) [[repository]](https://github.com/openmc-dev/openmc)

## Problem 4: C5G7-TD4-4

A 4x4 multigroup light water reactor assembly turned off-critical by maneuvers of control rod assemblies.

This is the fourth test problem of Exercise 4 of the C5G7-TD benchmark suite [^4].
The problem consists of two parts: (1) running static k-eigenvalue calculation to sample the steady-state initial condition and (2) running the transient problem using the obtained initial source neutrons.

[^4]: Jason Hou, Kostadin N. Ivanov, Victor F. Boyarinov, and Peter A. Formichenko, "OECD/NEA benchmark for time-dependent neutron transport calculations without spatial homogenization," Nuclear Engineering and Design, 317, 177-189 (2017). [[link]](https://www.sciencedirect.com/science/article/abs/pii/S0029549317300572?via%3Dihub)

## The Four-Phase Transient

A nuclear reactor transient exercise exhibiting several key neutronics transient features.
The transient is driven by time-dependent control rod positions and neutron source strengths.
- Phase 1: Start-up convergence of a source-driven subcritical configuration,
- Phase 2: Control rods withdrawal demonstrating the S-wave power maneuver,
- Phase 3: Power excursion from prompt supercriticality,
- Phase 4: Reactor shutdown emphasizing the delayed neutron effects.
Stuck control rods are considered to promote spatial asymmetry in the fux distribution.
Quantities of interest include total neutron density in time and axially-segmented pin power and fluxes.

## Problem 5: C5G7 Four-Phase Transient

The C5G7-TD model [^4] going through the Four-Phase Transient.

## Problem 6: C5CE Four-Phase Transient

A _continuous-energy_ version of the C5G7-TD model [^4] going through the Four-Phase Transient.

## Problem 7: SMR-MG Four-Phase Transient

A _multigroup_ NuScale-inspired small modular reactor model [^5] going through the 4-phase transients.

[^5]: "NuScale Codes and Methods Framework Description Report," NRC, NP-TR-0812-1682-NP (2013). [[link]](https://www.nrc.gov/docs/ML1301/ML13018A154.pdf)

## Problem 8: SMR Four-Phase Transient

A NuScale-inspired small modular reactor model [^5] going through the 4-phase transients.

## Problem 9: SMR-Depleted Four-Phase Transient

A _depleted_ NuScale-inspired small modular reactor model [^5] going through the 4-phase transients.

## Problem 10: Dragon

A fast neutron burst induced by strong reactivity pulses from a drop-through of a highly enriched uranium slug.

The problem attempts to simulate the Dragon machine experiment by Otto Frisch [^6].

[^6]: Robert Kimpland, Travis Grove, Peter Jaegers, Richard Malenfant, and William Myers, "Critical Assemblies: Dragon Burst Assembly and Solution Assemblies," Nuclear Technology, 207, S81-S99 (2021). [[link]](https://www.tandfonline.com/doi/pdf/10.1080/00295450.2021.1927626)
