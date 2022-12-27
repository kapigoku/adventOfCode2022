from functions import *
testLst= [[1000,2000,3000], [4000,],[5000,6000], [7000,8000,9000], [10000,]]

#--------------------------------------------Part One--------------------------------------------#
print(f"Part One : {mostCaloriesTotal(sumCalories(convertToList()))}")

#--------------------------------------------Part Two--------------------------------------------#
print(f"Part Two : {threeMostCaloriesTotal(sumCalories(convertToList()))}")