from numpy.testing import assert_equal

import numpy as np

import dcc212l1


def test_inner():
    for _ in range(10):
        x1 = np.random.randint(1, 10, 5)
        x2 = np.random.randint(1, 10, 5)
        assert_equal(sum(x1 * x2), dcc212l1.inner(x1, x2))


def test_simple():
    for _ in range(10):
        X = np.random.randint(1, 10, 9).reshape(3, 3)
        Y = np.random.randint(1, 10, 6).reshape(3, 2)
        
        assert_equal((X @ Y).mean(), dcc212l1.medmult(X, Y))

print("Teste 1 Finalizado", test_inner())
print("Teste 2 Finalizado", test_simple())
