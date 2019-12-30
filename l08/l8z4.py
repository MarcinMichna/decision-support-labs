import scipy.optimize as scipy
import numpy as np

Y = np.array([[-2, -1, 0],
    [-1, -2, 0],
    [-1, -1, -2],
    [0, -3, -1],
    [0, -2, -2],
    [0, -1, -4],
    [0, 0, -6]])

c = [12000, 24000, 27000]

b = np.array([0, -3, -1, -1, -4, -2, 0])

res = scipy.linprog(c, Y, b).x

np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)
print("y =", res)

resX = []
for i in range(len(Y)):
    tmp = -1 * Y[i][0] * res[0] + -1 * Y[i][1] * res[1] + -1 * Y[i][2] * res[2]
    tmp2 = -1 * b[i]
    #print(tmp, tmp2)

print("Produkty: \n", "11cm -- 0; 8cm -- 2; 5cm -- 2\n 11cm -- 0; 8cm -- 1; 5cm -- 4\n 11cm -- 0; 8cm -- 0; 5cm -- 6")