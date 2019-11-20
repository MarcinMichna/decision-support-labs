import scipy.optimize as scipy
import numpy as np

A = [[-5, -15],
    [-20, -5],
    [15, 2],
    [-1, 0],
    [0, -1]]

b = [-50, -40, 60, 0, 0]
c = [8, 4]

res = scipy.linprog(c, A, b).x
finalRes = 8*res[0] + 4*res[1]
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print("X result:", res)
print("Final rsult: {0:5.2f}".format(finalRes))
