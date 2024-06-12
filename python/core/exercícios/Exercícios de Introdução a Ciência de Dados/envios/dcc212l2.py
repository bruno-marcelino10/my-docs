# Copie e cole seu notebook aqui DEPOIS de exportar para o formato .py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from numpy.testing import assert_almost_equal
from numpy.testing import assert_equal
from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal

plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['lines.linewidth'] = 4
plt.ion()
plt.style.use('seaborn-colorblind')

def median_and_size(array):
    # Retorne uma tupla, abaixo temos um return de exemplo
    median = np.median(array)
    size = len(array)
    return median, size

def month_sales(df, month: str):
    res = df.loc[month]
    return res

def row_sales(df, row: int):
    return df.iloc[row]

def grafico_4(df):
    return df.plot(kind='bar')

def north_or_south():
    return "Norte"

def questao6(df):
    return df.describe()

def mortes_por_pump(df):
    res = df.groupby("NearestPumpID").sum()
    return res