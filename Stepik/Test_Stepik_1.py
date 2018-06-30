numberList = [int(i) for i in input().split()]
# The firs solution
j=1
z=numberList[0]
while j<len(numberList):
    z+=numberList[j]
    j+=1
print(z)

# The second solution
numberList=[int(i) for i in input().split()]
print(sum(numberList))

# Stepik question
# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
# Используйте метод split строки. ﻿﻿
# Sample Input:
# 4 -1 9 3
# Sample Output:
# 15