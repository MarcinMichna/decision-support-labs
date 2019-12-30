import numpy as np

A = [[1, 7, 3], [1 / 7, 1, 2], [1 / 3, 1 / 2, 1]]
B = [[1, 1 / 5, 7, 1], [5, 1, 1 / 2, 2], [1 / 7, 2, 1, 3], [1, 1 / 2, 1 / 3, 1]]
C = [[1, 2, 5, 1, 7], [1 / 2, 1, 3, 1 / 2, 5], [1 / 5, 1 / 3, 1, 1 / 5, 2], [1, 2, 5, 1, 7],
     [1 / 7, 1 / 5, 1 / 2, 1 / 7, 1]]


#saaty

eA = np.amax(np.linalg.eigvals(A))
nA = 3

eB = np.amax(np.linalg.eigvals(B))
nB = 4

eC = np.amax(np.linalg.eigvals(C))
nC = 5

saatyA = (eA - nA) / (nA - 1)
print(saatyA)

saatyB = (eB - nB)/(nB - 1)
print(saatyB)

saatyC = (eC - nC)/(nC - 1)
print(saatyC)

#indeks geometryczny

kA = 2 / ((nA-1)*(nA-2))
kB = 2 / ((nB-1)*(nB-2))
kC = 2 / ((nC-1)*(nC-2))


#indeks Koczkodaja

#A
maxv = 0
for i in range(len(A)):
    for j in range(len(A)):
        if i == j:
            continue
        for z in range(len(A)):
            if j == z:
                continue
            k = min(abs(1-(A[i][z]*A[z][j])/A[i][j]), abs(1-A[i][j]/(A[i][z]*A[z][j])))
            if k > maxv:
                maxv = k

print(maxv)

#B
maxv = 0
for i in range(len(B)):
    for j in range(len(B)):
        if i == j:
            continue
        for z in range(len(B)):
            if j == z:
                continue
            k = min(abs(1-(B[i][z]*B[z][j])/B[i][j]), abs(1-B[i][j]/(B[i][z]*B[z][j])))
            if k > maxv:
                maxv = k
print(maxv)

#C
maxv = 0
for i in range(len(C)):
    for j in range(len(C)):
        if i == j:
            continue
        for z in range(len(C)):
            if j == z:
                continue
            k = min(abs(1-(C[i][z]*C[z][j])/C[i][j]), abs(1-C[i][j]/(C[i][z]*C[z][j])))
            if k > maxv:
                maxv = k

print(maxv)