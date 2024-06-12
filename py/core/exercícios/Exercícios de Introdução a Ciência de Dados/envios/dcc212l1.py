# Copie e cole seu notebook aqui DEPOIS de exportar para o formato .py

import numpy as np
from numpy.testing import assert_almost_equal
from numpy.testing import assert_equal

from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal

def inner(array_1, array_2):
    res = array_1 * array_2
    res = res.sum()
    return res

x1 = np.array([2, 4, 8])
x2 = np.array([10, 100, 1000])
assert_equal(20 + 400 + 8000, inner(x1, x2))

def medmult(X_1, X_2):
    res = X_1 @ X_2
    res = res.mean()
    return res

X = np.array([1, 2, 3, 4]).reshape(2, 2)
Y = np.array([2, 1, 1, 2]).reshape(2, 2)
assert_equal(7.5, medmult(X, Y))