# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:20:52 2021

@author: s4680073
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from peeter_piper import piper

filename = "C:/Project/MBDA/post process/piper_diagram/piper_diagram.csv"
# filename = "C:/Project/MBDA/post process/piper_diagram/GW20130314-0057-s02_additional_field.csv"

df = pd.read_csv(filename)

# Plot example data
# Piper plot
fig = plt.figure()
markers = ["s", "o", "^", "v", ".", "X", "h", "p", "*", "D", ">","<"]
arrays = []
# for i, (label, group_df) in enumerate(df.groupby("additional-field")):
for i, (label, group_df) in enumerate(df.groupby("Site")):
    arr = group_df.iloc[:, 1:9].values
    arrays.append(
        [
            arr,
            {
                "label": label,
                "marker": markers[i],
                "edgecolor": "k",
                "linewidth": 0.3,
                "facecolor": "none",
            },
        ]
    )

rgb = piper(arrays, "Piper Diagram", use_color=False, fig=fig)
plt.legend(loc=[0.9,0.2])
# plt.tight_layout()
fig.savefig("piper_plot.png", dpi=300)
