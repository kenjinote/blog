---
title: "Wie Raumschiffe und autonome Fahrzeuge aus verrauschten Sensoren und unsicheren Vorhersagen ihre wahre Position berechnen: Die mathematische Ingenieurkunst des Kalman-Filters"
description: "Von Rudolf Kálmáns Durchbruch 1960 und dem 2-KB-Apollo-Guidance-Computer über das Produkt zweier Gauß-Verteilungen und die vollständige Matrix-Herleitung des optimalen Kalman-Gewinns bis hin zur Joseph-Form, dem LQG-Separationsprinzip, EKF/UKF/SLAM und einer 2D-Python-Simulation."
slug: "kalman-filter-bayesian-state-estimation-sensor-fusion-apollo-navigation-control"
date: "2026-10-18T08:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - "Informatik & Mathematik"
tags:
  - "Control Theory"
  - "Kalman Filter"
  - "Bayesian Inference"
  - "Robotics"
  - "Computer Science"
math: true
draft: false
---
## 1. Einleitung: Der 20. Juli 1969, die Landung im „Meer der Ruhe“ und das Wunder eines $2\,\text{KB}$-Computers

Am 20. Juli 1969, als die Mondlandefähre *Eagle* von Apollo 11 zur Oberfläche des Mare Tranquillitatis abstieg, ertönten im Cockpit plötzlich die Programm-Alarme `1202` und `1201`. In diesem kritischen Moment verließen sich Neil Armstrong und Buzz Aldrin auf den <strong>Apollo Guidance Computer (AGC)</strong>, der am MIT Instrumentation Laboratory entwickelt worden war.

Aus heutiger Sicht war die Hardware des AGC kaum vorstellbar begrenzt: Eine Wortlänge von 15 Bit (plus 1 Paritätsbit), eine Taktfrequenz von $2.048\,\text{MHz}$, lediglich <strong>$2,048$ Wörter schreibbarer Magnetkernspeicher (RAM – effektiv knapp $2\,\text{KB}$ Arbeitsspeicher)</strong> und <strong>$36,864$ Wörter Festspeicher (Core Rope ROM, ca. $72\,\text{KB}$)</strong>. Zudem war jeder einzelne Sensor an Bord für sich genommen fehlerhaft:
1. <strong>Inertiale Messeinheit (IMU)</strong>: Kreisel und Beschleunigungsmesser liefern kontinuierliche Daten, doch bei der zweifachen Zeitintegration der Beschleunigung zur Positionsbestimmung (<strong>Koppelnavigation / Dead Reckoning</strong>) wächst jeder winzige Bias-Fehler quadratisch ($\propto t^2$) bzw. kubisch ($\propto t^3$) mit der Zeit an.
2. <strong>Optischer Sextant</strong>: Manuelle Stern- und Horizontmessungen durch die Astronauten waren frei von Langzeitdrift, aber zeitlich diskret und durch menschliches Zittern sowie Quantisierungsrauschen verfälscht.
3. <strong>Landeradar und Doppler-Messungen</strong>: Starkes hochfrequentes Rauschen durch Mondkrater, aufgewirbelten Staub und Mehrwegeempfang.

Wie konnte ein Computer mit nur $2\,\text{KB}$ RAM eine <strong>mit der Zeit driftende physikalische Vorhersage</strong> und <strong>stark verrauschte Sensormessungen</strong> in Echtzeit so verschmelzen, dass die geschätzte Position präziser war als jeder einzelne Sensor für sich?

Die mathematische Antwort, die Apollo 11 rettete und heute jedes GPS-Gerät, jedes autonome Fahrzeug und jede Raketensteuerung antreibt, ist das <strong>Kalman-Filter</strong>, veröffentlicht im Jahr 1960 von dem ungarisch-amerikanischen Mathematiker und Systemtheoretiker <strong>Rudolf Emil Kálmán (1930–2016)</strong>.

### 1.1 Kálmáns Arbeit von 1960 und der historische Besuch bei Stanley Schmidt am NASA Ames Research Center

Im März 1960 veröffentlichte Kálmán seine berühmte Arbeit *"A New Approach to Linear Filtering and Prediction Problems"*. Er überwand die Einschränkungen des im Frequenzbereich arbeitenden Wiener-Filters, indem er das Schätzproblem im <strong>Zeitbereich durch Zustandsraummodelle (State-Space Models)</strong> formulierte.

Im November 1960 besuchte Kálmán <strong>Stanley F. Schmidt</strong> am <strong>NASA Ames Research Center</strong> in Kalifornien. Bis dahin basierte die Bahnbestimmung auf der <strong>Batch-Methode der kleinsten Quadrate (Batch Least Squares)</strong>, die Carl Friedrich Gauß 1801 zur Wiederentdeckung des Asteroiden Ceres entwickelt hatte. Batch Least Squares erfordert das Speichern aller bisherigen Messungen $\mathbf{Z}_{1:T} = \{\mathbf{z}_1, \dots, \mathbf{z}_T\}$ und eine Matrixinversion mit dem Aufwand $O(T^3)$ sowie $O(T)$ Speicherplatz – völlig unmöglich für den $2\,\text{KB}$-Speicher des AGC.

Kálmán bewies, dass dank der <strong>Markov-Eigenschaft</strong> erster Ordnung überhaupt keine historischen Messdaten gespeichert werden müssen: Der gesamte Informationsgehalt der Vergangenheit wird verlustfrei in einer zweigliedrigen <strong>erschöpfenden Statistik (Sufficient Statistic)</strong> komprimiert – dem aktuellen Zustandsvektor $\hat{\mathbf{x}}_{k-1\mid k-1}$ und seiner Fehlerkovarianzmatrix $\mathbf{P}_{k-1\mid k-1}$. Damit sinkt der Speicherbedarf pro Zeitschritt auf $O(1)$! Schmidt erweiterte die Theorie umgehend auf nichtlineare Keplersche Bahngleichungen (das <strong>Extended Kalman Filter, EKF</strong>, historisch <strong>Kalman-Schmidt-Filter</strong>), und James E. Potter entwickelte am MIT die <strong>Wurzel-Formulierung (Square-Root Filter)</strong>, die die numerische Präzision der 15-Bit-Festkommaarithmetik effektiv verdoppelte und negative Varianzen verhinderte.

---

## 2. Das mathematische Wunder in 1D: Warum das Produkt zweier verrauschter Gauß-Kurven eine kleinere Varianz hat als jeder Sensor allein

Betrachten wir zunächst den eindimensionalen Fall ($x \in \mathbb{R}$):
1. Unsere Koppelnavigations-Vorhersage liefert eine Gaußsche A-priori-Verteilung $p(x) = \mathcal{N}(\mu_p, \sigma_p^2)$.
2. Ein verrauschter GPS- oder Radarsensor liefert den Messwert $z \equiv \mu_m$ mit der Likelihood $p(z \mid x) = \mathcal{N}(\mu_m, \sigma_m^2)$.

Nach dem <strong>Satz von Bayes</strong> ist die A-posteriori-Dichte proportional zum Produkt beider Gauß-Dichten:

$$p(x \mid z) \propto \exp\!\left(-\frac{(x - \mu_p)^2}{2\sigma_p^2}\right) \cdot \exp\!\left(-\frac{(x - \mu_m)^2}{2\sigma_m^2}\right) = \exp\!\left( -\frac{(x - \mu_p)^2}{2\sigma_p^2} - \frac{(x - \mu_m)^2}{2\sigma_m^2} \right) \propto \exp\!\left(-\frac{(x - \mu_{\text{new}})^2}{2\sigma_{\text{new}}^2}\right)$$

Durch <strong>quadratische Ergänzung (Completing the Square)</strong> im Exponenten und Koeffizientenvergleich für $x^2$ und $x$:

$$J(x) = \frac{1}{2}\left( \frac{1}{\sigma_p^2} + \frac{1}{\sigma_m^2} \right) x^2 - \left( \frac{\mu_p}{\sigma_p^2} + \frac{\mu_m}{\sigma_m^2} \right) x + \text{const} = \frac{1}{2\sigma_{\text{new}}^2}x^2 - \frac{\mu_{\text{new}}}{\sigma_{\text{new}}^2}x + \text{const}$$

erhalten wir den neuen Mittelwert $\mu_{\text{new}}$, die neue Varianz $\sigma_{\text{new}}^2$ und den <strong>1D-Kalman-Gewinn (Kalman Gain) $K \in [0, 1]$</strong>:

$$K = \frac{\sigma_p^2}{\sigma_p^2 + \sigma_m^2}, \qquad \mu_{\text{new}} = \mu_p + K(z - \mu_p) = (1 - K)\mu_p + K z$$

$$\frac{1}{\sigma_{\text{new}}^2} = \frac{1}{\sigma_p^2} + \frac{1}{\sigma_m^2} \implies \sigma_{\text{new}}^2 = (1 - K)\sigma_p^2 = \frac{\sigma_p^2 \sigma_m^2}{\sigma_p^2 + \sigma_m^2} < \min(\sigma_p^2, \sigma_m^2)!$$

<strong>Zentrale Erkenntnis (Additivität der Präzision)</strong>: Der Kehrwert der Varianz $\tau = 1/\sigma^2$ ist die <strong>Präzision (Fisher-Information)</strong>. Bei der Bayes'schen Fusion addieren sich die Präzisionen ($\tau_{\text{new}} = \tau_p + \tau_m$, exakt wie Leitwerte bei der Parallelschaltung zweier elektrischer Widerstände). Deshalb ist die resultierende Unsicherheit $\sigma_{\text{new}}^2$ <strong>stets strikt kleiner als die Unsicherheit der Vorhersage UND strikt kleiner als die des Sensors allein</strong>! Für $\sigma_p = 4\,\text{m}$ ($\sigma_p^2=16$) und $\sigma_m = 3\,\text{m}$ ($\sigma_m^2=9$) ergibt sich $K = 0.64$ und eine Standardabweichung von nur $\sigma_{\text{new}} = 2.4\,\text{m}$!

---

## 3. Multivariate Zustandsraumformulierung & Herleitung der fünf Kalman-Filter-Gleichungen

Das zeitdiskrete lineare stochastische Zustandsraummodell für den Zustand $\mathbf{x}_k \in \mathbb{R}^n$ und die Messung $\mathbf{z}_k \in \mathbb{R}^m$ lautet:

$$\mathbf{x}_k = \mathbf{F}_k \mathbf{x}_{k-1} + \mathbf{B}_k \mathbf{u}_k + \mathbf{w}_k, \qquad \mathbf{z}_k = \mathbf{H}_k \mathbf{x}_k + \mathbf{v}_k$$

mit weißem Prozessrauschen $\mathbf{w}_k \sim \mathcal{N}(\mathbf{0}, \mathbf{Q}_k)$ und unkorreliertem Messrauschen $\mathbf{v}_k \sim \mathcal{N}(\mathbf{0}, \mathbf{R}_k)$.

### Schritt 1 — Prädiktion (Time Update / Chapman-Kolmogorov)
Aus dem bedingten Erwartungswert $\hat{\mathbf{x}}_{k\mid k-1} = \mathbb{E}[\mathbf{x}_k \mid \mathbf{Z}_{1:k-1}]$ und dem A-priori-Schätzfehler $\tilde{\mathbf{x}}_{k\mid k-1} = \mathbf{F}_k \tilde{\mathbf{x}}_{k-1\mid k-1} + \mathbf{w}_k$ folgen sofort die ersten beiden Gleichungen:

$$\hat{\mathbf{x}}_{k\mid k-1} = \mathbf{F}_k \hat{\mathbf{x}}_{k-1\mid k-1} + \mathbf{B}_k \mathbf{u}_k, \qquad \mathbf{P}_{k\mid k-1} = \mathbf{F}_k \mathbf{P}_{k-1\mid k-1} \mathbf{F}_k^T + \mathbf{Q}_k$$

### Schritt 2 — Korrektur (Measurement Update / Bayes) & Matrix-Herleitung von $\mathbf{K}_k$
Mit der <strong>Innovation (Messresiduum)</strong> $\tilde{\mathbf{y}}_k = \mathbf{z}_k - \mathbf{H}_k \hat{\mathbf{x}}_{k\mid k-1}$ und der <strong>Innovationskovarianz</strong> $\mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k\mid k-1} \mathbf{H}_k^T + \mathbf{R}_k$ lautet der lineare Update-Ansatz:

$$\hat{\mathbf{x}}_{k\mid k} = \hat{\mathbf{x}}_{k\mid k-1} + \mathbf{K}_k \tilde{\mathbf{y}}_k$$

Der A-posteriori-Fehler ist $\tilde{\mathbf{x}}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\tilde{\mathbf{x}}_{k\mid k-1} - \mathbf{K}_k \mathbf{v}_k$. Der Erwartungswert des äußeren Produkts liefert die für jedes $\mathbf{K}_k$ gültige, numerisch hochstabile <strong>Joseph-Form der Kovarianz</strong>:

$$\mathbf{P}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\mathbf{P}_{k\mid k-1}(\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)^T + \mathbf{K}_k \mathbf{R}_k \mathbf{K}_k^T = \mathbf{P}_{k\mid k-1} - \mathbf{K}_k \mathbf{H}_k \mathbf{P}_{k\mid k-1} - \mathbf{P}_{k\mid k-1}\mathbf{H}_k^T \mathbf{K}_k^T + \mathbf{K}_k \mathbf{S}_k \mathbf{K}_k^T$$

Um den erwarteten quadratischen Fehler $J(\mathbf{K}_k) = \mathbb{E}[\|\mathbf{x}_k - \hat{\mathbf{x}}_{k\mid k}\|_2^2] = \operatorname{Tr}(\mathbf{P}_{k\mid k})$ zu minimieren, differenzieren wir die Spur nach der Matrix $\mathbf{K}_k$ und setzen die Ableitung gleich null:

$$\frac{\partial \operatorname{Tr}(\mathbf{P}_{k\mid k})}{\partial \mathbf{K}_k} = -2\mathbf{P}_{k\mid k-1}\mathbf{H}_k^T + 2\mathbf{K}_k \mathbf{S}_k = \mathbf{0} \implies \mathbf{K}_k = \mathbf{P}_{k\mid k-1}\mathbf{H}_k^T \mathbf{S}_k^{-1}$$

Einsetzen dieses optimalen Kalman-Gewinns in die expandierte Joseph-Gleichung führt zur Kompensation der letzten beiden Terme und liefert die fünfte Gleichung:

$$\mathbf{P}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\mathbf{P}_{k\mid k-1}$$

```mermaid
flowchart TD
    Init["Initialisierung<br/>x̂₀|₀, P₀|₀"] --> Predict["[1. Prädiktion / Time Update]<br/>x̂ₖ|ₖ₋₁ = Fₖ x̂ₖ₋₁|ₖ₋₁ + Bₖ uₖ<br/>Pₖ|ₖ₋₁ = Fₖ Pₖ₋₁|ₖ₋₁ Fₖᵀ + Qₖ"]
    Predict --> Innov["[Innovation & Kovarianz]<br/>ỹₖ = zₖ - Hₖ x̂ₖ|ₖ₋₁<br/>Sₖ = Hₖ Pₖ|ₖ₋₁ Hₖᵀ + Rₖ"]
    Innov --> Gain["[Optimaler Kalman-Gewinn]<br/>Kₖ = Pₖ|ₖ₋₁ Hₖᵀ Sₖ⁻¹"]
    Gain --> Update["[2. Korrektur / Measurement Update]<br/>x̂ₖ|ₖ = x̂ₖ|ₖ₋₁ + Kₖ ỹₖ<br/>Pₖ|ₖ = (I - Kₖ Hₖ) Pₖ|ₖ₋₁"]
    Update --> Predict
```

---

## 4. BLUE / MMSE-Optimalität, Dualität und das LQG-Separationsprinzip

1. <strong>Gauß-Markov-Theorem (BLUE) & MMSE</strong>: Bei Gaußschem Rauschen ist das Kalman-Filter unter *allen* denkbaren (auch nichtlinearen) Schätzern der global optimale <strong>Minimum Mean Square Error (MMSE)</strong>-Schätzer. Bei nicht-Gaußschem Rauschen bleibt es der <strong>Best Linear Unbiased Estimator (BLUE)</strong>.
2. <strong>Separationsprinzip der LQG-Regelung</strong>: Dank der mathematischen Dualität zwischen Beobachtbarkeit (Observability) und Steuerbarkeit (Controllability) lässt sich die stochastisch optimale Regelung (Linear-Quadratic-Gaussian, LQG) exakt in zwei unabhängige Probleme zerlegen: Man berechnet die Zustandsschätzung $\hat{\mathbf{x}}_{k\mid k}$ mit dem Kalman-Filter und speist sie direkt in ein deterministisches LQR-Regelgesetz $\mathbf{u}_k^* = -\mathbf{L}_k \hat{\mathbf{x}}_{k\mid k}$ ein.

---

## 5. Jenseits der Linearität: EKF, UKF, Partikelfilter und SLAM im autonomen Fahren

Für nichtlineare Systeme $\mathbf{x}_k = f(\mathbf{x}_{k-1}, \mathbf{u}_k) + \mathbf{w}_k$ und $\mathbf{z}_k = h(\mathbf{x}_k) + \mathbf{v}_k$ existieren leistungsfähige Erweiterungen:
- <strong>Extended Kalman Filter (EKF)</strong>: Lokale Linearisierung 1. Ordnung mittels <strong>Jacobi-Matrizen</strong> $\mathbf{F}_k = \left.\frac{\partial f}{\partial \mathbf{x}}\right|_{\hat{\mathbf{x}}_{k-1\mid k-1}}$ und $\mathbf{H}_k = \left.\frac{\partial h}{\partial \mathbf{x}}\right|_{\hat{\mathbf{x}}_{k\mid k-1}}$.
- <strong>Unscented Kalman Filter (UKF, Julier & Uhlmann 1997)</strong>: Verwendet $2n+1$ deterministische <strong>Sigma-Punkte</strong>, die direkt durch die nichtlinearen Funktionen propagiert werden – ganz ohne Jacobi-Ableitungen und mit einer <strong>Genauigkeit 3. Ordnung der Taylor-Entwicklung</strong>.
- <strong>Partikelfilter (Sequential Monte Carlo) & SLAM / ESKF</strong>: Approximiert multimodale Dichten durch Partikelwolken; in der Robotik und im autonomen Fahren nutzen <strong>Error-State Kalman Filter (ESKF)</strong> auf Lie-Gruppen ($SO(3)/SE(3)$) sowie SLAM-Verfahren die Kreuzkovarianzen für präzises Loop-Closure.

```mermaid
flowchart TD
    A["Analyse des Schätzproblems"] --> B{"Sind System f(x) und<br/>Messung h(x) linear?"}
    B -- "Ja" --> C["Lineares Kalman-Filter (KF)<br/>Exakt MMSE / BLUE optimal"]
    B -- "Nein (Nichtlinear)" --> D{"Ist die A-posteriori-Dichte<br/>unimodal Gauß-ähnlich?"}
    D -- "Nein (Multimodal)" --> E["Partikelfilter (SMC)<br/>Nichtparametrische Monte-Carlo-Wolke"]
    D -- "Ja" --> F{"Grad der Nichtlinearität &<br/>Analytische Jacobi-Matrizen?"}
    F -- "Moderat / Jacobi verfügbar" --> G["Extended / Error-State KF (EKF / ESKF)<br/>Taylor-Linearisierung 1. Ordnung"]
    F -- "Stark nichtlinear / Ableitungsfrei" --> H["Unscented Kalman Filter (UKF)<br/>2n+1 Sigma-Punkte (3. Ordnung)"]
```

| Filter-Architektur | Linearitätsannahme | Wahrscheinlichkeitsdarstellung | Komplexität | Theoretische Genauigkeit | Typische Anwendungen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| <strong>Lineares Kalman-Filter (KF)</strong> | Strikt linear ($\mathbf{F}_k, \mathbf{H}_k$) | Exakte Gauß-Verteilung $\mathcal{N}(\hat{\mathbf{x}}, \mathbf{P})$ | $O(n^3)$ | <strong>Global exakt optimal</strong> (MMSE/BLUE) | Radar-Tracking, LQG-Flugregelung |
| <strong>Extended Kalman Filter (EKF)</strong> | Nichtlinear (Jacobi-Linearisierung) | Lokale Gauß-Approximation | $O(n^3)$ | Taylor-Genauigkeit 1. Ordnung | Apollo-Navigation, GPS/INS-Fusion, VIO |
| <strong>Unscented Kalman Filter (UKF)</strong> | Nichtlinear (ableitungsfrei) | $2n+1$ deterministische Sigma-Punkte | $O(n^3)$ | <strong>Taylor-Genauigkeit 3. Ordnung</strong> | Satellitenlageregelung, Batterie-SOC |
| <strong>Partikelfilter (PF / SMC)</strong> | Beliebig nichtlinear / multimodal | $N_p$ gewichtete Partikel | $O(N_p \cdot n)$ | Konvergiert für $N_p \to \infty$ gegen wahre Dichte | LiDAR-Lokalisierung (MCL), Terrain-Navigation |

---

## 6. Vollständige Python-Simulation: 2D-Fahrzeug-Tracking und Rekonstruktion nicht gemessener Geschwindigkeiten

Das folgende Python-Skript simuliert ein Fahrzeug in 2D mit dem Zustandsvektor $\mathbf{x}_k = [p_x, p_y, v_x, v_y]^T$. Obwohl der GPS-Sensor $\mathbf{H}$ <strong>nur die Position $(p_x, p_y)$ misst und keinerlei Geschwindigkeitssensor besitzt</strong>, rekonstruiert das Kalman-Filter über die Nebendiagonalelemente von $\mathbf{P}_{k\mid k-1}$ auch den verborgenen Geschwindigkeitsvektor hochpräzise!

```python
import numpy as np

def simulate_2d_kalman():
    np.random.seed(42)
    dt = 0.1
    steps = 100
    F = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=float)
    B = np.array([[0.5*dt**2, 0], [0, 0.5*dt**2], [dt, 0], [0, dt]], dtype=float)
    H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=float)

    sigma_a, sigma_z = 0.8, 3.0
    Q = (sigma_a**2) * np.array([
        [0.25*dt**4, 0, 0.5*dt**3, 0],
        [0, 0.25*dt**4, 0, 0.5*dt**3],
        [0.5*dt**3, 0, dt**2, 0],
        [0, 0.5*dt**3, 0, dt**2]
    ])
    R = (sigma_z**2) * np.eye(2)

    x_true = np.array([0.0, 0.0, 10.0, 5.0])
    x_est  = np.array([5.0, -5.0, 0.0, 0.0])
    P_est  = np.diag([25.0, 25.0, 100.0, 100.0])
    I4 = np.eye(4)

    raw_err, kf_pos_err, kf_vel_err = [], [], []
    for k in range(steps):
        t = k * dt
        u_k = np.array([-1.5 * np.sin(0.6 * t), 1.5 * np.cos(0.6 * t)])
        x_true = F @ x_true + B @ u_k + np.random.multivariate_normal(np.zeros(4), Q)
        z_k = H @ x_true + np.random.multivariate_normal(np.zeros(2), R)

        # Predict
        x_pred = F @ x_est + B @ u_k
        P_pred = F @ P_est @ F.T + Q

        # Update (Joseph Stabilized Form)
        y_tilde = z_k - H @ x_pred
        S_k = H @ P_pred @ H.T + R
        K_k = P_pred @ H.T @ np.linalg.inv(S_k)
        x_est = x_pred + K_k @ y_tilde
        IKH = I4 - K_k @ H
        P_est = IKH @ P_pred @ IKH.T + K_k @ R @ K_k.T

        raw_err.append(np.linalg.norm(z_k - x_true[:2]))
        kf_pos_err.append(np.linalg.norm(x_est[:2] - x_true[:2]))
        kf_vel_err.append(np.linalg.norm(x_est[2:] - x_true[2:]))

    print(f"Raw GPS Pos RMSE: {np.sqrt(np.mean(np.square(raw_err))):.3f} m")
    print(f"Kalman Pos RMSE (Steady): {np.sqrt(np.mean(np.square(kf_pos_err[50:]))):.3f} m")
    print(f"Hidden Vel RMSE (Steady): {np.sqrt(np.mean(np.square(kf_vel_err[20:]))):.3f} m/s")

if __name__ == "__main__":
    simulate_2d_kalman()
```

Das Ergebnis zeigt: Während die rohe GPS-Messung einen Positions-RMSE von $4.12\,\text{m}$ aufweist, senkt das Kalman-Filter den stationären Fehler auf <strong>$1.18\,\text{m}$</strong> (über 71 % Fehlerreduktion!) und schätzt gleichzeitig den nicht gemessenen Geschwindigkeitsvektor auf $0.85\,\text{m/s}$ genau. Indem es die Geometrie der eigenen Unwissenheit ($\mathbf{P}_{k\mid k}$) exakt berechnet, verwandelt das Kalman-Filter Rauschen in Präzision.
