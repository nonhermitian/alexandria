# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Reference QV circuits and generators"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info.random import random_unitary

def quantum_volume_reference(dimension, seed=None):
    """Build a reference quantum volume circuit.
    
    Parameters:
        dimension (int): Dimension of QV circuit.
        seed (int): Optional seed at which to start generator.
    
    Returns:
        QuantumCircuit

    Reference Circuit:
        Canonical:
            .. jupyter-execute::

                from alexandria.quantum_volume import quantum_volume_reference
                from alexandria.visuals import circuit_widget

                qc = quantum_volume_reference(5, seed=123456)
                circuit_widget(qc)

        .. container:: toggle

            .. container:: header
        
                **IBM Quantum Basis Set Decomposition**
            
            .. jupyter-execute::
                :hide-code:

                qc.decompose().draw(output='mpl')

    """
    #setup RandomState
    rnd = np.random.RandomState(seed)  # pylint: disable=no-member
    
    # build the circuit
    qc = QuantumCircuit(dimension)
    for _ in range(dimension):
        # Generate uniformly random permutation Pj of [0...n-1]
        perm = rnd.permutation(dimension)
        # For each pair p in Pj, generate Haar random SU(4)
        for k in range(int(np.floor(dimension/2))):
            U = random_unitary(4)
            pair = int(perm[2*k]), int(perm[2*k+1])
            qc.append(U, [pair[0],pair[1]])
    return qc


def quantum_volume_generator(dimension, seed=None):
    """A generator for quantum volume circuits.
    
    Parameters:
        dimension (int): Dimension of QV circuit.
        seed (int): Optional seed at which to start generator.
    
    Yields:
        QuantumCircuit
    """
    #setup RandomState
    rnd = np.random.RandomState(seed)  # pylint: disable=no-member
    
    while True:
        # build the circuit
        qc = QuantumCircuit(dimension)
        for _ in range(dimension):
            # Generate uniformly random permutation Pj of [0...n-1]
            perm = rnd.permutation(dimension)
            # For each pair p in Pj, generate Haar random SU(4)
            for k in range(int(np.floor(dimension/2))):
                U = random_unitary(4)
                pair = int(perm[2*k]), int(perm[2*k+1])
                qc.append(U, [pair[0],pair[1]])
        yield qc