from functions import *

#Test
testList = ['vJrwpWtwJgWrhcsFMMfFFhFp','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']
print(f"Total Score by Splitted Line : {totalScore(priorityItem(repeatedCharByLine(splitByLine(convertToList()))))}")
print(f"Total Score by Group : {totalScore(priorityItem(repeatedCharBy3(splitBy3(convertToList()))))}")