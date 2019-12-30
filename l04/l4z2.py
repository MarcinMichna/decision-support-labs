import numpy as np
import math

A = [[1, 2 / 3, 2, 5 / 2, 5 / 3, 5],
     [3 / 2, 1, 3, 10 / 3, 3, 9],
     [1 / 2, 1 / 3, 1, 4 / 3, 7 / 8, 5 / 2],
     [2 / 5, 3 / 10, 3 / 4, 1, 5 / 6, 12 / 5],
     [3 / 5, 1 / 3, 8 / 7, 6 / 5, 1, 3],
     [1 / 5, 1 / 9, 2 / 5, 5 / 12, 1 / 3, 1]]

B = [[1, 2 / 5, 3, 7 / 3, 1 / 2, 1],
     [5 / 2, 1, 4 / 7, 5 / 8, 1 / 3, 3],
     [1 / 3, 7 / 4, 1, 1 / 2, 2, 1 / 2],
     [3 / 7, 8 / 5, 2, 1, 4, 2],
     [2, 3, 1 / 2, 1 / 4, 1, 1 / 2],
     [1, 1 / 3, 2, 1 / 2, 2, 1]]

C = [[1, 17 / 4, 17 / 20, 8 / 5, 23 / 6, 8 / 3],
     [4 / 17, 1, 1 / 5, 2 / 5, 9 / 10, 2 / 3],
     [20 / 17, 5, 1, 21 / 10, 51 / 10, 10 / 3],
     [5 / 8, 5 / 2, 10 / 21, 1, 5 / 2, 11 / 6],
     [6 / 23, 10 / 9, 10 / 51, 2 / 5, 1, 19 / 30],
     [3 / 8, 3 / 2, 3 / 10, 6 / 11, 30 / 19, 1]]


def swapColumns(my_array, n1, n2):
    my_array = np.array(my_array)
    my_array[:, [n1, n2]] = my_array[:, [n2, n1]]
    return np.ndarray.tolist(my_array)


def swapRows(my_array, n1, n2):
    my_array[n1], my_array[n2] = my_array[n2], my_array[n1]
    return my_array


##### HRE ŚREDNIA GEOMETRYCZNA #####
def HREgeo(M, Wk, toSwap):
    n = len(M)
    k = len(Wk)

    # tworzenie wkeotra b
    b = []
    for i in range(n - k):
        X = 1
        for j in range(n):
            X *= M[i][j]
        for j in range(k):
            X *= Wk[j]
        b.append(math.log(X, 10))

    # tworzenie macierzy A

    A = []
    for i in range(n - k):
        A.append([])

    for i in range(n - k):
        for j in range(n - k):
            if i == j:
                A[i].append(n - 1)
            else:
                A[i].append(-1)

    # tworzenie macierzy W
    W = np.matmul(np.linalg.inv(A), b)
    for i in range(n - k):
        W[i] = pow(10, W[i])

    # połączenie w pełen ranking
    res = np.concatenate((W, Wk), axis=None)
    if len(toSwap) != 0:
        for i in range(len(toSwap)):
            res[toSwap[i][0]], res[toSwap[i][1]] = res[toSwap[i][1]], res[toSwap[i][0]]

    print("         Ranking końcowy: ", res)


print("\nHRE Średnia geometryczna:")
print("    Macierz A")
WkA = [3, 1]
HREgeo(A, WkA, [])
print("    Macierz B")
WkB = [2, 1 / 2, 1]
HREgeo(B, WkB, [])
print("    Macierz C")
WkC = [2, 5]
C = swapRows(C, 1, 4)
C = swapRows(C, 3, 5)
C = swapColumns(C, 1, 4)
C = swapColumns(C, 3, 5)
HREgeo(C, WkC, [[1, 4], [3, 5]])
