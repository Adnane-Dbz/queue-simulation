# Queue Simulation (M/M/1 & M/M/c)

This project provides a Python-based simulation of **queueing systems**, specifically the **M/M/1** (single server) and **M/M/c** (multiple servers) models. It allows you to study the behavior of queues under different arrival and service rates, and calculate key performance metrics.

---

## Features

- Simulate **M/M/1 queue** (single server)
- Simulate **M/M/c queue** (multiple servers)
- Generate random arrival and service times using **exponential distributions**
- Calculate performance measures:
  - Average waiting time in queue (**Wq**)
  - Average time in the system (**W**)
  - Server utilization (**ρ**)
- Fully flexible simulation parameters:
  - Arrival rate (λ)
  - Service rate (μ)
  - Number of servers (c)
  - Number of clients (N)

---

## Requirements

- Python 3.x
- Numpy

Install dependencies with:

```bash
pip install numpy
```
Usage

M/M/1 Simulation
```bash
python mm1_simulation.py
```
M/M/c Simulation
```bash
python mmc_simulation.py
```
Example Output
M/M/1
```bash
******** M/M/1 *******
temps moyen d'attente Wq = 0.65
temps moyen dans le systeme W = 1.0
saturation du serveur ρ = 0.66
Clients servis = 100 %
```
M/M/c
```bash
=== M/M/c ===
Temps moyen d'attente Wq = 0.2
Temps moyen dans le système W = 0.7
Saturation moyenne ρ = 0.67
Clients servis = 100 %
```
