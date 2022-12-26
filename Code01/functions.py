#convertToList(): Convert text file to a nested list of integers.
def convertToList():
    with open('Code01/input.txt') as file:
        numStrBlock = file.read().split('\n\n')
        return [[int(num) for num in numStr.split("\n")] for numStr in numStrBlock]

#mostCaloriesTotal : Sum each element from a nested list and then check the maximum calories.
def mostCaloriesTotal(intLst):
    return max([sum(intNestedLst) for intNestedLst in intLst])