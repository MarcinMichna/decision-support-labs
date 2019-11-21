import scipy.optimize as scipy
import numpy as np

A = [[1, 1, 1],
    [-1, -1, -1],
    [-1, -2, -1],
    [0, 2, 1],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1]]

b = [30, -30, -10, 20, 0, 0, 0]
c = [-2, -1, -3]

res = scipy.linprog(c, A, b).x
finalRes = 2*res[0] + res[1] + 3*res[2]
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print("X result:", res)
print("Final result: {0:5.5f}".format(finalRes))

