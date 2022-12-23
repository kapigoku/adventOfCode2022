#convertToList(): Convert text file to list. Each line is a string.
def convertToList():
    with open('test04.txt', 'r') as textList:
        return [eval(line.replace('-',',')) for line in textList]


#isFullOverlapTrue(integerList): Count each time an assignment is fully contained in another
def isFullOverlapTrue(integerList):
    count = 0

    for i in range(len(integerList)):
        startFirst = integerList[i][0] 
        finalFirst = integerList[i][1] 
        startLast = integerList[i][2] 
        finalLast = integerList[i][3] 

        if abs(startFirst - finalFirst) > abs(startLast - finalLast):
            if set(range(startLast,finalLast+1)).issubset(set(range(startFirst,finalFirst+1))): count += 1
        else:
            if set(range(startFirst,finalFirst+1)).issubset(set(range(startLast,finalLast+1))): count += 1

    return count


#isOverlapTrue(integerList): Count each time an nassignment is contained in another
def isOverlapTrue(integerList):
    count = 0

    for i in range(len(integerList)):

        startFirst = integerList[i][0] 
        finalFirst = integerList[i][1] 
        startLast = integerList[i][2] 
        finalLast = integerList[i][3] 

        if finalFirst >= startLast and finalLast >= startFirst: count += 1

    return count