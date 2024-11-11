# pennylane-multi-qubit-operation-quantum-basic-circuit

## Overview

This project demonstrates a basic quantum circuit using [PennyLane](https://pennylane.ai/), an open-source library for differentiable quantum programming. The circuit performs rotation and entanglement operations on a three-qubit system, illustrating multi-qubit gate usage and probabilistic measurement on a quantum simulator.

## Project Structure

- **Quantum Circuit**: A simple circuit is created using single-qubit rotation gates (RX, RY, and RZ) and multi-qubit entangling gates (CNOT).
- **Device Setup**: The `default.qubit` simulator from PennyLane is used as the quantum device.
- **Probabilistic Output**: After the operations are applied, the circuit returns the probability of each possible basis state for the three qubits.

## Prerequisites

- Python 3.x
- PennyLane library (`pip install pennylane`)

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pennylane-multi-qubit-operation-quantum-basic-circuit.git
   cd pennylane-multi-qubit-operation-quantum-basic-circuit

2. **Run the Code: Execute the script using Python:**:
   ```bash
   python main.py


### Expected Output

The output of this script is a list of probabilities for each possible state of the three-qubit system, representing the likelihood of measuring each state after the operations are applied.

### Code Explanation

The main components of the code are:

- **Device Initialization**: Defines a quantum device with three qubits (wires).
- **Circuit Definition**: A quantum function that applies a series of rotation and entangling gates.
- **QNode Creation**: Combines the circuit and device to create a callable function.
- **Execution**: Runs the circuit and outputs the resulting probabilities of the qubits' final states.

### Quantum Gates Used

- **RX, RY, RZ**: Single-qubit rotation gates on the X, Y, and Z axes, respectively.
- **CNOT**: A two-qubit entangling gate, introducing quantum entanglement between pairs of qubits.

