import scipy.optimize as scipy
import numpy as np
import math
import time
import copy





#### WIEM co źle, nie chce mi się poprawiać, za dużo roboty #####





A = [[4, 3],
     [1, 1]]

b = [190, 55]
c = [-23, -17]
res = []
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
cont = True
x11 = []
x12 = []
b11 = []
b12 = []

x21 = []
x22 = []
b21 = []
b22 = []

while cont:
    print("\n\nfor")
    cont = False
    change1 = False
    change2 = False
    res = scipy.linprog(c, A, b).x
    print(A)
    print(b)
    print("X result:", res)
    if abs(res[0] - round(res[0])) > 0.00001:
        time.sleep(2.4)
        x11 = [-1, 0]
        x12 = [1, 0]
        b11 = -1 * (math.floor(res[0]) + 1)
        b12 = math.floor(res[0])
        change1 = True
    if abs(res[1] - round(res[1])) > 0.00001:
        x21 = [0, -1]
        x22 = [0, 1]
        b21 = -1 * (math.floor(res[1]) + 1)
        b22 = math.floor(res[1])
        change2 = True

    if change1 or change2:


        A1 = copy.deepcopy(A)
        A2 = copy.deepcopy(A)

        b1 = copy.deepcopy(b)
        b2 = copy.deepcopy(b)

        if change1 and not change2:
            A1.append(x11)
            A2.append(x12)

            b1.append(b11)
            b2.append(b12)
        if change2 and not change1:
            A1.append(x21)
            A2.append(x22)

            b1.append(b21)
            b2.append(b22)

        if change1 and change2:
            A1.append(x11)
            A2.append(x12)
            A1.append(x21)
            A2.append(x22)

            b1.append(b11)
            b2.append(b12)
            b1.append(b21)
            b2.append(b22)

        print("\na1", A1)
        print("a2", A2)
        print("b1", b1)
        print("b2", b2)

        res1 = scipy.linprog(c, A1, b1).x
        res2 = scipy.linprog(c, A2, b2).x
        finalRes1 = 23 * res1[0] + 17 * res1[1]
        finalRes2 = 23 * res2[0] + 17 * res2[1]

        print("res1", res1)
        print("res2", res2)
        print("final1", finalRes1)
        print("final2", finalRes2)
        if finalRes1 > finalRes2:
            A = A1
            b = b1
        else:
            A = A2
            b = b2


        print("\na", A)
        print("b", b)

        cont = True

finalRes = 23 * res[0] + 17 * res[1]
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print("X result:", res)
print("Final result: {0:5.5f}".format(finalRes))
