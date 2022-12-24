#convertToList(): Convert text file to list, nesting a new list for each blank line.
def convertToList():
    with open('Code01/test01.txt') as text:
        return [list(map(int, item.split("\n"))) for item in text.read().strip().split("\n\n")]

#mostCaloriesTotal : Sum each element from a nested list and then check the maximum calories.
mostCaloriesTotal = lambda integerList : max([sum(i) for i in integerList])