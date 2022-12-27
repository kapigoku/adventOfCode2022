#convertToList(): Convert text file to a nested list of two letters.
def convertToList():
    with open('Code02/input.txt') as file:
        return [line.split() for line in file]

print(convertToList())
#changeFirstIndex(strLst): Convert the first index from each list to its equivalent from a dictionary.
def changeFirstIndex(strLst):
    mapping = {'A' : 'X', 'B' : 'Y', 'C' : 'Z',}
    return [[mapping.get(string[0], string[0]) for string in strSubLst] for strSubLst in strLst]

#outcomeRound(pointLst): Create a nested list based from the game map and point matrix data.
def outcomeRound(pointLst):
    pointMap = {'X' : 0, 'Y' : 1, 'Z' : 2}
    pointMatrix = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

    for point, pointSubLst in enumerate(pointLst):
        pointSubLst[0] = pointMatrix[pointMap.get(pointSubLst[0])][pointMap.get(pointSubLst[1])]
        pointSubLst[1] = pointMap.get(pointSubLst[1]) + 1

    return pointLst

#totalScore(intLst): Sum the nested list to return the total score.
def totalScore(pointLst):
    return sum([sum(pointSubLst) for pointSubLst in pointLst])
