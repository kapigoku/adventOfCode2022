#convertToList(): Convert text file to list, nesting a new list for each " ".
def convertToList():
    with open('test01.txt') as temp:
        textList = temp.read().strip()
        return [[int(sublist) for sublist in list.split("\n")] for list in textList.split("\n\n")]


#mostCaloriesTotal : Sum each element from a nested list and then check the maximum calorie
mostCaloriesTotal = lambda tupleCalories : max([sum(i) for i in tupleCalories])