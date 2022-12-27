with open('Code01/input.txt') as file:
    intNestedLst = [[int(line) for line in lineBlock.split()] for lineBlock in file.read().split('\n\n')]
sumLst = [sum(intLst) for intLst in intNestedLst]
print(f"Part One : {max(sumLst)}")
print(f"Part Two : {sum(sorted(sumLst, reverse=True)[:3])}")