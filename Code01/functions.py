#convertToList(): Convert text file to list, Nesting a new list each " ".
def convertToList():
    
    newList = list()
    temp = list()
    for i in open('test01.txt','r').read().splitlines():
        if(i == ''):
            newList.append(temp)
            temp=list()
        else:
            temp.append(int(i))
    
    return newList


#mostCaloriesTotal : Sum each element from a nested list and then check the maximum calorie
## mostCaloriesTotal = lambda tupleCalories : max([sum(i) for i in tupleCalories]) ##


#totalCalories: Sum each element from a nested list.
totalCalories = lambda listCalories : [sum(i) for i in listCalories]


#mostCalories: Check the maximum calorie from a list.
mostCalories = lambda listCalories :max(listCalories)


#mostCaloriesIndex: Check the index from the maximum calorie from a list.
mostCaloriesIndex = lambda listCalories : totalCalories(listCalories).index(mostCalories(totalCalories(listCalories)))