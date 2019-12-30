import numpy as np


# funkcja normalizująca wektor
def normalization(v):
    s = sum(v)
    for elem in v:
        elem /= s
    return v


# zdefiniowanie macierzy porównań
C1 = np.matrix([[1, 1 / 7, 1 / 5],
               [7, 1, 3],
               [5, 1 / 3, 1]])

C2 = np.matrix([[1, 5, 9],
               [1 / 5, 1, 4],
               [1 / 9, 1 / 4, 1]])

C3 = np.matrix([[1, 4, 1 / 5],
               [1 / 4, 1, 1 / 9],
               [5, 9, 1]])

C4 = np.matrix([[1, 9, 4],
               [1 / 9, 1, 1 / 4],
               [1 / 4, 4, 1]])

C5 = np.matrix([[1, 1, 1],
               [1, 1, 1],
               [1, 1, 1]])

C6 = np.matrix([[1, 6, 4],
               [1 / 6, 1, 1 / 3],
               [1 / 4, 3, 1]])

C7 = np.matrix([[1, 9, 6],
               [1 / 9, 1, 1 / 3],
               [1 / 6, 3, 1]])

C8 = np.matrix([[1, 1 / 2, 1 / 2],
               [2, 1, 1],
               [2, 1, 1]])

# ważność kategorii względem siebie
Cp = np.matrix([[1, 4, 7, 5, 8, 6, 6, 2],
               [1 / 4, 1, 5, 3, 7, 6, 6, 1 / 3],
               [1 / 7, 1 / 5, 1, 1 / 3, 5, 3, 3, 1 / 5],
               [1 / 5, 1 / 3, 3, 1, 6, 3, 4, 1 / 2],
               [1 / 8, 1 / 7, 1 / 5, 1 / 6, 1, 1 / 3, 1 / 4, 1 / 7],
               [1 / 6, 1 / 6, 1 / 3, 1 / 3, 3, 1, 1 / 2, 1 / 5],
               [1 / 6, 1 / 6, 1 / 3, 1 / 4, 4, 2, 1, 1 / 5],
               [1 / 2, 3, 5, 2, 7, 5, 5, 1]])

#obliczanie wektorów własncyh i wartości własnych macierzy porównań
w1, v1 = np.linalg.eig(C1)
w2, v2 = np.linalg.eig(C2)
w3, v3 = np.linalg.eig(C3)
w4, v4 = np.linalg.eig(C4)
w5, v5 = np.linalg.eig(C5)
w6, v6 = np.linalg.eig(C6)
w7, v7 = np.linalg.eig(C7)
w8, v8 = np.linalg.eig(C8)
wp, vp = np.linalg.eig(Cp)


#wybieranie znormalizowanego wektora własnego(tego z największej wartości włąsnej)
n1 = normalization(v1[:, np.argmax(w1)])
n2 = normalization(v2[:, np.argmax(w2)])
n3 = normalization(v3[:, np.argmax(w3)])
n4 = normalization(v4[:, np.argmax(w4)])
n5 = normalization(v5[:, np.argmax(w5)])
n6 = normalization(v6[:, np.argmax(w6)])
n7 = normalization(v7[:, np.argmax(w7)])
n8 = normalization(v8[:, np.argmax(w8)])
npp = normalization(vp[:, np.argmax(wp)])

#utworzenie macierzy wektorów włąsnych
r = np.transpose(np.array([n1, n2, n3, n4, n5, n6, n7, n8]))

#wygenerowanie rankingu
ranking = np.matmul(r, npp)
print(ranking)
