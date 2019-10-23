import numpy as np


# funkcja normalizująca wektor
def normalization(v):
    s = sum(v)
    for elem in v:
        elem /= s
    return v

#hotel1
cena1 = 210
jedz1 = 20
d1 = 20 * 3   #minut pieszo * liczba przystankow * (1 jak bez przesiadek, elase 1.5)
p1 = 1             #tak - 2; nie - 1

#hotel2
cena2 = 150
jedz2 = 20
d2 = 30 * 7 * 1.5
p2 = 2

#hotel3
cena3 = 230
jedz3 = 30
d3 = 12 * 2
p3 = 1

#hotel4
cena4 = 250
jedz4 = 25
d4 = 8
p4 = 2

# zdefiniowanie macierzy porównań
C1 = np.matrix([[1, cena1/cena2, cena1/cena3, cena1/cena4],
                [cena2/cena1, 1, cena2/cena3, cena2/cena4],
                [cena3/cena1, cena3/cena2, 1, cena3/cena4],
                [cena4/cena1, cena4/cena2, cena4/cena3, 1]])

C2 = np.matrix([[1, jedz1/jedz2, jedz1/jedz3, jedz1/jedz4],
                [jedz2/jedz1, 1, jedz2/jedz3, jedz2/jedz4],
                [jedz3/jedz1, jedz3/jedz2, 1, jedz3/jedz4],
                [jedz4/jedz1, jedz4/jedz2, jedz4/jedz3, 1]])

C3 = np.matrix([[1, d1/d2, d1/d3, d1/d4],
                [d2/d1, 1, d2/d3, d2/d4],
                [d3/d1, d3/d2, 1, d3/d4],
                [d4/d1, d4/d2, d4/d3, 1]])

C4 = np.matrix([[1, p1/p2, p1/p3, p1/p4],
                [p2/p1, 1, p2/p3, p2/p4],
                [p3/p1, p3/p2, 1, p3/p4],
                [p4/p1, p4/p2, p4/p3, 1]])

Cp = np.matrix([[1, 5, 3, 4],
                [1/5, 1, 4, 1],
                [1/3, 1/4, 1, 2],
                [1/4, 1, 1/2, 1]])

#obliczanie wektorów własncyh i wartości własnych macierzy porównań
w1, v1 = np.linalg.eig(C1)
w2, v2 = np.linalg.eig(C2)
w3, v3 = np.linalg.eig(C3)
w4, v4 = np.linalg.eig(C4)
wp, vp = np.linalg.eig(Cp)

#wybieranie znormalizowanego wektora własnego(tego z największej wartości włąsnej)
n1 = normalization(v1[:, np.argmax(w1)])
n2 = normalization(v2[:, np.argmax(w2)])
n3 = normalization(v3[:, np.argmax(w3)])
n4 = normalization(v4[:, np.argmax(w4)])
npp = normalization(vp[:, np.argmax(wp)])

#utworzenie macierzy wektorów włąsnych
r = np.transpose(np.array([n1, n2, n3, n4]))

#wygenerowanie rankingu
ranking = np.matmul(r, npp)
print(ranking)
