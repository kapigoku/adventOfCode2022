"""convertToList(): Convert text file to a nested list of integers"""
def convertToList():
    with open('Code01/input.txt') as file:
        lineBlockLst = file.read().split('\n\n')
        return [[int(line) for line in lineBlock.split()] for lineBlock in lineBlockLst]

"""sumCalories(intNestedLst): Sum each element from a nested list"""
def sumCalories(intNestedLst):
    return [sum(intLst) for intLst in intNestedLst]

#--------------------------------------------Part One--------------------------------------------#
"""mostCaloriesTotal : Check the maximum calories"""
def mostCaloriesTotal(intLst):
    return max(intLst)

#--------------------------------------------Part Two--------------------------------------------#
"""threeMostCaloriesTotal: Check which are the three most calories in total and sum them"""
def threeMostCaloriesTotal(intLst):
    return sum(sorted(intLst, reverse=True)[:3])