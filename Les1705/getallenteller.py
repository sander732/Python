import random

#een lijst maken met willekeurege getallen,
randomList=[]
for i in range(0,20):
    randomList.append(random.randint(1,5))

print(randomList)
#getallen teller
frequetieDict = {}
for getal in randomList:
    if getal in frequetieDict:
        aantal = frequetieDict[getal]
    else:
        aantal = 0
    frequetieDict[getal] = aantal + 1
print("list :", randomList)
print("Dict :", frequetieDict)
