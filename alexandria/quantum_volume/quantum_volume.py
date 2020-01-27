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

MAX_INT = np.iinfo(np.int32).max-1

def quantum_volume_reference(dimension, seed=None):
    """Build a reference quantum volume circuit.

    Name of the circuits is ``QV{volume}_{seed}``,
    where volume is :math:`2^{dimension}`, and ``seed`` is the seed
    used in the random number generator.
    
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
        seed = np.random.randint(MAX_INT)
    rnd = np.random.RandomState(seed)  # pylint: disable=no-member

    qv_dim = 2**dimension
    circ_name = 'QV{}_{}'.format(qv_dim, seed)
    
    # build the circuit
    qc = QuantumCircuit(dimension, name=circ_name)
    for _ in range(dimension):
        # Generate uniformly random permutation Pj of [0...n-1]
        perm = rnd.permutation(dimension)
        # For each pair p in Pj, generate Haar random SU(4)
        for k in range(int(dimension/2)):
            U = random_unitary(4, seed=rnd.randint(MAX_INT))
            pair = int(perm[2*k]), int(perm[2*k+1])
            qc.append(U, [pair[0],pair[1]])
    return qc


def quantum_volume_generator(dimension, seed=None, samples=None):
    """A generator for quantum volume circuits.

    Name of the circuits is ``QV{volume}_{seed}+{offset}``,
    where volume is :math:`2^{dimension}`, ``seed`` is the seed
    used in the random number generator, and ``offset`` is the number
    of times the generator was called; the first call has ``offset=0``.
    
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
        seed = np.random.randint(MAX_INT)
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
            for k in range(int(dimension/2)):
                U = random_unitary(4, seed=rnd.randint(MAX_INT))
                pair = int(perm[2*k]), int(perm[2*k+1])
                qc.append(U, [pair[0],pair[1]])
        yield qc
        count += 1

class quantum_volume_gen():
    def __init__(self, dimension, seed=None):
        """A generator for quantum volume circuits.

        Parameters:
            dimension (int): Dimension of QV circuit.
            seed (int): Optional seed at which to start generator.
        """
        if seed is None:
            seed = np.random.randint(MAX_INT)
        self.rnd = np.random.RandomState(seed) # pylint: disable=no-member
        self.dimension = dimension
        qv_dim = 2**dimension
        self.circ_name = 'QV{}_{}'.format(qv_dim, seed)
        self.count = 0
        
    def __call__(self, samples=None):
        """
        Generate a collection or quantum circuits with names
         ``QV{volume}_{seed}+{offset}``, where volume is :math:`2^{dimension}`,
         ``seed`` is the seed used in the random number generator, and 
         ``offset`` is the number of times the generator was called; the first 
         call has ``offset=0``.

        Parameters:
            samples (int): Optional number of samples to generate.
                           Default is 1.

        Returns:
            list: A list of QuantumCircuits.
        """
        if samples is None:
            samples = 1
        out = []
        for _ in range(samples):
            qc_name = self.circ_name + '+{}'.format(self.count)
            qc = QuantumCircuit(self.dimension, name=qc_name)
            for _ in range(self.dimension):
                # Generate uniformly random permutation Pj of [0...n-1]
                perm = self.rnd.permutation(self.dimension)
                # For each pair p in Pj, generate Haar random SU(4)
                for k in range(int(self.dimension/2)):
                    U = random_unitary(4, seed=self.rnd.randint(MAX_INT))
                    pair = int(perm[2*k]), int(perm[2*k+1])
                    qc.append(U, [pair[0],pair[1]])
            out.append(qc)
            self.count += 1
        return out

    def __next__(self):
        return self.__call__()[0]