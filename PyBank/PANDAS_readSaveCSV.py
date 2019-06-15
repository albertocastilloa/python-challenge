#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:33:23 2019

@author: albertocastillo
"""

import pandas as pd

df = pd.read_csv("budget_data.csv")

profit = pd.DataFrame([
        ["1", "Alberto", "alberto@me.com"]
        ],
        columns=["ID", "Nombre", "Email"])

meses = pd.DataFrame([
        ["Hola", "Adios"],
        ["Hi", "Bye"],
        ["Sayonara", "Sayonara"]
        ], columns=["Inicio", "Fin"])

print(profit)
print(meses)
profit.to_csv("justProfit.csv")