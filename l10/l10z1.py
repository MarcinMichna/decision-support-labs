import scipy.optimize as scipy
import numpy as np

A = [[1, 2, -500],
     [1, 1, -350],
     [-2, -1, 600],
     [1, 2, 0],
     [-1, -2, 0]]

b = [0, 0, 0, 1, -1]
c = [-3, -4, 0]
res = scipy.linprog(c, A, b).x
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print("X result:", res)

x1 = res[0] / res[2]
print("A: {0:5.2f}".format(x1))

x2 = res[1] / res[2]
print("B: {0:5.2f}".format(x2))
