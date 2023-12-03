import re

f = open("input.txt","r")
finalPartOne = 0
finalPartTwo = 0

for i in f:
    tmpList = []
    tmpList2 = []

    for j, c in enumerate(i):
        if c.isdigit():
            tmpList.append(c)
            tmpList2.append(c)
        
        for index, letter in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if i[j:].startswith(letter):
                tmpList2.append(str(index+1))

    finalPartOne += int(tmpList[0]+tmpList[-1])
    finalPartTwo += int(tmpList2[0]+tmpList2[-1])