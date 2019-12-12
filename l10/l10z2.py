import scipy.optimize as scipy
import numpy as np

A = [[2, 1, -9000],
     [1, 1, -5500],
     [1, 2.5, -10000],
     [-1, 0, 100],
     [0, -1, 100],
     [36.8, 65.7, 0],
     [-36.8, -65.7, 0]]

b = [0, 0, 0, 0, 0, 1, -1]
c = [-150, -130, 0]
res = scipy.linprog(c, A, b).x
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print("X result:", res)

x1 = res[0] / res[2]
print("Lakierki: {0:5.2f}".format(x1))

x2 = res[1] / res[2]
print("Sportowe: {0:5.2f}".format(x2))
