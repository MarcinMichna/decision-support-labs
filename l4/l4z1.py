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


def koczkodaj(mtx):
    maxOfVal = 0
    for x in range(len(mtx)):
        for y in range(len(mtx)):
            if x == y:
                continue
            for z in range(len(mtx)):
                if y == z:
                    continue
                inKocz = min(abs(1 - (mtx[x][z] * mtx[z][y]) / mtx[x][y]), abs(1 - mtx[x][y] / (mtx[x][z] * mtx[z][y])))
                if inKocz > maxOfVal:
                    maxOfVal = inKocz

        return maxOfVal


def koczkodajVal(n, k):
    return 1 - ((1 + pow(4 * (n - 1) * (n - k - 2), 1 / 2)) / (2 * (n - 1)))


def swapColumns(my_array, n1, n2):
    my_array = np.array(my_array)
    my_array[:, [n1, n2]] = my_array[:, [n2, n1]]
    return np.ndarray.tolist(my_array)


def swapRows(my_array, n1, n2):
    my_array[n1], my_array[n2] = my_array[n2], my_array[n1]
    return my_array


##### HRE ŚREDNIA ARYTMETYCZNA #####
def HREavg(M, Wk):
    n = len(M)
    k = len(Wk)
    print("         Indeks Koczkodaja: ", koczkodaj(M))
    print("         Maksymalna wartość indeksu Koczkodaja: ", koczkodajVal(n, k))

    # tworzenie macierzy A
    A1 = []
    for i in range(n - k):
        A1.append([])

    for i in range(n - k):
        for j in range(n - k):
            A1[i].append(M[i][j])

    for i in range(n - k):
        for j in range(n - k):
            if i != j:
                A1[i][j] *= -1 / (n - 1)

    # tworzenie macierzy B
    B1 = []
    for i in range(n - k):
        B1.append([])

    for i in range(n - k):
        for j in range(n - k, n):
            B1[i].append(M[i][j])

    # tworzenie wektora b
    B1 = np.matmul(B1, Wk)
    b = B1 / (n - 1)

    # tworzenie rankingu
    W = np.matmul(np.linalg.inv(A1), b)
    res = np.concatenate((W, Wk), axis=None)
    print("         Ranking końcowy: ", res)





print("\nHRE Średnia arytmetyczna:")
print("    Macierz A")
WkA = [3, 1]
HREavg(A, WkA)

print("    Macierz B")
WkB = [2, 1 / 2, 1]
HREavg(B, WkB)

print("    Macierz C")
WkC = [2, 5]
C = swapRows(C, 1, 4)
C = swapRows(C, 3, 5)
C = swapColumns(C, 1, 4)
C = swapColumns(C, 3, 5)
HREavg(C, WkC)

