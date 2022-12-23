#convertToList(): Convert text file to list. Each line is a string.
def convertToList():
    return open('test03.txt', 'r').read().splitlines()


#splitCompartment(stringList): Create a nested list, where each string it will split in two parts.
def splitCompartment(stringList):

    splittedList = [[j for j in range(2)] for i in range(len(stringList))]

    for i in range(len(stringList)):
        for j in range(2):
            splittedList[i][0] = stringList[i][:len(stringList[i])//2]
            splittedList[i][1] = stringList[i][len(stringList[i])//2:]

    return splittedList


#repeatedChar(stringList): Check which character is repeated, then it will append to a new list.
def repeatedChar(splittedList):

    newList = []

    for i in range(len(splittedList)):
        count = list(set(splittedList[i][0])&set(splittedList[i][1]))
        for j in count:
            newList.append(j)
    return newList


#priorityItem(charList): Create two lists: one count the score of uppercase letters, and another 
#                        the lowercase letters. Then, the two are concatenated.
def priorityItem(charList):
    scoreListUpper = [ord(charList[i]) - 38 for i in range(len(charList)) if charList[i].isupper()]
    scoreListLower = [ord(charList[i]) - 96 for i in range(len(charList)) if charList[i].islower()]
    scoreList = scoreListUpper + scoreListLower
    return scoreList


#totalScore(scoreList): Return the total score.
totalScore = lambda scoreList : sum(i for i in scoreList)