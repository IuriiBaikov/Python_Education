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
    print(str(everyNumber)+ " ")


#     Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

# Если на вход пришло только одно число, надо вывести его же.

# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

# Sample Input 1:

# 1 3 5 6 10
# Sample Output 1:

# 13 6 9 15 7
# Sample Input 2:

# 10
# Sample Output 2:

# 10