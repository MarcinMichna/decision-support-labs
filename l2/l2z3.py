import numpy as np


# funkcja normalizująca wektor
def normalization(v):
    s = sum(v)
    for elem in v:
        elem /= s
    return v


# zdefiniowanie macierzy porównań
#auto1
c1 = 68.2                     #cena samochodu
zp1 = 8.9                     #zużycie paliwa
cena1 = 1 / (c1 + 20 * zp1)   #kryterium cena = 1 / cena samochodu + 50 * zużycie paliwa

poj1 = 460 * 5          #kryterium pojemnosc = rozmiar bagaznika * ilosc pasażerów
bez1 = 4                #kryterium bezpieczenstwo

#auto2
c2 = 39.9
zp2 = 11.2
cena2 = 1 / (c2 + 20 * zp2)


poj2 = 415 * 5
bez2 = 3.5

#auto3
c3 = 87.394
zp3 = 5.81
cena3 = 1 / (c3 + 20 * zp3)

poj3 = 430 * 5
bez3 = 4.5

# zdefiniowanie macierzy porównań
C1 = np.matrix([[1, cena1/cena2, cena1/cena3],
                [cena2/cena1, 1, cena2/cena3],
                [cena3/cena1, cena3/cena2, 1]])

C2 = np.matrix([[1, bez1/bez2, bez1/bez3],
                [bez2/bez1, 1, bez2/bez3],
                [bez3/bez1, bez3/bez2, 1]])

C3 = np.matrix([[1, poj1/poj2, poj1/poj3],
                [poj2/poj1, 1, poj2/poj3],
                [poj3/poj1, poj3/poj2, 1]])

Cp = np.matrix([[1, 3, 7],
                [1/3, 1, 2],
                [1/7, 1/2, 1]])

#obliczanie wektorów własncyh i wartości własnych macierzy porównań
w1, v1 = np.linalg.eig(C1)
w2, v2 = np.linalg.eig(C2)
w3, v3 = np.linalg.eig(C3)
wp, vp = np.linalg.eig(Cp)

#wybieranie znormalizowanego wektora własnego(tego z największej wartości włąsnej)
n1 = normalization(v1[:, np.argmax(w1)])
n2 = normalization(v2[:, np.argmax(w2)])
n3 = normalization(v3[:, np.argmax(w3)])
npp = normalization(vp[:, np.argmax(wp)])

#utworzenie macierzy wektorów włąsnych
r = np.transpose(np.array([n1, n2, n3]))

#wygenerowanie rankingu
ranking = np.matmul(r, npp)
print(ranking)

