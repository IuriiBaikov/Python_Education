numberList = [int(i) for i in input().split()]
# First solution
outputList = []
for j in range(len(numberList)):
    if len(numberList)==1:
        outputList.append(numberList[0])
    elif len(numberList)==2:
        outputList.append(sum(numberList))
        break
    elif j==0:
        outputList.append(numberList[(len(numberList)-1)] + numberList[j+1])
    elif j==(len(numberList)-1):
        outputList.append(numberList[j-1] + numberList[0])
    else:
        outputList.append(numberList[j-1] + numberList[j+1])
for everyNumber in outputList:
    print(str(everyNumber+) " ")