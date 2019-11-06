M = [[20, -150, -250],
     [150, -80, -100],
     [250, 100, 40]]


#B choice
bChoices = []
for i in range(len(M)):
    bChoices.append(min(M[i]))
bChoice = max(bChoices)

#A choice
aChoices = []
for i in range(len(M)):
    tmp = []
    for j in range(len(M)):
        tmp.append(M[j][i])
    aChoices.append(max(tmp))
aChoice = min(aChoices)

#summary
if aChoice == bChoice:
    print("Równowaga Nasha przy wyborze strategii", aChoices.index(aChoice) + 1)
else:
    print("Nie ma równowagi Nasha")