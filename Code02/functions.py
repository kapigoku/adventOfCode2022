#convertToList(): Convert text file to list, Nesting a new list each " ".
def convertToList():
    return [i.split() for i in open('test02.txt', 'r').read().splitlines()]


#changeFirstIndex(stringList): Convert the first index from each list to its equivalent from a dictionary variable.
def changeFirstIndex(stringList):

    dictFile = {'A' : 'X', 'B' : 'Y', 'C' : 'Z',}

    for i in range(len(stringList)):
        stringList[i][0] = dictFile.get(stringList[i][0])

    return stringList


#outcomeRound(stringList): Create a new nested list based from the game map and matches matrix data.
def outcomeRound(stringList):

    gameMap = {'X' : 0, 'Y' : 1, 'Z' : 2}
    wldMatrix = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]
    newList = [[j for j in range(2)] for i in range(len(stringList))]

    for i in range(len(stringList)):
        for j in range(2):
            newList[i][0] = wldMatrix[gameMap.get(stringList[i][0])][gameMap.get(stringList[i][1])]
            newList[i][1] = gameMap.get(stringList[i][1]) + 1

    return newList


#totalScore(stringList): Sum the nested list, to return the total score.
totalScore = lambda integerList : sum([sum(i) for i in integerList])