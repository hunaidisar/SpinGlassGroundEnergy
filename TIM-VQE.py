# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:49:06 2023
@author: Acer

"""
from qiskit import QuantumCircuit, Aer, transpile
from qiskit.circuit import Parameter
import numpy as np
from numpy import pi
#from qiskit.quantum_info import Statevector
#from qiskit.providers.aer.noise import NoiseModel
#from qiskit.circuit.library import  RealAmplitudes
#from qiskit.visualization import plot_bloch_multivector, plot_state_qsphere
from qiskit.opflow import Z, X, I
from qiskit.algorithms.optimizers import COBYLA
from qiskit.utils import QuantumInstance
from qiskit.algorithms import VQE
#%%

theta = Parameter("θ")
theta_range = np.linspace(0.01, 1.99*pi , 10)

# preparing an ansatz circuit

def prepare(param):
    
    qc = QuantumCircuit(4)
    qc.rz(theta, 0)
    qc.ry(theta,1)
    qc.rz(theta,0)
    qc.rx(-np.pi/2,0)
    qc.rz(theta,0)
    qc.rx(np.pi/2,0)
    qc.rz(-theta,0)
    #qc.draw("mpl")
    
    # bind the parameters after circuit to create a bound circuit
    bc = [qc.bind_parameters({theta: theta_val}) for theta_val in theta_range]
    backend = Aer.get_backend('statevector_simulator')
    job = backend.run(transpile(bc, backend))
    output1= job.result().get_counts()
    print(output1)


q = 2
h = 0.75

# getting the hamiltonian for the model
def Ising_Hamilton(q,h):
    Ising_Hamilton = 0
    for i in range(q):
        Zterm  = 1
        Xterm  = 1
        for j in range(q-1):
            if j == i:
                Zterm = Zterm^Z^Z
                Xterm  = Xterm^X^I
            elif i == (q-1) and j == (i-1):
                Xterm = Xterm^I^X
                Zterm = 0
            else:
                Zterm = Zterm^I
                Xterm = Xterm^I
        Ising_Hamilton = Ising_Hamilton + Zterm + h*Xterm
    return Ising_Hamilton



# Get Ising Hamilton operator
op = Ising_Hamilton(q,h)

backend = Aer.get_backend('statevector_simulator')
seed = 555     #set random seed
quantum_instance = QuantumInstance(backend=backend, seed_simulator=seed, seed_transpiler=seed)
optimizer = COBYLA(maxiter=1000)

# calling the ansatz
parameters = theta
State = prepare(parameters)

vqeqiskit = VQE(State,optimizer=optimizer,quantum_instance=quantum_instance)
result = vqeqiskit.compute_minimum_eigenvalue(op)
print(result)
