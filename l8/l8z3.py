import scipy.optimize as scipy
import numpy as np

Y = [[-4, 0],
     [-1, -1],
     [-8, 0],
     [-5, -1],
     [-2, -2],
     [0, -3]]

b = [-0.1, -0.2, -0.2, -0.3, -0.4, 0]

c = [12000, 18000]

res = scipy.linprog(c, Y, b).x

np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)
print("y =", res)

resX = []
for i in range(len(Y)):
    tmp = -1 * Y[i][0] * res[0] + -1 * Y[i][1] * res[1]
    tmp2 = -1 * b[i]
    print(tmp, tmp2)

A1 = np.array([[4, 8, 5], [0, 0, 1]])
b1 = np.array([12000, 18000])
r = np.linalg.solve(A1, b1)
print("x1 = ", r[0])
print("x2 = 0")
print("x3 =", r[1])
print("x4 =", r[2])
print("x5 = 0")
print("x6 = 0")