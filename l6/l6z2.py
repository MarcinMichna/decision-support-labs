####################################################
#### tylko warunek stopu funkcji rekurencyjnej #####
####################################################


from copy import deepcopy
import math


def game(coinsStack, takenStacks1, takenStacks2, takenBefore, score, playerTurn):
    ###WARUNKI STOPU###
    # sprawdzam czy stosy nie są puste
    if sum(coinsStack) == 0:
        return score

    # sprawdzam czy gracz ma możliwość wziąć z któregkolwiek stosu
    if playerTurn == 1:
        if sum(takenStacks1) == 3 and takenBefore == 0:
            return score
        elif sum(takenStacks1) == 3:
            game(deepcopy(coinsStack), deepcopy(takenStacks1), deepcopy(takenStacks2), 0, deepcopy(score), 2)

    if playerTurn == 2:
        if sum(takenStacks2) == 3 and takenBefore == 0:
            return score
        elif sum(takenStacks2) == 3:
            game(deepcopy(coinsStack), deepcopy(takenStacks1), deepcopy(takenStacks2), 0, deepcopy(score), 1)

    ###OBLICZANIE TURY###
    if playerTurn == 1:
        # szukam najlepszej ścieżki
        maxScore = -math.inf

        #wyniki dla brania z 1 stosu
        # if takenStacks1[0] != 0:
        #     if takenBefore == 0 and coinsStack[0] > 0:
        #         tmpStack = deepcopy(coinsStack)
        #         tmpStack[0] -= 1
        #         tmpTaken1 = deepcopy(takenStacks1)
        #         tmpTaken1[0] = 1
        #         tmpScore = deepcopy(score) + 1
        #         tmpScore = game(deepcopy(tmpStack), deepcopy(tmpTaken1), deepcopy(takenStacks2), 0, deepcopy(tmpScore), 2)
        #         if tmpScore > maxScore:
        #             maxScore = tmpScore


game([2, 2, 2], [], [], 0, 0, 1)
