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

TABLE_STYLE = "style='border-radius: 5px;background: #7918f2;font-size: 14px;color: #fff;" + \
              "line-height: 1.5;" + \
              "background: -webkit-linear-gradient(-8deg, #B39DDB , #512DA8);" + \
              "background: -o-linear-gradient(-8deg, #B39DDB , #512DA8);" + \
              "background: -moz-linear-gradient(-8deg, #B39DDB , #512DA8);" + \
              "background: linear-gradient(-8deg, #B39DDB, #512DA8);" + \
              "min-height: 100vh; width: 100%"
TABLE_STYLE += "'"

TD_STYLE = "'padding: 0px 0px 5px 5px;'"


def circuit_data_table(qc):
    
    ops = qc.count_ops()
    
    num_cx = None
    if 'cx' in ops.keys():
        num_cx = ops['cx']  
    
    html = "<table {}>".format(TABLE_STYLE)
    html += "<tr><th style={}>{}</th><th></tr>".format(TD_STYLE, qc.name)

    html += "<tr><td style={}>Width</td><td>{}</td></tr>".format(TD_STYLE, qc.width())
    html += "<tr><td style={}>Depth</td><td>{}</td></tr>".format(TD_STYLE, qc.depth())
    html += "<tr><td style={}>Gate Count</td><td>{}</td></tr>".format(TD_STYLE, sum(ops.values()))
    html += "<tr><td style={}>CX Count</td><td>{}</td></tr>".format(TD_STYLE, num_cx)
    html += "</table>"
    
    out_wid = wid.HTML(html,layout=wid.Layout(width='45%'))
    return out_wid