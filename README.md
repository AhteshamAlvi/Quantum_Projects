# Quantum Projects

A hands-on collection of quantum computing experiments and algorithm implementations built with **IBM Qiskit**. This repository explores fundamental quantum phenomena — from entanglement to Bell inequality violations — and serves as a growing library of quantum algorithm implementations that run on both simulators and real IBM Quantum hardware.

---

## Table of Contents

- [Quantum Projects](#quantum-projects)
  - [Table of Contents](#table-of-contents)
  - [Implemented Experiments](#implemented-experiments)
    - [Bell State Circuit](#bell-state-circuit)
    - [CHSH Inequality](#chsh-inequality)
  - [Planned Algorithms](#planned-algorithms)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Running the Notebooks](#running-the-notebooks)

---

## Implemented Experiments

### Bell State Circuit

**Notebook:** [`bell_state.ipynb`](bell_state.ipynb)

The Bell State is the simplest and most famous example of **quantum entanglement** — a phenomenon where two qubits become correlated in a way that has no classical analog.

**How it works:**

1. A **Hadamard gate** (H) is applied to qubit 0, placing it in an equal superposition of |0⟩ and |1⟩.
2. A **CNOT gate** (CX) entangles qubit 0 with qubit 1, creating the Bell state:

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

3. Both qubits are measured across 1024 shots using Qiskit's `StatevectorSampler`.

**Expected output:** A roughly 50/50 probability distribution between |00⟩ and |11⟩ — the two qubits are always found in the same state, demonstrating perfect correlation through entanglement. The results are visualized as a histogram.

---

### CHSH Inequality

**Notebook:** [`CSHS_inequality.ipynb`](CSHS_inequality.ipynb)

The **CHSH (Clauser-Horne-Shimony-Holt) inequality** is a Bell inequality that sets an upper bound on correlations achievable by any local hidden variable theory. Classical physics limits the CHSH witness value to **|S| <= 2**, while quantum mechanics allows violations up to **|S| <= 2sqrt(2) ~ 2.828** (Tsirelson's bound).

**How it works:**

1. **Parameterized circuit:** A Bell state is prepared (H + CNOT), then an RY rotation with parameter theta is applied to qubit 0, sweeping through 21 phase values from 0 to 2pi.
2. **Two CHSH observables** are defined using Pauli operator combinations:
   - CHSH1 = ZZ - ZX + XZ + XX
   - CHSH2 = ZZ + ZX - XZ + XX
3. **Hardware execution:** The circuit is transpiled and optimized (optimization level 3) for a real IBM Quantum backend (127+ qubit systems) using `EstimatorV2` from Qiskit Runtime.
4. **Visualization:** Results are plotted against theta, with shaded regions highlighting where quantum correlations exceed the classical bound of +/-2, demonstrating a genuine quantum advantage.

**Key result:** At certain rotation angles, the measured CHSH witness values exceed the classical limit of 2, providing experimental evidence that quantum entanglement produces correlations that cannot be explained by any local hidden variable theory.

---

## Planned Algorithms

The following notebooks are scaffolded and planned for future implementation:

| Algorithm | Notebook | Description |
|-----------|----------|-------------|
| **Deutsch-Jozsa** | [`deutsch-jozsa.ipynb`](deutsch-jozsa.ipynb) | Determines whether a function is constant or balanced using a single query — an exponential speedup over classical approaches. |
| **Bernstein-Vazirani** | [`bernstein–vazirani.ipynb`](bernstein–vazirani.ipynb) | Finds a hidden bit string encoded in a function with a single query, compared to n classical queries. |
| **Grover's Algorithm** | [`grovers.ipynb`](grovers.ipynb) | Searches an unsorted database of N items in O(sqrt(N)) time — a quadratic speedup over classical search. |
| **Quantum Fourier Transform** | [`QFT.ipynb`](QFT.ipynb) | The quantum analog of the discrete Fourier transform; a key subroutine in many quantum algorithms including Shor's. |
| **Shor's Algorithm** | [`shors.ipynb`](shors.ipynb) | Factors large integers in polynomial time using quantum period-finding, threatening classical RSA encryption. |
| **VQE** | [`VQE.ipynb`](VQE.ipynb) | Variational Quantum Eigensolver — a hybrid classical-quantum algorithm for finding the ground state energy of molecular systems. |
| **QAOA** | [`QAOA.ipynb`](QAOA.ipynb) | Quantum Approximate Optimization Algorithm — tackles combinatorial optimization problems using parameterized quantum circuits. |

---

## Tech Stack

| Category | Libraries |
|----------|-----------|
| **Quantum Computing** | Qiskit 2.x, Qiskit IBM Runtime, Qiskit Aer |
| **Scientific Computing** | NumPy, SciPy, SymPy |
| **Visualization** | Matplotlib |
| **Environment** | Python 3.12, Jupyter Lab, python-dotenv |

---

## Project Structure

```
Quantum_Projects/
├── README.md                    # This file
├── service.py                   # IBM Quantum authentication & setup
├── .env                         # API credentials (not tracked in git)
├── .gitignore                   # Ignores .env and .venv
├── bell_state.ipynb             # Bell State entanglement demo
├── CSHS_inequality.ipynb        # CHSH inequality violation on real hardware
├── deutsch-jozsa.ipynb          # Deutsch-Jozsa algorithm (planned)
├── bernstein–vazirani.ipynb     # Bernstein-Vazirani algorithm (planned)
├── grovers.ipynb                # Grover's search algorithm (planned)
├── QFT.ipynb                    # Quantum Fourier Transform (planned)
├── shors.ipynb                  # Shor's factoring algorithm (planned)
├── VQE.ipynb                    # Variational Quantum Eigensolver (planned)
└── QAOA.ipynb                   # Quantum Approximate Optimization (planned)
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- An [IBM Quantum](https://quantum.ibm.com/) account (free tier available)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AhteshamAlvi/Quantum_Projects.git
   cd Quantum_Projects
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   # .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install qiskit qiskit-ibm-runtime qiskit-aer numpy scipy sympy matplotlib jupyterlab python-dotenv
   ```

4. **Configure IBM Quantum credentials:**

   Create a `.env` file in the project root:

   ```
   QUANTUM_API_KEY=your_ibm_quantum_api_key
   CRN_INSTANCE=your_crn_instance
   ```

   Then run the authentication setup:

   ```bash
   python service.py
   ```

   This saves your credentials locally so notebooks can connect to IBM Quantum hardware.

---

## Running the Notebooks

```bash
jupyter lab
```

Open any `.ipynb` file and run the cells. The Bell State notebook runs entirely on a local simulator, while the CHSH Inequality notebook connects to real IBM Quantum hardware (requires valid credentials).
