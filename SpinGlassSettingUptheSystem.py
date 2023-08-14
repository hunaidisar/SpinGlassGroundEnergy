# -*- coding: utf-8 -*-


# env reqs: qiskit nature
#
#-----------------------
import numpy as np
from qiskit_nature.second_q.hamiltonians.lattices import Lattice
from qiskit_nature.second_q.hamiltonians import IsingModel
from qiskit.primitives import Estimator
from qiskit.algorithms.minimum_eigensolvers import VQE
from qiskit.algorithms.optimizers import COBYLA, L_BFGS_B, SLSQP
#from qiskit.circuit.library import TwoLocal
from qiskit.utils import algorithm_globals

# we also import the numpyminimumEigensolver to compare to classical resuts.
from qiskit.algorithms.minimum_eigensolvers import NumPyMinimumEigensolver

#%%

interaction = np.array([[5.0, 4.0], [4.0, 5.0]])

lattice = Lattice.from_adjacency_matrix(interaction)
ising = IsingModel(lattice)
#print (ising.lattice)

estimator = Estimator()