import scipy.optimize as scipy
import numpy as np

#### PLAYER A ####
shift = 4
A = [[-4, -2, -7, -4],
     [-6, -4, -7, -1],
     [-1, -1, -4, -8],
     [-4, -7, 0, -4]]

b = [-1, -1, -1, -1]

c = [1, 1, 1, 1]

res = scipy.linprog(c, A, b).x
finalRes = res[0] + res[1] + res[2] + res[3]
V = (1 / finalRes) - shift
Vtmp = 1 / finalRes
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print("\n\n#### PLAYER A ####")
print("Dodatkowe dane:")
print("X result:", res)
print("x1 + x2 + x3 + x4 = 1/v = {0:5.2f}".format(finalRes))
print("\nWyniki: ")
print("Wartość gry: {0:5.2f}".format(V))

print("Strategia A(moje palce, suma palców):")
print("A1,2: {0:3.2f}%".format(Vtmp * res[0] * 100))
print("A1,3: {0:3.2f}%".format(Vtmp * res[1] * 100))
print("A2,3: {0:3.2f}%".format(Vtmp * res[2] * 100))
print("A2,4: {0:3.2f}%".format(Vtmp * res[3] * 100))

#### PLAYER B ####

A = [[4, 6, 1, 4],
     [2, 4, 1, 7],
     [7, 7, 4, 0],
     [4, 1, 8, 4]]

b = [1, 1, 1, 1]

c = [-1, -1, -1, -1]

res = scipy.linprog(c, A, b).x
finalRes = res[0] + res[1] + res[2] + res[3]
V = (1 / finalRes) - shift
Vtmp = 1 / finalRes

print("#### PLAYER B ####")
print("\nDodatkowe dane:")
print("X result:", res)
print("x1 + x2 + x3 + x4 = 1/v = {0:5.2f}".format(finalRes))
print("\nWyniki: ")
print("Wartość gry: {0:5.2f}".format(V))

print("Strategia B(moje palce, suma palców):")
print("B1,2: {0:3.2f}%".format(Vtmp * res[0] * 100))
print("B1,3: {0:3.2f}%".format(Vtmp * res[1] * 100))
print("B2,3: {0:3.2f}%".format(Vtmp * res[2] * 100))
print("B2,4: {0:3.2f}%".format(Vtmp * res[3] * 100))
