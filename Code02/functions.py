#convertToList(): Convert text file to list, Nesting a new list each " ".
def convertToList():
    with open('Code02/test02.txt') as text:
        return [line.split() for line in text]

#changeFirstIndex(stringList): Convert the first index from each list to its equivalent from a dictionary variable.
def changeFirstIndex(stringList):
    dictFile = {'A' : 'X', 'B' : 'Y', 'C' : 'Z',}
    return [[dictFile.get(letter[0], letter[0]) for letter in sublist] for sublist in stringList]

#outcomeRound(stringList): Create a new nested list based from the game map and matches matrix data.
def outcomeRound(gameList):
    gameMap = {'X' : 0, 'Y' : 1, 'Z' : 2}
    wldMatrix = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

    for item, subList in enumerate(gameList):
        gameList[item][0] = wldMatrix[gameMap.get(subList[0])][gameMap.get(subList[1])]
        gameList[item][1] = gameMap.get(subList[1]) + 1

    return gameList

#totalScore(stringList): Sum the nested list, to return the total score.
totalScore = lambda integerList : sum([sum(item) for item in integerList])