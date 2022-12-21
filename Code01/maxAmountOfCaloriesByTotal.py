#mostCalories = lambda tupleCalories : max([sum(i) for i in tupleCalories])

#MaxAmountOfCaloriesByTotal
totalCalories = lambda tupleCalories : [sum(i) for i in tupleCalories]
mostCalories = lambda tupleCalories : max(totalCalories(tupleCalories))
mostCaloriesIndex = lambda tupleCalories : totalCalories(tupleCalories).index(mostCalories(tupleCalories))