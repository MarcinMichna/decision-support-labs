import numpy as np


def normalization(v):
    s = sum(v)
    res = []
    for elem in v:
        res.append(elem / s)
    return res


C_1 = [[1, 1 / 7, 1 / 5], [7, 1, 3], [5, 1 / 3, 1]]
C_2 = [[1, 5, 9], [1 / 5, 1, 4], [1 / 9, 1 / 4, 1]]
C_3 = [[1, 4, 1 / 5], [1 / 4, 1, 1 / 9], [5, 9, 1]]
C_4 = [[1, 9, 4], [1 / 9, 1, 1 / 4], [1 / 4, 4, 1]]
C_5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
C_6 = [[1, 6, 4], [1 / 6, 1, 1 / 3], [1 / 4, 3, 1]]
C_7 = [[1, 9, 6], [1 / 9, 1, 1 / 3], [1 / 6, 3, 1]]
C_8 = [[1, 1 / 2, 1 / 2], [2, 1, 1], [2, 1, 1]]

C_parametry = [[1, 4, 7, 5, 8, 6, 6, 2],
               [1 / 4, 1, 5, 3, 7, 6, 6, 1 / 3],
               [1 / 7, 1 / 5, 1, 1 / 3, 5, 3, 3, 1 / 5],
               [1 / 5, 1 / 3, 3, 1, 6, 3, 4, 1 / 2], [1 / 8, 1 / 7, 1 / 5, 1 / 6, 1, 1 / 3, 1 / 4, 1 / 7],
               [1 / 6, 1 / 6, 1 / 3, 1 / 3, 3, 1, 1 / 2, 1 / 5], [1 / 6, 1 / 6, 1 / 3, 1 / 4, 4, 2, 1, 1 / 5],
               [1 / 2, 3, 5, 2, 7, 5, 5, 1]]

C1r = []
for i in range(len(C_1)):
    mul = np.prod(C_1[i])
    pierw = pow(mul, 1 / 3)
    C1r.append(pierw)
C1r = normalization(C1r)

C2r = []
for i in range(len(C_2)):
    mul = np.prod(C_2[i])
    pierw = pow(mul, 1 / 3)
    C2r.append(pierw)
C2r = normalization(C2r)

C3r = []
for i in range(len(C_3)):
    mul = np.prod(C_3[i])
    pierw = pow(mul, 1 / 3)
    C3r.append(pierw)
C3r = normalization(C3r)

C4r = []
for i in range(len(C_4)):
    mul = np.prod(C_4[i])
    pierw = pow(mul, 1 / 3)
    C4r.append(pierw)
C4r = normalization(C4r)

C5r = []
for i in range(len(C_5)):
    mul = np.prod(C_5[i])
    pierw = pow(mul, 1 / 3)
    C5r.append(pierw)
C5r = normalization(C5r)

C6r = []
for i in range(len(C_6)):
    mul = np.prod(C_6[i])
    pierw = pow(mul, 1 / 3)
    C6r.append(pierw)
C6r = normalization(C6r)

C7r = []
for i in range(len(C_7)):
    mul = np.prod(C_7[i])
    pierw = pow(mul, 1 / 3)
    C7r.append(pierw)
C7r = normalization(C7r)

C8r = []
for i in range(len(C_8)):
    mul = np.prod(C_8[i])
    pierw = pow(mul, 1 / 3)
    C8r.append(pierw)
C8r = normalization(C8r)

Cpr = []
for i in range(len(C_parametry)):
    mul = np.prod(C_parametry[i])
    pierw = pow(mul, 1 / 8)
    Cpr.append(pierw)
Cpr = normalization(Cpr)

r = np.transpose(np.array([C1r, C2r, C3r, C4r, C5r, C6r, C7r, C8r]))
ranking = np.matmul(r, Cpr)
print(ranking)
