#convertToList(): Convert text file to list, nesting a new list for each blank line.
def convertToList():
    with open('Code01/test01.txt') as temp:
        return [list(map(int, item.split("\n"))) for item in temp.read().strip().split("\n\n")]

#mostCaloriesTotal : Sum each element from a nested list and then check the maximum calories.
mostCaloriesTotal = lambda tupleCalories : max([sum(i) for i in tupleCalories])