#convertToList(): Convert text file to a nested list of integers.
def convertToList():
    with open('Code01/input.txt') as file:
        lineBlockLst = file.read().split('\n\n')
        return [[int(line) for line in lineBlock.split("\n")] for lineBlock in lineBlockLst]

#mostCaloriesTotal : Sum each element from a nested list and then check the maximum calories.
def mostCaloriesTotal(intLst):
    return max([sum(intSubLst) for intSubLst in intLst])