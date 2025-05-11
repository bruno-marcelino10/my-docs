# Copie e cole seu notebook aqui DEPOIS de exportar para o formato .py
from numpy.testing import assert_almost_equal
from numpy.testing import assert_equal

from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize']  = (16, 10)
plt.rcParams['axes.labelsize']  = 20
plt.rcParams['axes.titlesize']  = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['lines.linewidth'] = 4
plt.ion()
plt.style.use('seaborn-colorblind')

def count_missing(df) -> int:
    res = df.isna().sum().sum()
    return res

def drop_missing(df):
    res = df.dropna()
    return res

def all_median(df):
    res = df.median()
    return res

def delay(df) -> tuple:
    res = df.dropna()
    res = res[["DepDelay", "ArrDelay"]].mean()
    return res

def high_delay(df):
    res = df.dropna().query('Cancelled == 0')
    res["TravelTime"] = (res["CRSArrTime"] + res["ArrDelay"]) - (res["CRSDepTime"] + res["DepDelay"])
    res = (res
           .groupby(["OriginAirportName", "DestAirportName"], as_index=False)
           .mean()[["OriginAirportName", "DestAirportName", "TravelTime"]]
           .sort_values(by="TravelTime", ascending=False))
    return res.loc[0, "OriginAirportName"], res.loc[0, "DestAirportName"]

def boxplot(df):
    res = df[["DepDelay", "DayOfWeek"]].boxplot(column='DepDelay', by='DayOfWeek', grid=False, showfliers=False)
    return res

def corrplot(df):
    res = (df[["ArrDelay", "DepDelay", "Cancelled"]]
    .query('Cancelled == 0')
    .dropna()
    .drop("Cancelled", axis=1)
    .plot(kind="scatter", x="DepDelay", y="ArrDelay", edgecolor='k', alpha=0.75))
    return res