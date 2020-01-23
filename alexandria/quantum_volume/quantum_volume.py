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
    if seed is None:
        seed = np.random.randint(np.iinfo(np.int32).max-1)
    rnd = np.random.RandomState(seed)  # pylint: disable=no-member

    qv_dim = 2**dimension
    circ_name = 'QV{}_{}'.format(qv_dim, seed)
    
    # build the circuit
    qc = QuantumCircuit(dimension, name=circ_name)
    for _ in range(dimension):
        # Generate uniformly random permutation Pj of [0...n-1]
        perm = rnd.permutation(dimension)
        # For each pair p in Pj, generate Haar random SU(4)
        for k in range(int(np.floor(dimension/2))):
            U = random_unitary(4)
            pair = int(perm[2*k]), int(perm[2*k+1])
            qc.append(U, [pair[0],pair[1]])
    return qc


def quantum_volume_generator(dimension, seed=None, samples=None):
    """A generator for quantum volume circuits.

    Name of the circuits is QV{volume}_{seed}+{offset},
    where volume is :math:`2^{dimension}`, `seed` is the seed
    used in the random number generator, and `offset` is the number
    of times the generator was called; the first call has `offset=0`.
    
    Parameters:
        dimension (int): Dimension of QV circuit.
        seed (int): Optional seed at which to start generator.
        samples (int): Optional number of samples to generate.
                       Default is infinite.
    
    Returns:
        QuantumCircuit
    """
    #setup RandomState
    if seed is None:
        seed = np.random.randint(np.iinfo(np.int32).max-1)
    rnd = np.random.RandomState(seed) # pylint: disable=no-member

    qv_dim = 2**dimension
    circ_name = 'QV{}_{}'.format(qv_dim, seed)
    
    count = 0
    while True:
        if samples and count >= samples:
            break
        # build the circuit
        _name = circ_name
        if count:
            _name = _name + '+{}'.format(count)
        qc = QuantumCircuit(dimension, name=_name)
        for _ in range(dimension):
            # Generate uniformly random permutation Pj of [0...n-1]
            perm = rnd.permutation(dimension)
            # For each pair p in Pj, generate Haar random SU(4)
            for k in range(int(np.floor(dimension/2))):
                U = random_unitary(4)
                pair = int(perm[2*k]), int(perm[2*k+1])
                qc.append(U, [pair[0],pair[1]])
        yield qc
        count += 1