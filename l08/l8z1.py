import scipy.optimize as scipy
import numpy as np

Y = [[-1, -4],
     [-3, -6],
     [-2, -5],
     [-3, -7],
     [-1, -1]]

c = [6, 15]

b = [-2, -5, -3, -1, -1]

res = scipy.linprog(c, Y, b).x
print(res)

resX = []
for i in range(len(Y)):
    tmp = -1 * Y[i][0] * res[0] + -1 * Y[i][1] * res[1]
    tmp2 = -1 * b[i]
    print(tmp, tmp2)

A1 = np.array([[1, 3], [4, 6]])
b1 = np.array([6, 15])
r = np.linalg.solve(A1, b1)
print("x1 =", r[0])
print("x2 =", r[1])
print("x3 = 0")
print("x4 = 0")
print("x5 = 0")
