---
title: "Mega-Constellations and Orbital Mechanics: The Starlink Paradigm"
description: "A comprehensive mathematical and physical exploration of artificial satellite mega-constellations, covering orbital mechanics, communication limits, hardware, and space sustainability."
slug: "satellite-mega-constellation-orbital-mechanics-starlink"
categories: ["Space", "Technology"]
tags: ["Starlink", "Orbital Mechanics", "Mega-Constellation"]
image: "eyecatch.jpg"
date: "2026-10-03T13:00:00+09:00"
---

# Introduction: The Dawn of Mega-Constellations Covering Humanity's Skies
In the 21st century's space development, the most ambitious and dramatic transformation is brought about by "Mega-Constellations" of artificial satellites. Led by SpaceX's Starlink, along with OneWeb and Amazon's Project Kuiper, an unprecedented scale of satellite swarms numbering in the thousands to tens of thousands is about to blanket Earth's low orbit. This is not merely an evolution of communication technology, but a grand endeavor for humanity to design and bring under control the three-dimensional canvas of outer space with the extreme precision of mathematics and physics.

In this article, we will thoroughly unravel the fundamental theories that make mega-constellations possible, using highly detailed mathematical approaches: from "Orbital Mechanics", the foundation of space communication, electromagnetic wave propagation, hardware propulsion systems, down to the debris problem that threatens the sustainability of the space environment.

# Chapter 1: The Limitations of Geostationary Earth Orbit (GEO) and the Paradigm Shift to Low Earth Orbit (LEO) Mega-Constellations

## 1.1 Physical Constraints of Geostationary Earth Orbit (GEO) Communications
For a long time, the Geostationary Earth Orbit (GEO), located approximately 35,786 km above the equator, played the leading role in communication systems utilizing outer space. Because the orbital period of a GEO satellite perfectly matches Earth's rotation period (sidereal day: approx. 23 hours, 56 minutes, 4 seconds), it appears stationary in the same direction from the ground at all times. This characteristic provided an immense advantage: ground antennas could remain fixed without requiring tracking mechanisms, and a single satellite could cover a vast region.

However, the laws of physics determined the limitations of GEO. The most prominent of these is **propagation delay (latency)**. Even with the speed of light $c \approx 3 \times 10^8$ m/s, considering the round trip from the ground to the GEO satellite (uplink and downlink) and the response from the other end (round trip), the distance the radio waves travel is approximately $35,786 \times 4 \approx 143,144$ km.
Dividing this by the speed of light, the theoretical minimum delay time is:
$$ t_{delay} = \frac{4 \times 35,786,000}{3 \times 10^8} \approx 0.477 \text{ s} = 477 \text{ ms} $$
Factoring in processing delays in actual communication protocols, calculation time for Forward Error Correction (FEC), and routing delays in the ground network, the round-trip delay time easily reaches 600ms to 800ms. This is a fatal latency for modern online gaming, High-Frequency Trading (HFT), telemedicine, or smooth video conferencing, which demand real-time performance. Coupled with the limitations of the window size in the TCP/IP protocol (BDP: Bandwidth-Delay Product), GEO suffered from a problem where throughput drastically declined even with broad bandwidth.

## 1.2 The Paradigm Shift to Low Earth Orbit (LEO)
To fundamentally resolve this latency issue, the mega-constellation concept emerged, utilizing Low Earth Orbit (LEO) at altitudes of 500 km to 1,200 km. In an LEO communication network represented by Starlink, assuming an altitude of 550 km, the round-trip delay due to the speed of light decreases dramatically.
$$ t_{LEO\_delay} = \frac{4 \times 550,000}{3 \times 10^8} \approx 0.0073 \text{ s} = 7.3 \text{ ms} $$
Even including routing delays in the ground network, an ultra-low latency internet of 20-30ms becomes possible, rivaling—or in the case of long-distance communications, surpassing—terrestrial optical fiber networks. The refractive index of light in glass fibers is about 1.5, reducing the speed of light to about 2/3 (approx. $2 \times 10^8$ m/s). On the other hand, the speed of light is maintained in the vacuum of space, so over distances of thousands of kilometers like intercontinental communication, data physically arrives faster when routed through LEO.

## 1.3 Friis Transmission Equation and Link Budget Analysis
LEO's advantage is not limited to latency. It also holds an overwhelming superiority in radio wave propagation loss. According to the Friis transmission equation, which forms the core of link budget (circuit design), the received power $P_r$ is expressed as follows:
$$ P_r = P_t G_t G_r \left( \frac{\lambda}{4 \pi d} \right)^2 \frac{1}{L_a L_s} $$
Here, $L_a$ is atmospheric attenuation, and $L_s$ is system loss.
The Free Space Path Loss (FSPL) is defined by the following equation:
$$ L_{FSPL} = \left( \frac{4 \pi d}{\lambda} \right)^2 $$
In decibel (dB) notation:
$$ L_{FSPL}(dB) = 20 \log_{10}(d) + 20 \log_{10}(f) + 20 \log_{10}\left(\frac{4 \pi}{c}\right) $$
Taking a Ku-band downlink frequency $f = 12$ GHz as an example.
Calculating the difference $\Delta L$ in propagation loss between GEO ($d \approx 36,000$ km) and LEO ($d \approx 550$ km):
$$ \Delta L = 20 \log_{10}\left(\frac{36000}{550}\right) \approx 20 \log_{10}(65.45) \approx 36.3 \text{ dB} $$
In other words, compared to GEO satellites, LEO satellites experience about 36.3 dB (approximately 4,200 times less in power ratio) less radio wave attenuation in the same frequency band. This allows the satellite's Equivalent Isotropically Radiated Power (EIRP) to be significantly suppressed while miniaturizing the user terminal's antenna aperture. This powerful link budget has made broadband communication possible with a home antenna only about 50cm in diameter.

# Chapter 2: The Mathematics of Orbital Mechanics and Perturbation Theory

To ensure that tens of thousands of satellites continue to seamlessly cover every point on Earth without colliding with one another, precise mathematical models are essential. Here, we follow in detail everything from the two-body problem to perturbation theory.

## 2.1 Kepler's Laws and the Two-Body Problem Equation
The foundation of orbital mechanics is derived from Newton's law of universal gravitation and the equations of motion in the two-body problem. Let $M$ be the mass of the Earth, $m$ be the mass of the satellite, and $\mathbf{r}$ be the position vector from the center of the Earth to the satellite. The equation of motion is described as follows:
$$ m \frac{d^2\mathbf{r}}{dt^2} = -G \frac{Mm}{r^3} \mathbf{r} $$
Using the Earth's standard gravitational parameter $\mu = GM \approx 3.986004418 \times 10^5 \text{ km}^3/\text{s}^2$, the equation simplifies to a form independent of mass $m$.
$$ \ddot{\mathbf{r}} + \frac{\mu}{r^3} \mathbf{r} = 0 $$
The solution trajectory for this non-linear differential equation is a conic section. The velocity $v$ of the satellite at any point on the orbit can be found using the "Vis-viva equation," derived from the law of conservation of energy.
$$ v^2 = \mu \left( \frac{2}{r} - \frac{1}{a} \right) $$
For a circular orbit at an altitude of 550 km ($a = 6371 + 550 = 6921$ km, $r=a$), the velocity is $v = \sqrt{\mu/a} \approx 7.59 \text{ km/s}$ (about 27,300 km/h). This immense speed creates the extreme frequency of Doppler shifts and handovers described later.

## 2.2 Keplerian Elements
To completely specify a satellite's orbit and position in three-dimensional space, six independent parameters are required.
1. **Semi-major axis ($a$)**: Determines the orbit's energy and period.
2. **Eccentricity ($e$)**: The shape of the orbit ($e=0$ for circular orbits). To maintain constant communication quality, LEO constellations adopt highly circular orbits with $e \approx 0.0001$.
3. **Inclination ($i$)**: The angle between the equatorial plane and the orbital plane. Starlink adopts angles such as 53 degrees, 70 degrees, and 97.6 degrees.
4. **Right Ascension of the Ascending Node ($\Omega$)**: The angle on the equatorial plane from the direction of the Vernal Equinox to the ascending node (the point where the satellite crosses the equator from south to north).
5. **Argument of Perigee ($\omega$)**: The angle on the orbital plane from the ascending node to the perigee.
6. **True Anomaly ($\nu$)**: The angle representing the current position of the satellite measured from the perigee.

## 2.3 Gravitational Potential $J_2$ Perturbation Due to Earth's Oblateness
The real Earth is not a perfect sphere; it is an Oblate Spheroid bulging by about 21 km at the equator due to centrifugal force from its rotation. This uneven mass distribution causes secular deviations (perturbations) from the ideal two-body problem. The Earth's gravitational potential $U$ is expressed by spherical harmonic expansion as follows:
$$ U = \frac{\mu}{r} \left[ 1 - \sum_{n=2}^{\infty} J_n \left(\frac{R_e}{r}\right)^n P_n(\sin \phi) \right] $$
Here, $R_e$ is the Earth's equatorial radius (6378.137 km), $P_n$ is the Legendre polynomial, and $\phi$ is the geocentric latitude. The most impactful factor is the 2nd-degree zonal harmonic coefficient $J_2 \approx 1.08263 \times 10^{-3}$, which represents the equatorial bulge.

The $J_2$ perturbation causes a secular perturbation that gradually rotates the entire orbital plane. Particularly important are the time rates of change of the Right Ascension of the Ascending Node $\Omega$ and the Argument of Perigee $\omega$.
$$ \dot{\Omega} = -\frac{3}{2} J_2 \left(\frac{R_e}{p}\right)^2 n \cos i $$
$$ \dot{\omega} = \frac{3}{4} J_2 \left(\frac{R_e}{p}\right)^2 n (5 \cos^2 i - 1) $$
Here, $p = a(1-e^2)$ is the semi-latus rectum, and $n = \sqrt{\mu/a^3}$ is the mean motion.

If the inclination $i$ is less than 90 degrees (prograde orbit), $\dot{\Omega}$ becomes negative, and the orbital plane rotates westward, contrary to the Earth's rotation (Nodal Regression). For an altitude of 550 km and an inclination of 53 degrees, $\dot{\Omega}$ is approximately $-5.2^\circ / \text{day}$. In mega-constellations, all satellites are precisely controlled to have the same altitude and inclination. As a result, the rate of change of $\dot{\Omega}$ due to the $J_2$ perturbation becomes identical across all planes, maintaining the relative shape of the constellation's mesh structure over a long period.

## 2.4 Design Principles of Sun-Synchronous Orbit (SSO)
The Sun-Synchronous Orbit (SSO) turns the $J_2$ perturbation to its advantage. The mean angular velocity of the Sun's apparent movement due to the Earth's revolution around the Sun is 360 degrees in one year, or about $0.9856^\circ/\text{day}$.
By properly selecting the orbital parameters so that $\dot{\Omega} = 0.9856^\circ/\text{day}$, the orbital plane will always maintain a constant angle relative to the Sun.
$$ 0.9856^\circ/\text{day} = -\frac{3}{2} J_2 \left(\frac{R_e}{a}\right)^2 n \cos i $$
To satisfy this, we must have $\cos i < 0$, meaning it must be a retrograde orbit with an inclination $i > 90^\circ$. For an altitude of 550 km, $i \approx 97.6^\circ$. Some of Starlink's shells adopt near-polar SSOs to cover the polar regions (around the North and South Poles).

# Chapter 3: Walker Constellation Geometry

The geometrical optimal solution for seamlessly covering the entire Earth with thousands of satellites is the "Walker Constellation."

## 3.1 Mathematical Definition of Walker-Delta Configuration $i: T/P/F$
The Walker-Delta pattern, devised by John G. Walker, is completely defined by the notation $i: T/P/F$.
- $i$: Inclination
- $T$: Total number of satellites composing the constellation
- $P$: Number of orbital Planes
- $F$: Phase difference parameter of satellites between adjacent orbital planes (an integer where $0 \le F \le P-1$)

Each orbital plane has $S = T/P$ satellites distributed evenly. The spacing between satellites within an orbital plane is $\Delta \nu = 360^\circ / S$.
The Right Ascension of the Ascending Node $\Omega$ is evenly divided along the equator, and the spacing between adjacent orbital planes is $\Delta \Omega = 360^\circ / P$.
Furthermore, the shift in true anomaly (phase difference) of the satellites in the adjacent eastward orbital plane is given by $\Delta \Phi = F \times (360^\circ / T)$.

For example, a typical shell (Shell 1) in Starlink's first generation adopts a massive Walker configuration of $T=1584, P=72$ at an altitude of 550 km and an inclination of 53 degrees ($S=22$ satellites per plane). By optimizing the phase difference $F$ between adjacent planes, it minimizes the collision risk between satellites at the highest latitudes (around 53 degrees North and South) where the orbits are most dense, while guaranteeing continuous coverage where at least one satellite is always visible at an elevation angle of 25 degrees or more when looking up from the ground.

## 3.2 Space Mesh Network via Inter-Satellite Links (ISL)
First-generation mega-constellations could only provide internet within ranges where a satellite could simultaneously communicate with both a ground user terminal and a gateway station (a bent-pipe connection). This meant services could not be provided in the middle of oceans or at the poles.

Breaking through this limitation is the Inter-Satellite Link (ISL) using laser communication. Because the vacuum of space has no atmospheric attenuation or scintillation (atmospheric fluctuations), high-capacity, low-latency communication of several Gbps to tens of Gbps using lasers in the 1.55 $\mu$m band (C-band) becomes possible.
Each satellite is equipped with four optical communication terminals, establishing laser links with two adjacent satellites ahead and behind in the same orbital plane (Intra-plane ISL) and two satellites in adjacent left and right orbital planes (Inter-plane ISL).

## 3.3 Shortest Path Dijkstra's Algorithm and Dynamic Topology Updates
In the network formed by ISL, the nodes (satellites) travel at about 7.5 km/s, causing the network topology to change rapidly on a second-by-second basis. Especially as they head towards the polar regions, orbital planes intersect, so laser links with satellites in adjacent planes (Inter-plane ISL) regularly disconnect and reconnect (handover).

For packet routing on this dynamic graph network, extensions of Dijkstra's Algorithm and Contact Graph Routing (CGR) are used. The edge cost $C_{ij}$ between node $i$ and node $j$ is evaluated as follows:
$$ C_{ij} = \alpha \cdot d_{ij} + \beta \cdot Q_{ij} + \gamma \cdot L_{ij} $$
Here, $d_{ij}$ is the physical distance (delay), $Q_{ij}$ is the queue length (congestion), and $L_{ij}$ is the remaining viable time of the link.
Data packets hop linearly through space at the speed of light. Compared to ground networks where optical fibers creep along Earth's curvature, the path lengths are shorter and there is no refractive index delay (which is $c/1.5$ in fiber). Therefore, for ultra-long-distance communication such as between New York and London, routing via ISL is theoretically faster.

# Chapter 4: Starlink Satellite Hardware and Propulsion Systems

The condition for a mega-constellation to be viable is the mass production of satellites and dramatic cost reductions.

## 4.1 Specific Impulse and Propellant Mass Calculation of Krypton/Argon Hall Thrusters
After being injected into orbit, satellites must ascend to their operational orbit under their own power, compensate for atmospheric drag during operation, and perform a deorbit at the end of their lifespan. To achieve the necessary velocity increment $\Delta V$ for these maneuvers, an electric propulsion system called a Hall-effect Thruster is employed.

According to Tsiolkovsky's rocket equation, the required propellant mass $m_p$ is:
$$ m_p = m_0 \left( 1 - e^{-\frac{\Delta V}{I_{sp} g_0}} \right) $$
Here, $I_{sp}$ is the specific impulse, $g_0$ is the standard gravitational acceleration, and $m_0$ is the initial mass.
Conventional electric propulsion used expensive Xenon, but SpaceX adopted Krypton for the first generation and Argon for the second generation (V2 Mini). Argon is abundantly present in the atmosphere and extremely cheap, but it has high ionization energy, which lowers thrust efficiency. However, by optimizing magnetic field topology, the Argon Hall thruster achieved an exhaust velocity corresponding to a specific impulse of 2500 seconds $\approx 24.5 \text{ km/s}$, revolutionizing propellant costs for mass launches.

## 4.2 Beamforming Mathematics of Phased Array Antennas
For communication with ground terminals, a Phased Array Antenna is used, which can instantaneously change the direction of the radio beam without any mechanical moving parts.
By arranging antenna elements in a grid pattern and controlling the phase of the radio waves transmitted from each element, a strong radio beam can be formed in a specific direction due to interference effects.

In a two-dimensional planar array, to direct the main beam to the target direction $(\theta, \phi)$, the phase shift amount $\Delta \Phi_{mn}$ for an element located at coordinates $(x_m, y_n)$ is calculated by the following equation:
$$ \Delta \Phi_{mn} = -\frac{2\pi}{\lambda} (x_m \sin\theta \cos\phi + y_n \sin\theta \sin\phi) $$
Starlink satellites and user terminals are equipped with advanced beamformer ICs, recalculating phase weight matrices thousands of times per second. This enables them to track satellites moving at high speeds overhead electronically and seamlessly.

## 4.3 Autonomous Collision Avoidance Algorithms
In LEO, where thousands of satellites fly around, the risk of colliding with debris or other satellites is omnipresent. Starlink satellites are equipped with their own autonomous collision avoidance system that links with orbital data (TLE) provided by the 18th Space Defense Squadron (18 SDS).
The probability of collision $P_c$ at the Time of Closest Approach (TCA) is calculated by projecting the covariance matrix of the position error of the two objects onto a two-dimensional plane and integrating it over the collision cross-sectional area:
$$ P_c = \frac{1}{2\pi |C_p|^{1/2}} \iint_{A} \exp\left( -\frac{1}{2} \mathbf{r}^T C_p^{-1} \mathbf{r} \right) dx dy $$
Here, $C_p$ is the projected covariance matrix, and $A$ is the collision cross-sectional area. If $P_c$ exceeds $10^{-5}$ (1 in 100,000), the satellite autonomously ignites its Hall thrusters to execute an avoidance maneuver. The fusion of AI and Model Predictive Control (MPC) ensures safety without human intervention.

# Chapter 5: The Space Debris Problem and the Terror of the Kessler Syndrome

## 5.1 Poisson Process Model of Collision Probability
Collisions between objects in orbit can be modeled probabilistically as a Poisson Process. If a satellite with cross-sectional area $A$ flies through a space with debris spatial density $\rho$ at a relative velocity $v_{rel}$, the expected value $d\lambda$ of collisions in time $dt$ is:
$$ d\lambda = \rho \cdot A \cdot v_{rel} \cdot dt $$
The probability $P_c$ of colliding at least once over a certain period $T$ is:
$$ P_c = 1 - e^{-\int_0^T \rho A v_{rel} dt} $$
In head-on collisions in low orbit, relative speeds reach about $10 \sim 15 \text{ km/s}$. The kinetic energy of even a 1 cm piece of aluminum is comparable to a hand grenade, capable of completely shattering a satellite.

## 5.2 Natural Decay Mechanism due to Atmospheric Drag
Even if the propulsion system fails and becomes uncontrollable, atmospheric drag from the upper atmosphere acts as a natural cleaner. The perturbing acceleration $\mathbf{a}_{drag}$ due to atmospheric drag is:
$$ \mathbf{a}_{drag} = -\frac{1}{2} \rho_{atm} \frac{C_D A}{m} v_{rel}^2 \frac{\mathbf{v}_{rel}}{v_{rel}} $$
The atmospheric density $\rho_{atm}$ increases exponentially as altitude drops, and rises further when the thermosphere expands due to extreme ultraviolet (EUV) radiation from solar activity. This is the main reason Starlink chose the 550 km altitude. Even in the worst case of becoming uncontrollable, it is a "self-cleaning orbit" where atmospheric drag naturally lowers the altitude within a few years (usually 1 to 5 years), burning it up upon re-entry. Above an altitude of 1000 km, objects would remain for hundreds of years.

## 5.3 Chain Destruction by In-Orbit Collisions: The Kessler Syndrome
The "Kessler Syndrome," proposed by NASA's Donald Kessler in 1978, is the worst-case scenario.
When large objects collide, they generate a cloud of thousands of debris pieces, which rapidly increases the probability of them hitting other satellites. Collisions occur in a chain reaction, and fragments multiply exponentially.
Once a critical density is surpassed, self-multiplication becomes unstoppable without even conducting new launches, and specific orbital regions (for example, altitudes of 700 to 1,000 km) become unusable for hundreds or thousands of years. The strong sense of crisis to prevent this catastrophic chain reaction in advance is behind the FCC's mandate to deorbit within 5 years after the end of operations.

# Chapter 6: The Light Pollution Problem for Astronomy and the Sustainability of Space

## 6.1 Satellite Reflection Magnitude and its Impact on Optical Telescopes
Swarms of satellites just after launch (the Starlink Train) strongly reflect sunlight and cross the night sky.
Astronomical magnitude $m$ is defined by the following equation:
$$ m_1 - m_2 = -2.5 \log_{10} \left( \frac{F_1}{F_2} \right) $$
Early Starlink satellites reached apparent magnitudes of $+3$ to $+5$, saturating the CCD sensors of ultra-sensitive wide-field telescopes like the Vera C. Rubin Observatory and causing severe crosstalk. This fatally impacted Near-Earth Object (NEO) exploration and cosmological observations.

## 6.2 Light Mitigation Strategies: VisorSat and Dielectric Mirror Films
SpaceX and the astronomical community collaborated to take countermeasures.
1. **DarkSat**: The surface was painted black, but it absorbed solar heat, causing thermal design failures.
2. **VisorSat**: Created shadows using deployable sun visors, but interfered with laser communication equipment and increased atmospheric drag.
3. **Dielectric Mirror Film**: The second generation (V2 Mini) employs advanced thermal and optical controls combining black paint and a special Bragg reflection film (Dielectric Mirror Film) that specularly reflects light into space instead of to the ground. This is succeeding in darkening them to $+7$ magnitude or below, making them invisible to the naked eye.

## 6.3 The Future of Space Traffic Management (STM)
The low-Earth orbit mega-constellation woven by tens of thousands of artificial satellites is a revolution bringing broadband to all of humanity. At the same time, however, it serves as a touchstone for human morality against the harsh mathematics of orbital mechanics and the limits of the space environment known as the Kessler Syndrome.
Currently, spearheaded by the UN COPUOS, there is a rapid push to create a framework for Space Traffic Management (STM), equivalent to "Freedom of Navigation" or "COLREGs" in the ocean. Realizing space sustainability is our greatest responsibility to the next generation.

# Appendix: Communication Capacity Modeling of Mega-Constellations

To mathematically evaluate the System Capacity of the entire mega-constellation, a spatial multiplexing model extending the Shannon-Hartley theorem is required.
The channel capacity $C_{beam}$ in a single beam is expressed by the following equation:
$$ C_{beam} = B \log_2 \left( 1 + \text{SINR} \right) $$
Here, $B$ is the bandwidth (e.g., a channel width like 250 MHz in the Ku-band), and SINR is the Signal-to-Interference-plus-Noise Ratio.

SINR is expanded as follows:
$$ \text{SINR} = \frac{P_r}{N_0 B + \sum I_{intra} + \sum I_{inter}} $$
- $P_r$: Received power (calculated from the Friis transmission equation)
- $N_0$: Noise power density ($N_0 = k T_{sys}$, where $k$ is the Boltzmann constant and $T_{sys}$ is the system noise temperature)
- $\sum I_{intra}$: Intra-system interference from other beams or other satellites within the same system
- $\sum I_{inter}$: Inter-system interference from GEO satellites or other companies' constellations like OneWeb or Kuiper

The greatest feature of a mega-constellation lies in its high Spatial Frequency Reuse. The Earth is divided into hexagonal cells (coverage areas), and adjacent cells use different frequency channels or polarizations (Right-Hand Circular Polarization RHCP and Left-Hand Circular Polarization LHCP). This is called a frequency reuse pattern with a cluster size $K$.
If the number of spot beams that a single satellite can form simultaneously is $N_{beam}$, the throughput per satellite $C_{sat}$ is:
$$ C_{sat} = \sum_{i=1}^{N_{beam}} B_i \log_2 \left( 1 + \text{SINR}_i \right) $$

The total system capacity $C_{total}$ of the entire constellation, given the number of active satellites $N_{active}$, does not simply equal $C_{total} = N_{active} \times C_{sat}$. This is because about 70% of the satellites are flying over oceans or polar regions with low communication demand.
If the ratio of land to the Earth's surface area is $\eta_{land} \approx 0.29$, and its population coverage weighting factor is $\eta_{pop}$, the effective system capacity $C_{eff}$ is estimated as follows:
$$ C_{eff} = C_{total} \times \eta_{land} \times \eta_{pop} \times \eta_{utilization} $$
Here, $\eta_{utilization}$ is the network uptime and routing efficiency.
As is clear from these equations, to enhance the economic viability of a mega-constellation, how to monetize the "satellite capacity over the ocean," which would otherwise go to waste, by providing services to aircraft and ships over oceans, or through long-distance backhaul communication using ISL, becomes a critically important proposition in the business model.
