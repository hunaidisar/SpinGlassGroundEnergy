# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:49:06 2023

@author: Acer
"""
from qiskit import QuantumCircuit, QuantumRegister, Aer, transpile, assemble, execute
from qiskit.circuit import Parameter
import numpy as np
from numpy import pi
from qiskit.quantum_info import Statevector
from qiskit.providers.aer.noise import NoiseModel
from qiskit.circuit.library import  RealAmplitudes
from qiskit.visualization import plot_bloch_multivector, plot_state_qsphere

#%%

def prepare():
    theta = Parameter("θ")
    qc = QuantumCircuit(4)
    qc.rz(theta, 0)
    qc.ry(theta,1)
    #qc.draw("mpl")
    
    # bind the parameters after circuit to create a bound circuit
    # bc = qc.bind_parameters({theta: pi})
    theta_range = np.linspace(0, 2*pi , 20)
    bc = [qc.bind_parameters({theta: theta_val}) for theta_val in theta_range]
    backend = Aer.get_backend('statevector_simulator')
    job = backend.run(transpile(bc, backend))
    output1= job.result().get_counts()
    print(output1)

prepare()