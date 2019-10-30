# macierze do zadań
A = [[1, 2 / 3, 2, 5 / 2, 5 / 3, 5], [3 / 2, 1, 3, 10 / 3, 3, 9], [1 / 2, 1 / 3, 1, 4 / 3, 7 / 8, 5 / 2],
     [2 / 5, 3 / 10, 3 / 4, 1, 5 / 6, 12 / 5], [3 / 5, 1 / 3, 8 / 7, 6 / 5, 1, 3],
     [1 / 5, 1 / 9, 2 / 5, 5 / 12, 1 / 3, 1]]

B = [[1, 2 / 5, 3, 7 / 3, 1 / 2, 1, 2], [5 / 2, 1, 4 / 7, 1, 1, 3, 2 / 3], [1 / 3, 7 / 4, 1, 1 / 2, 2, 1 / 2, 1],
     [3 / 7, 1, 2, 1, 4, 2, 6], [2, 1, 1 / 2, 1 / 4, 1, 1 / 2, 3 / 4], [1, 1 / 3, 2, 1 / 2, 2, 1, 5 / 8],
     [1 / 2, 3 / 2, 1, 1 / 6, 4 / 3, 8 / 5, 1]]

C = [[1, 2 / 3, 2 / 15, 1, 8, 12 / 5, 1, 1 / 2], [3 / 2, 1, 1, 2, 1, 2 / 3, 1 / 6, 1],
     [15 / 2, 1, 1, 5 / 2, 7 / 8, 2, 1, 1 / 5], [1, 1 / 2, 2 / 5, 1, 4 / 3, 1, 2 / 7, 1],
     [1 / 8, 1, 8 / 7, 3 / 4, 1, 1 / 5, 2 / 7, 1], [5 / 12, 3 / 2, 1 / 2, 1, 5, 1, 3, 2],
     [1, 6, 1, 7 / 2, 7 / 2, 1 / 3, 1, 3 / 11], [2, 1, 5, 1, 1, 1 / 2, 11 / 3, 1]]

D = [[0, 1, 1, -1, -1, 1, -1], [-1, 0, 0, 1, 1, -1, 0], [-1, 0, 0, 0, 1, 1, -1], [1, -1, 0, 0, 1, 0, 1],
     [1, 0, -1, -1, 0, 1, -1], [-1, 1, -1, 1, -1, 0, 0], [1, 0, 1, -1, 1, 0, 0]]

E = [[0, 1, 0, 0, -1], [-1, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, -1, 0, 0], [1, -1, 0, 0, 0]]

F = [[0, -1, 1, -1, 1, -1, 1, -1, 1], [1, 0, 1, 1, 1, -1, -1, -1, -1], [-1, -1, 0, -1, 1, -1, 1, 1, 1],
     [1, -1, 1, 0, -1, 1, -1, 1, -1], [-1, -1, -1, 1, 0, -1, 1, 1, 1], [1, 1, 1, -1, 1, 0, -1, -1, -1],
     [-1, 1, -1, 1, -1, 1, 0, 1, -1], [1, 1, -1, -1, -1, 1, -1, 0, 1], [-1, 1, -1, 1, -1, 1, 1, -1, 0]]


# zadania


# zamiana na macierze turniejowe uogulnione
def makeTournamentTies(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if i != j:
                if M[i][j] > 1:
                    M[i][j] = 1
                elif M[i][j] < 1:
                    M[i][j] = -1
                else:
                    M[i][j] = 0
            else:
                M[i][j] = 0
    return M


def checkTournamentTies(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if i == j:
                if M[i][j] != 0:
                    return False
            else:
                if M[i][j] != -1 * M[j][i]:
                    return False
    return True


def checkTies(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if i != j:
                if M[i][j] == 0:
                    return True
    return False


def kendal(M):
    if len(M) % 2 == 1:
        I = (pow(len(M), 3) - len(M)) / 24
    else:
        I = (pow(len(M), 3) - 4 * len(M)) / 24

    count = 0
    # k > j > i --  gwarantuje, że trójki nie będą się powtarzać,
    #               ponieważ ich indeksy zawsze będą w kolejności rosnącej
    for i in range(len(M)):
        for j in range(i + 1, len(M)):
            for k in range(j + 1, len(M)):
                if i != j and j != k:
                    if M[i][j] == M[j][k] == M[k][i]:
                        count += 1
    return 1 - (count / I)


def extendedKendal(M):
    n = len(M)
    if n % 4 == 0:
        y = (13 * pow(n, 3) - 24 * n * n - 16 * n) / 96
    elif n % 4 == 1:
        y = (13 * pow(n, 3) - 24 * n * n - 19 * n + 30) / 96
    elif n % 4 == 2:
        y = (13 * pow(n, 3) - 24 * n * n - 4 * n) / 96
    else:
        y = (13 * pow(n, 3) - 24 * n * n - 19 * n + 18) / 96

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                # wszystkie takie same ale nie równe 0
                if M[i][j] == M[j][k] and M[j][k] == M[k][i] and M[k][i] != 0:
                    count += 1
                # 2 zera, 1 jedynka lub -1
                if M[i][j] == 1 or M[i][j] == -1:
                    if M[j][k] == 0 and M[k][i] == 0:
                        count += 1
                elif M[j][k] == 1 or M[j][k] == -1:
                    if M[i][j] == 0 and M[k][i] == 0:
                        count += 1
                elif M[k][i] == 1 or M[k][i] == -1:
                    if M[i][j] == 0 and M[j][k] == 0:
                        count += 1
                # 1 zero, 2 równe i różne od 0
                if M[i][j] == 0:
                    if M[j][k] == M[k][i] and M[k][i] != 0:
                        count += 1
                elif M[j][k] == 0:
                    if M[k][i] == M[i][j] and M[i][j] != 0:
                        count += 1
                elif M[k][i] == 0:
                    if M[i][j] == M[j][k] and M[i][j] != 0:
                        count += 1
    return 1 - (count / y)


# Macierze A, B i C zamień na macierze uogólnione turniejowe[2 pt.]
A = makeTournamentTies(A)
B = makeTournamentTies(B)
C = makeTournamentTies(C)

# które z macierzy D, E i F są uogólnione turniejowe[2pt.]
print("A - uogólniona Turniejowa: ", checkTournamentTies(A))
print("B - uogólniona Turniejowa: ", checkTournamentTies(B))
print("C - uogólniona Turniejowa: ", checkTournamentTies(C))
print("D - uogólniona Turniejowa: ", checkTournamentTies(D))
print("E - uogólniona Turniejowa: ", checkTournamentTies(E))
print("F - uogólniona Turniejowa: ", checkTournamentTies(F))

# czy dopuszcza remisy[2 pt.]
print("\nA - dopuszcza remisy: ", checkTies(A))
print("B - dopuszcza remisy: ", checkTies(B))
print("C - dopuszcza remisy: ", checkTies(C))
print("E - dopuszcza remisy: ", checkTies(E))
print("F - dopuszcza remisy: ", checkTies(F))

# jeżeli nie dopuszcza remisów, wylicz także klasyczny indeks Kendalla[2 pt.]
print("\nA - Kendal: ", kendal(A))
print("F - Kendal: ", kendal(F))

# uogólniony indeks Kendalla[2 pt.]
print("\nB - uogólniony Kendall: ", extendedKendal(B))
print("C - uogólniony Kendall: ", extendedKendal(C))
print("E - uogólniony Kendall: ", extendedKendal(E))
