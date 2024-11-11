# Import the pennylane library, a framework for quantum machine learning and quantum computing.
import pennylane as qml

# Initialize a quantum device with three wires, or qubits, using the default qubit simulator.
# Wires represent the number of qubits in the device, which will hold quantum states for computation.
dev = qml.device("default.qubit", wires=3)


# Define a quantum circuit as a function. This circuit will take three parameters: theta, phi, and omega.
def my_circuit(theta, phi, omega):
    # Apply a rotation around the X-axis on qubit 0 by an angle of 'theta'.
    qml.RX(theta, wires=0)

    # Apply a rotation around the Y-axis on qubit 1 by an angle of 'phi'.
    qml.RY(phi, wires=1)

    # Apply a rotation around the Z-axis on qubit 2 by an angle of 'omega'.
    qml.RZ(omega, wires=2)

    # Add a series of CNOT gates to entangle the qubits.
    # The first CNOT gate uses qubit 0 as the control and qubit 1 as the target.
    qml.CNOT(wires=[0, 1])

    # The second CNOT gate uses qubit 1 as the control and qubit 2 as the target.
    qml.CNOT(wires=[1, 2])

    # The third CNOT gate uses qubit 2 as the control and qubit 0 as the target, creating a closed loop.
    qml.CNOT(wires=[2, 0])

    # Return the probability of measuring each possible state on the three qubits (wires).
    # This function will provide a list of probabilities corresponding to the basis states of the qubits.
    return qml.probs(wires=[0, 1, 2])


# Create a QNode to bind the quantum circuit to the device, making it callable like a function.
my_qnode = qml.QNode(my_circuit, dev)

# Set values for the parameters to be used in the circuit.
# These values are angles (in radians) for the rotations applied in the circuit.
theta, phi, omega = 0.1, 0.2, 0.3

# Execute the quantum node (QNode) by passing in the parameters and printing the resulting state probabilities.
print(my_qnode(theta, phi, omega))
