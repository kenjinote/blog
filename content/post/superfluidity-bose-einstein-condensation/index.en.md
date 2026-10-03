---
title: "Superfluidity and Bose-Einstein Condensation: The Physics of Macroscopic Quantum Phenomena Near Absolute Zero"
description: "Liquid helium climbing walls with zero viscosity, the fountain effect, and the topology of quantum vortices. The marvel of BEC where bosons degenerate into a single wavefunction."
slug: "superfluidity-bose-einstein-condensation"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["quantum-mechanics", "condensed-matter", "superfluidity", "thermodynamics"]
image: "eyecatch.jpg"
---

# Superfluidity and Bose-Einstein Condensation: The Physics of Macroscopic Quantum Phenomena Near Absolute Zero

In modern physics, the ultracold world near absolute zero (0 K = -273.15 °C) is a treasure trove of astonishing phenomena that profoundly betray our everyday intuition. Among them, "Superfluidity" and "Bose-Einstein Condensation (BEC)" have continued to fascinate many physicists as the most prominent examples of "macroscopic quantum phenomena," where microscopic quantum mechanical properties are directly observed on a macroscopic scale.

Liquid helium, which exhibits completely zero viscosity and spontaneously creeps up the walls of its container. The thermomechanical effect (fountain effect), where liquid spouts from a fine nozzle when exposed to light. And BEC, where trillions of atoms fall into exactly the same quantum state and behave as a single giant matter wave. In this article, we will delve deeply into how these phenomena were discovered and theoretically elucidated, from their historical background to their advanced theoretical framework, from a highly detailed and academic perspective.

---

## Chapter 1: The Challenge Toward Absolute Zero and the History of Helium Liquefaction

### 1.1 The Dawn of Low-Temperature Physics and the Liquefaction of Permanent Gases
In the late 19th century, one of the major themes in physics was the question, "Can all gases be liquefied by cooling and pressurization?" Through the efforts of Michael Faraday and others, many gases were liquefied, but oxygen, nitrogen, hydrogen, and helium were called "permanent gases," and their liquefaction was considered extremely difficult.

However, with the development of thermodynamics and the advancement of cooling technologies utilizing the Joule-Thomson effect, oxygen was liquefied in 1877, and hydrogen liquefaction (boiling point approximately 20 K) was achieved by James Dewar in 1898. The last remaining uncharted gas was helium.

### 1.2 The Liquefaction of Helium and the Glory of Kamerlingh Onnes
Heike Kamerlingh Onnes, who established a cryogenic laboratory at Leiden University in the Netherlands, made meticulous preparations and built a massive liquefaction apparatus. On July 10, 1908, using liquid hydrogen for pre-cooling and repeating Joule-Thomson expansion, he finally succeeded in liquefying helium. The boiling point of liquid helium is 4.2 K, and humanity had opened the door to the ultracold world just 4 degrees short of absolute zero. For this achievement, Kamerlingh Onnes was awarded the Nobel Prize in Physics in 1913.

The production of liquid helium directly led to the discovery of superconductivity in 1911 (a phenomenon where the electrical resistance of mercury drops to zero at 4.2 K), but it took several more decades before the anomalous properties of liquid helium itself became clear.

### 1.3 The Lambda Transition and the Discovery of Superfluidity
From the 1920s to the 1930s, Willem Hendrik Keesom and others discovered that as liquid helium is cooled further, its specific heat exhibits a logarithmic divergence at approximately 2.17 K. Because the graph of the temperature variation of this specific heat resembles the Greek letter "$\lambda$ (lambda)," this phase transition was named the "$\lambda$ (lambda) transition." The phase above 2.17 K ($T_\lambda$) is called "helium I," and the lower temperature phase is called "helium II."

Helium II exhibited anomalous behavior completely different from ordinary liquids. The most dramatic discoveries were reported successively in 1938. Pyotr Kapitza in Moscow, and John F. Allen and Don Misener at Cambridge University independently discovered that helium II flows through extremely fine capillaries without resistance (with zero viscosity).

Kapitza named this anomalous fluidity "superfluidity," drawing an analogy from superconductivity. In the experiment conducted by Kapitza, a microscopic gap (a few microns) was created by facing two glass disks, and the viscosity was measured as liquid helium flowed through it. While helium I exhibited resistance as a normal viscous fluid, the moment it dropped below $T_\lambda$, the outflow velocity increased dramatically, and it was confirmed that the apparent viscosity coefficient plummeted to at least less than $10^{-4}$ of the normal value.

Even more strangely, measurements using a rotational viscometer (an experiment in which a cylinder is rotated in the liquid) yielded a contradictory result, behaving as if helium II still had finite viscosity. This seemingly incomprehensible phenomenon of "zero viscosity in a narrow tube, yet exerting viscous resistance on a rotating body" would later be beautifully resolved by the "two-fluid model."

---

## Chapter 2: The Theoretical Framework of Bose-Einstein Condensation (BEC)

The key to understanding the superfluidity of liquid helium from a microscopic perspective lies in quantum statistical mechanics. A helium-4 atom is composed of 2 protons, 2 neutrons, and 2 electrons, and the sum of its spins is an integer (0). That is, helium-4 is a "boson." What happens when a macroscopic ensemble of bosons is cooled toward absolute zero? We will derive its theoretical framework.

### 2.1 Bose Statistics and Fermi Statistics
In quantum mechanics, identical particles are fundamentally indistinguishable. Based on the symmetry of the wavefunction under particle exchange, particles are broadly classified into two categories.
- **Bosons**: Particles with integer spin. The wavefunction is symmetric (its sign does not change) under particle exchange. They do not obey Pauli's exclusion principle, and multiple particles can simultaneously occupy the same quantum state.
- **Fermions**: Particles with half-integer spin. The wavefunction is antisymmetric (its sign changes) under particle exchange. They obey Pauli's exclusion principle, and only one particle can occupy a given quantum state.

Consider the statistical mechanics of an ideal Bose gas. Letting the grand partition function be $\Xi$, the chemical potential be $\mu$, and the inverse temperature be $\beta = 1 / (k_B T)$, the average number of particles $\langle n_i \rangle$ in a state with energy $\epsilon_i$ is given by the Bose-Einstein distribution function:
$$ \langle n_i \rangle = \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1} $$
Here, for the number of particles to be non-negative, $\epsilon_i - \mu > 0$ must hold for all states $i$. Setting the ground state energy to $\epsilon_0 = 0$, the chemical potential must always satisfy $\mu \leq 0$.

### 2.2 Thermal de Broglie Wavelength and the Emergence of the Macroscopic Wavefunction
The index representing the spread of a particle as a wave is the "Thermal de Broglie Wavelength" $\lambda_{dB}$. From the thermal average of kinetic energy $p^2 / 2m \sim k_B T$, the momentum is $p \sim \sqrt{m k_B T}$, so the de Broglie wavelength $\lambda = h/p$ is approximately given by:
$$ \lambda_{dB} = \sqrt{\frac{2\pi \hbar^2}{m k_B T}} $$

At high temperatures, $\lambda_{dB}$ is very short, much smaller than the average distance between particles $d = (V/N)^{1/3}$. At this time, particles behave like classical billiard balls and can be adequately approximated by Maxwell-Boltzmann statistics.
However, as the temperature $T$ is lowered, $\lambda_{dB}$ gradually becomes longer. Then, at a certain critical temperature $T_c$, the wavelength $\lambda_{dB}$ becomes comparable to the interparticle distance $d$ ($\lambda_{dB} \sim d$). At this point, the wavefunctions of individual particles begin to overlap spatially, and quantum mechanical interference effects become manifest on a macroscopic scale.

As the temperature is lowered further, a large number of bosons undergo an avalanche into the lowest energy state (ground state). In this state, countless particles behave as a single giant matter wave with perfectly identical phase, namely a "Macroscopic Wavefunction $\Psi(\mathbf{r}) = \sqrt{n_0(\mathbf{r})} e^{i\theta(\mathbf{r})}$". This is Bose-Einstein Condensation (BEC).

### 2.3 Mathematical Derivation of the Condensation Transition Temperature $T_c$
Consider a system of ideal Bose gas in a 3D volume $V$. The total number of particles $N$ in the system is expressed as the sum of the average number of particles in each state:
$$ N = \sum_i \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1} $$

In a macroscopic system ($V \to \infty$), the sum over states can be replaced by an integral over energy. The density of states $D(\epsilon)$, assuming a spin degree of freedom of 1, is:
$$ D(\epsilon) = \frac{V}{(2\pi)^2} \left( \frac{2m}{\hbar^2} \right)^{3/2} \sqrt{\epsilon} $$
Evaluating the number of particles using the integral, we get:
$$ N_{ex} = \int_0^\infty D(\epsilon) \frac{1}{e^{\beta(\epsilon - \mu)} - 1} d\epsilon $$
This represents the number of particles $N_{ex}$ in the excited states.
As the temperature is lowered (as $\beta$ increases), the chemical potential $\mu$ approaches 0 to maintain $N_{ex}$. However, setting $\mu = 0$ yields an upper bound for the integral value:
$$ N_{max} = \frac{V}{(2\pi)^2} \left( \frac{2m}{\hbar^2} \right)^{3/2} \int_0^\infty \frac{\sqrt{\epsilon}}{e^{\beta \epsilon} - 1} d\epsilon $$
Here, applying the change of variables $x = \beta \epsilon$, the integral part can be calculated using the Gamma function $\Gamma(z)$ and the Riemann zeta function $\zeta(z)$ as follows:
$$ \int_0^\infty \frac{\sqrt{\epsilon}}{e^{\beta \epsilon} - 1} d\epsilon = (k_B T)^{3/2} \int_0^\infty \frac{x^{1/2}}{e^x - 1} dx = (k_B T)^{3/2} \Gamma(3/2) \zeta(3/2) $$
Since $\Gamma(3/2) = \sqrt{\pi}/2$ and $\zeta(3/2) \approx 2.612$, the maximum number of particles that the excited states can accommodate is:
$$ N_{max} = V \left( \frac{m k_B T}{2\pi \hbar^2} \right)^{3/2} \zeta(3/2) = \frac{V}{\lambda_{dB}^3} \zeta(3/2) $$
What happens if the total number of particles $N$ exceeds $N_{max}$? The excess particles $N_0 = N - N_{max}$ have no choice but to condense into the ground state with energy $\epsilon = 0$, which is not included in the integral ($\epsilon > 0$). This is the mathematical mechanism of BEC.

The critical temperature $T_c$ at which condensation begins is defined as the temperature where $N = N_{max}(T_c)$. Solving this for $T_c$ yields:
$$ T_c = \frac{2\pi \hbar^2}{m k_B} \left( \frac{n}{\zeta(3/2)} \right)^{2/3} $$
(where $n = N/V$ is the number density).
This formula gives the exact BEC transition temperature for a non-interacting ideal gas. Substituting the density of liquid helium gives $T_c \approx 3.1$ K, a value close to the actual $\lambda$ transition temperature of 2.17 K. This agreement strongly suggests that the superfluidity of helium II is essentially a phenomenon related to BEC. However, because liquid helium is a "strongly correlated quantum liquid" with very strong interactions between particles, there is a deviation from the ideal gas model.

---

## Chapter 3: The Two-Fluid Model of Tisza and Landau

To explain the strange property of superfluid helium, which "flows with zero viscosity in a narrow tube but shows viscous resistance to a rotating body," László Tisza proposed a groundbreaking phenomenology in 1938. Later, in 1941, Lev Landau perfected this into the "Two-Fluid Model" as a more sophisticated theory based on quantum mechanical microscopic foundations.

### 3.1 Coexistence of Normal Fluid and Superfluid Components
The core of the two-fluid model is to view helium II as a system in which two fluid components with entirely different physical properties are independently intermingled.
The total density $\rho$ and flow velocity $\mathbf{v}$ of the system are expressed as the sum of the two components as follows:
$$ \rho = \rho_n + \rho_s $$
$$ \mathbf{j} = \rho_n \mathbf{v}_n + \rho_s \mathbf{v}_s $$
Here,
- **Normal fluid component ($\rho_n$)**: A component that has finite viscosity and carries entropy. It corresponds to an ensemble of particles in thermally excited states.
- **Superfluid component ($\rho_s$)**: A component that has completely zero viscosity and no entropy (it is in the same state as at absolute zero). It corresponds to an ensemble of particles in a macroscopic quantum state (BEC state).

At absolute zero ($T = 0$), everything is the superfluid component ($\rho_s = \rho, \rho_n = 0$), but as the temperature rises, the proportion of the normal fluid component increases, and the superfluid component vanishes at $T_\lambda$ ($\rho_s = 0, \rho_n = \rho$).

Using this model, the aforementioned contradiction of viscosity is beautifully resolved. In an experiment passing through an ultra-fine tube, the normal fluid component with viscosity is blocked by friction with the tube walls, while only the non-viscous superfluid component slips through the tube, making the apparent viscosity zero. On the other hand, in an experiment where a cylinder is rotated in the bulk liquid, the cylinder generates friction with the normal fluid component, so a finite viscosity is observed.

### 3.2 Thermomechanical Effect (Fountain Effect) and Mechanocaloric Effect
The property that the superfluid component "has no entropy" causes an astonishing phenomenon where heat and matter flow are directly coupled. A typical example of this is the "Thermomechanical effect" or "Fountain effect."

An ultrafine porous filter (superleak) packed with very fine powder is placed in the middle of a U-tube, and both sides are filled with helium II. When one side of the filter is heated with a heater, the liquid level on the heated side rises, and if conditions are right, helium spouts vigorously from the nozzle.
The mechanism of this phenomenon is as follows. When the temperature on the heated side rises, according to the two-fluid model, the proportion of the normal fluid component $\rho_n$ in that region increases, and the superfluid component $\rho_s$ decreases. Then, a gradient of chemical potential (similar to osmotic pressure) is generated, attempting to eliminate the concentration gradient of the superfluid component through the superleak. Since the normal fluid component cannot pass through the filter, only the superfluid component flows in large quantities from the cold side to the hot side, pushing up the liquid level.
Thermodynamically, London's equation holds between the pressure difference $\Delta P$ and the temperature difference $\Delta T$:
$$ \Delta P = \rho S \Delta T $$
($S$ is the entropy per unit mass)

Conversely, when helium II is forced out through a superleak, what flows out is only the superfluid component carrying no entropy, which causes the temperature of the remaining liquid to rise. This is called the mechanocaloric effect.

### 3.3 The Physics of Second Sound
In ordinary fluids, a "sound wave" is a compressional wave (pressure wave) of density. However, in helium II, because two independent velocity fields $\mathbf{v}_n$ and $\mathbf{v}_s$ exist, two types of waves can propagate.
- **First Sound**: A wave in which the normal and superfluid components oscillate in phase. This corresponds to an ordinary density wave (pressure wave).
- **Second Sound**: A wave in which the normal and superfluid components oscillate completely out of phase (in opposite directions). While the overall density is kept constant, the ratio of the normal fluid component (a mass of entropy) to the superfluid component oscillates spatially, so this effectively propagates as a "temperature wave (heat wave)."

In ordinary materials, heat is transmitted as a diffusion phenomenon, but in helium II, heat propagates as an unattenuated "wave" at the speed of sound (second sound speed). This phenomenon was also predicted by Landau and later demonstrated experimentally, decisively proving the correctness of the two-fluid model.

---

## Chapter 4: Landau's Critical Velocity for Superfluidity and the Elementary Excitation Spectrum

The theory of Bose-Einstein condensation was predicated on an ideal gas and could not explain the strong interactions acting between helium atoms. In an ideal Bose gas without interactions, superfluidity does not actually appear (it is easily excited by impurity scattering). Lev Landau formulated liquid helium as a "background liquid in the ground state at absolute zero" with a "gas of elementary excitations" riding on it.

### 4.1 Phonons and Rotons: Energy-Momentum Dispersion Curve
To explain the thermal properties of helium II, Landau assumed the relationship between the energy $\epsilon$ and the momentum $p$ of the elementary excitations (the dispersion relation $\epsilon(p)$) as follows.

1. **Phonon Region (Low Momentum Region)**
   Long-wavelength excitations are fluctuations in the density of the entire fluid, i.e., quantized sound waves (phonons). The energy is proportional to the momentum:
   $$ \epsilon(p) = c p $$
   ($c$ is the speed of first sound)

2. **Roton Region (High Momentum Region)**
   As the momentum increases, the dispersion curve passes through a local maximum and has a local minimum. Landau named the excitations near this minimum "Rotons." The dispersion relation for rotons is approximated by a parabola:
   $$ \epsilon(p) = \Delta + \frac{(p - p_0)^2}{2\mu} $$
   Here, $\Delta$ is the roton gap energy, $p_0$ is the momentum at the minimum, and $\mu$ is the effective mass of the roton.

This peculiar dispersion curve was later measured extremely accurately by inelastic neutron scattering experiments, beautifully proving Landau's genius intuition.

### 4.2 Zero Friction Impossibility of Scattering Proof by Critical Velocity $v_c$
Landau's greatest achievement lies in using this dispersion relation to dynamically prove the fundamental mechanism of superfluidity—"why helium II can flow without friction against the walls" (Landau's critical velocity theorem).

Assume that a massive object of mass $M$ (for example, a microscopic protrusion on the wall of a capillary) is moving at a constant velocity $v$ in liquid helium at absolute zero. For this object to decelerate due to friction with helium, it must impart a portion of its kinetic energy to the helium and generate "elementary excitations" within it.
Suppose one elementary excitation with momentum $p$ and energy $\epsilon(p)$ is generated. From the laws of conservation of energy and momentum, assuming the change in velocity of the object is infinitesimally small, the following relation holds:
$$ \Delta E = \mathbf{v} \cdot \mathbf{p} = \epsilon(p) $$
Since $\mathbf{v} \cdot \mathbf{p} = v p \cos\theta \leq v p$, the condition for generating an elementary excitation is:
$$ v \geq \frac{\epsilon(p)}{p} $$

In other words, if the velocity $v$ of the object is smaller than the minimum value of $\epsilon(p)/p$ for all possible momenta $p$, no elementary excitations can be generated whatsoever, and no energy dissipation (friction) occurs at all. This limiting velocity is called the Landau critical velocity $v_c$:
$$ v_c = \min \left[ \frac{\epsilon(p)}{p} \right] $$

If liquid helium were an ideal Bose gas, it would have the dispersion relation of free particles $\epsilon(p) = p^2 / 2m$, so $v_c = \min [p/2m] = 0$. This means that no matter how slowly it moves, excitations would occur and it would not become a superfluid.
However, in real liquid helium, due to interactions, the dispersion curve starts linearly ($\epsilon = c p$), so the slope near the origin is $c$ (the speed of sound, approximately 240 m/s). Finding the minimum from the overall shape of the dispersion curve, the slope of the tangent heading toward the roton minimum gives $v_c$, which is approximately 60 m/s.
(*The critical velocity observed in actual experiments is much smaller, on the order of a few cm/s, but this was later elucidated by Richard Feynman and others as the generation mechanism of "quantum vortices.")

Thus, the existence of a "gap" or a "finite slope" in the energy dispersion relation of the system is the absolute condition guaranteeing superfluidity (flow with zero friction).

---

## Chapter 5: Quantized Vortices and Topological Defects

While Landau's critical velocity theory explained the microscopic origin of superfluidity, the reason why the experimentally observed critical velocity was much lower than the theoretical value remained a mystery. This mystery was unravelled and linked to the phase of the macroscopic wavefunction of the superfluid (topology) by the "quantized vortex" theory by Lars Onsager and Richard Feynman.

### 5.1 Phase of the Macroscopic Wavefunction and Quantization of Circulation
A superfluid undergoing BEC is described by a single macroscopic wavefunction $\Psi(\mathbf{r}) = \sqrt{n_0(\mathbf{r})} e^{i\theta(\mathbf{r})}$. Here, $n_0(\mathbf{r})$ is the number density of the condensate, and $\theta(\mathbf{r})$ is the phase.
The velocity field $\mathbf{v}_s$ of the superfluid is derived from the probability current density in quantum mechanics to be proportional to the spatial gradient of the phase:
$$ \mathbf{v}_s = \frac{\hbar}{m} \nabla \theta $$

In fluid dynamics, an indicator showing the degree of rotation of a fluid is the "Circulation $\kappa$." It is defined as the line integral of the velocity vector $\mathbf{v}_s$ along a closed curve $C$.
$$ \kappa = \oint_C \mathbf{v}_s \cdot d\mathbf{r} = \frac{\hbar}{m} \oint_C \nabla \theta \cdot d\mathbf{r} $$
The integral part means the change in phase $\Delta\theta$ when going once around the closed curve $C$.
Here, there is a quantum mechanical requirement that the wavefunction $\Psi(\mathbf{r})$ must have a unique (single-valued) value at each point in space. Therefore, when returning to the original position after going once around a closed curve, the phase must be identical to its original value, or shifted by an integer multiple of $2\pi$:
$$ \Delta\theta = 2\pi n \quad (n = 0, \pm 1, \pm 2, \dots) $$
Substituting this into the circulation equation yields an astonishing result.
$$ \kappa = \frac{\hbar}{m} (2\pi n) = n \frac{h}{m} $$
In other words, the circulation in a superfluid cannot take continuous values, and is completely "quantized" in units of $h/m$ (Planck's constant $h$ divided by the mass $m$ of a helium atom). This is the "quantization of circulation."

### 5.2 Vortex Lattices and Topological Defects in Rotating Liquid Helium
When a container holding an ordinary viscous fluid is rotated, the fluid rotates entirely like a rigid body, drawing a paraboloid. However, the (superfluid component of) superfluid helium has the property $\nabla \times \mathbf{v}_s = (\hbar/m) \nabla \times \nabla \theta = 0$, meaning it is irrotational (vortex-free), so even if the container is slowly turned, the contents do not rotate with it.
However, as the rotational speed is gradually increased, the moment it exceeds a certain critical angular velocity, innumerable lines (vortex filaments) of "Quantized Vortices" penetrate into the superfluid.

At the center (core) of a quantum vortex, the phase becomes a singularity and cannot be defined, so the superfluid density $n_0$ becomes zero (i.e., it becomes a normal fluid or a vacuum). Around the core, the fluid rotates with a quantized circulation $\kappa = h/m$ (usually the minimal state of $n=1$ is energetically stable).
When the rotational speed is further increased, the number of quantum vortices increases, and they repel each other to form a regular triangular lattice (a vortex lattice similar to the Abrikosov lattice). Macroscopically, this assembly of innumerable quantum vortices behaves as if the entire fluid is undergoing rigid-body rotation.

The discrepancy in Landau's critical velocity was also explained by these quantum vortices. When flowing along the walls of a capillary tube, even at very small flow velocities, quantum vortices are generated by microscopic unevenness on the walls. Because the energy required to generate these quantum vortices is much lower than that for roton excitations, the experimental critical velocity was extremely small compared to Landau's theoretical value. Quantum vortices function as "topological defects" that destroy superfluidity.

---

## Chapter 6: Realization of Gaseous BEC by Laser Cooling and Expansion into Modern Physics

Because liquid helium has extremely strong interparticle interactions, the condensate fraction is limited to about 10% even at absolute zero, far from the BEC of a pure ideal gas. To realize a true "BEC in a dilute gas," it was necessary to cool a gas, dilute enough that interatomic interactions could be ignored, close to absolute zero.

### 6.1 Achievement of BEC in Alkali Atom Gases
From the 1980s to the 1990s, innovative technologies such as laser cooling (Doppler cooling, Sisyphus cooling), magnetic traps, and evaporative cooling were developed, making it possible to cool atomic gases to the nanokelvin ($10^{-9}$ K) regime.
Then, in 1995, Eric Cornell and Carl Wieman of the University of Colorado (JILA) using a rubidium ($^{87}$Rb) atomic gas, and in the same year, Wolfgang Ketterle of MIT using a sodium ($^{23}$Na) atomic gas, succeeded for the first time in human history in directly observing Bose-Einstein condensation in dilute alkali atomic gases. They were awarded the Nobel Prize in Physics in 2001 for this achievement.

In an experiment conducted by Ketterle's group, distinct "interference fringes" were observed by spatially interfering two independent BECs. This was conclusive evidence that macroscopic-scale lumps of matter were behaving as a single matter wave.

### 6.2 Superfluid-Mott Insulator Transition in Optical Lattices
Modern BEC research goes beyond simply confirming the phenomenon and has developed into applications as "quantum simulators." When a BEC is introduced into a periodic potential (Optical Lattice) created by interfering opposing laser beams, the atoms behave like electrons in the crystal lattice of a solid.
By adjusting the intensity of the lasers, the ratio between the interatomic interactions and hopping (the tunnel effect to adjacent sites) can be freely controlled. When the interaction is weak, the atoms roam freely across the entire system in a phase-aligned state, resulting in a "superfluid state." However, as the interaction is made stronger, the atoms undergo a quantum phase transition into a "Mott Insulator state," where one atom is localized at each lattice point and macroscopic phase coherence is completely destroyed.
This Superfluid-Mott insulator transition (observed by Greiner et al. in 2002) opened the way for precisely verifying the Hubbard model of strongly correlated electron systems (such as high-temperature superconductors) in ideal artificial systems.

### 6.3 Unified Understanding with Superconductivity (BEC of Cooper Pairs)
Finally, let us touch on the deep relationship between superfluidity and superconductivity. Superconductivity can be interpreted as a phenomenon where conduction electrons (fermions) in a metal form pairs (Cooper pairs) by twos due to attractive forces mediated by phonons (lattice vibrations), and these pairs behave like bosons to undergo BEC (BCS theory).
In recent years, using Fermi atomic gases, research on the "BCS-BEC crossover" has been actively conducted, where the interactions between atoms are controlled by a magnetic field (Feshbach resonance), continuously changing the state from the BEC of molecules (BEC limit) to the BCS state of Cooper pairs (BCS limit).

Superfluidity and BEC are ultimate physical phenomena where the laws governed by microscopic quantum mechanics are extended to everyday macroscopic scales. Flow with zero viscosity, quantization of circulation, and interference of matter waves. These are all nothing but the most fundamental and pure aspects of the universe that nature shows us under the extreme condition of absolute zero.
