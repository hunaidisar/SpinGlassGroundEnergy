# -*- coding: utf-8 -*-


# env reqs: qiskit nature
# https://qiskit.org/documentation/stubs/qiskit.algorithms.gradients.FiniteDiffEstimatorGradient.html#qiskit.algorithms.gradients.FiniteDiffEstimatorGradient
#https://qiskit.org/ecosystem/nature/stubs/qiskit_nature.second_q.hamiltonians.lattices.Lattice.from_adjacency_matrix.html
#https://qiskit.org/ecosystem/nature/stubs/qiskit_nature.second_q.hamiltonians.lattices.Lattice.to_adjacency_matrix.html
#-----------------------
import numpy as np
from qiskit_nature.second_q.hamiltonians.lattices import Lattice , BoundaryCondition, SquareLattice
from qiskit_nature.second_q.hamiltonians import IsingModel, LatticeModel
from qiskit.primitives import Estimator
from qiskit.algorithms.minimum_eigensolvers import VQE
from qiskit.algorithms.optimizers import COBYLA, L_BFGS_B, SLSQP
#from qiskit.circuit.library import TwoLocal
from qiskit.utils import algorithm_globals

# we also import the numpyminimumEigensolver to compare to classical resuts.
from qiskit.algorithms.minimum_eigensolvers import NumPyMinimumEigensolver

#%%

interaction = np.array([[-1, 1.0], [1.0, -1.0]])

# lattice = Lattice.from_adjacency_matrix(interaction)
# ising = IsingModel(lattice)
# #print (ising.lattice)

estimator = Estimator()

from math import pi
import numpy as np
import rustworkx as rx
from qiskit_nature.second_q.hamiltonians import FermiHubbardModel

#%%
rows = 5
cols = 5
boundary_condition = BoundaryCondition.OPEN
spin_glass = SquareLattice(rows=rows, cols=cols, boundary_condition=boundary_condition)
sg_ising = IsingModel(spin_glass)
print (type (sg_ising))
#--------
# Or, initializing an ising model from parameters:
    # Example
# interaction = np.array([[4.0, 2.0], [2.0, 4.0]])
# ising = IsingModel.from_parameters(interaction)
#-----------

print (spin_glass.draw())


