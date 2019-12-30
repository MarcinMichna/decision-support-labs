import scipy.optimize as scipy
import numpy as np

Y = [[-0.5, -0.4],
     [-0.4, -0.2],
     [-0.4, 0],
     [-0.2, -0.5]]

b = [-10, -14, -8, -11]

c = [2000, 2800]

res = scipy.linprog(c, Y, b).x
print("y =", res)

resX = []
for i in range(len(Y)):
    tmp = -1 * Y[i][0] * res[0] + -1 * Y[i][1] * res[1]
    tmp2 = -1 * b[i]
    # print(tmp, tmp2)

A1 = np.array([[0.4, 0.2], [0.2, 0.5]])
b1 = np.array([2000, 2800])
r = np.linalg.solve(A1, b1)
print("x1 = 0")
print("x2 =", r[0])
print("x3 = 0")
print("x4 =", r[1])
