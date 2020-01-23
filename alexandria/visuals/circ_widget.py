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

import ipywidgets as wid
from IPython.display import display
from .data_table import circuit_data_table

def circuit_widget(qc):
    circ_output = wid.Output(layout=wid.Layout(width='100%'))
    
    with circ_output:
        fig = qc.draw(output='mpl')
        display(fig)
        
    html = "<p>"
    for line in qc.qasm().split('\n'):
        html += line + '<br>'
    html += "</p>"

    qasm_output = wid.HTML(html, layout=wid.Layout(width='90%'))

    circ_data = circuit_data_table(qc)
    hrow = wid.HBox(children=[circ_data, qasm_output])

    out_wid = wid.VBox(children=[circ_output, hrow])
    return out_wid