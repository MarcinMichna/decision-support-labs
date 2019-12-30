import scipy.optimize as scipy
import numpy as np

#### PLAYER A ####
shift = 2
A = [[0, -5],
     [-10, -1],
     [-4, -2]]

b = [-1, -1, -1]
c = [1, 1]


res = scipy.linprog(c, A, b).x
finalRes = res[0] + res[1]
V = (1/finalRes) - shift
Vtmp = 1 / finalRes

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print("#### PLAYER A ####")
print("\nDodatkowe dane:")
print("X result:", res)
print("x1 + x2 = 1/v = {0:5.2f}".format(finalRes))
print("\nWyniki: ")
print("Wartość gry: {0:5.2f}".format(V))

print("Strategia:")
print("A1: {0:3.2f}%".format(Vtmp * res[0] * 100))
print("A2: {0:3.2f}%".format(Vtmp * res[1] * 100))


#### PLAYER B ####
A = [[0, 10, 4],
     [5, 1, 2]]

b = [1, 1]
c = [-1, -1, -1]


res = scipy.linprog(c, A, b).x
finalRes = res[0] + res[1] + res[2]
V = (1/finalRes) - shift
Vtmp = 1 / finalRes
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print("\n\n#### PLAYER B ####")
print("Dodatkowe dane:")
print("X result:", res)
print("x1 + x2 + x3 = 1/v = {0:5.2f}".format(finalRes))
print("\nWyniki: ")
print("Wartość gry: {0:5.2f}".format(V))

print("Strategia:")
print("B1: {0:3.2f}%".format(Vtmp * res[0] * 100))
print("B2: {0:3.2f}%".format(Vtmp * res[1] * 100))
print("B3: {0:3.2f}%".format(Vtmp * res[2] * 100))
