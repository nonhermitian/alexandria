# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"Setup for Theia"

import os
import sys
import setuptools
import numpy as np
from Cython.Build import cythonize

REQUIREMENTS = [
    "qiskit>=0.14",
]

VERSION_PATH = os.path.abspath(
    os.path.join(os.path.join(os.path.dirname(__file__), 'alexandria', 'VERSION.txt')))
with open(VERSION_PATH, 'r') as fd:
    VERSION = fd.read().rstrip()


setuptools.setup(
    name='alexandria',
    version=VERSION,
    packages=setuptools.find_namespace_packages(exclude=['test*']),
    cmake_source_dir='.',
    description="Alexandria - The Quantum Library",
    url="",
    author="Alexandria Development Team",
    author_email="qiskit@us.ibm.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=REQUIREMENTS,
    keywords="qiskit",
    include_package_data=True,
    zip_safe=False
)
