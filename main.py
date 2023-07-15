
# 9.182.
#      Даны два предложения. Напечатать слова, которые есть только
#      в одном из них (в том числе повторяющиеся).

sent = input('Enter sentence one: ')
sent1 = input('Enter sentence two: ')

sentList = sent.split(' ')
sentList1 = sent1.split(' ')

for index in range(len(sentList)):
    if sentList[index] not in sentList1:
        print(sentList[index])

for index in range(len(sentList1)):
    if sentList1[index] not in sentList:
        print(sentList1[index])


# 9.183.
#      Даны два предложения. Напечатать слова, которые встречаются в двух
#      предложениях только один раз.

sent = input('Enter sentence one: ')
sent1 = input('Enter sentence two: ')

result = sent + ' ' + sent1

resultList = result.split(' ')

for item in resultList:
    if resultList.count(item) == 1:
        print(item)


# 8.54.
# *Дано натуральное число n. Получить все простые делители этого числа

# Если одно натуральное число нацело делится на другое натуральное число,
# то первое число называют кратным второму числу,
# а второе число называют делителем первого числа.

import random

n = random.randint(1, 50)

print(n)  # выводим само число 'n' т.к. оно также явл-ся делителем самого себя

m = n - 1

while m > 0:
    if n % m == 0:
        print(m)
    m -= 1


# 11.245.
# *Дан массив. Переписать его элементы в другой массив такого же размера
# следующим образом: сначала должны идти все отрицательные элементы,
# а затем все остальные. Использовать только один проход по исходному массиву

someList = [25, 45, -8, -15, 8, -7, 0]

result = []
result1 = []

for index in range(len(someList)):
    if someList[index] < 0:
        result.append(someList[index])
    # elif someList[index] >= 0:
    else:
        result1.append(someList[index])

print(result + result1)


# Задача.
# Даны 2 матрицы, написать функцию для нахождения суммы этих матриц.

def summ_two_matrix(matrix_two):

    summ = 0
    for index in range(lenX):
        for i in range(lenY):
            summ += matrix_two[index][i]
    # print(summ)
    return summ

lenX = int(input('Enter X: '))
lenY = int(input('Enter Y: '))

matrix = [[]] * lenX
for i in range(lenX):
    matrix[i] = [0] * lenY

import random

for i in range(lenX):
    for j in range(lenY):
        matrix[i][j] = random.randint(10, 99)

for i in range(lenX):
    print(matrix[i])

summ_two_matrix(matrix)

lenX2 = int(input('Enter X2: '))
lenY2 = int(input('Enter Y2: '))

matrix2 = [[]] * lenX2
for i in range(lenX2):
    matrix2[i] = [0] * lenY2

import random

for i in range(lenX2):
    for j in range(lenY2):
        matrix2[i][j] = random.randint(10, 99)

for i in range(lenX2):
    print(matrix2[i])

summ_two_matrix(matrix2)

result = summ_two_matrix(matrix) + summ_two_matrix(matrix2)
print(result)
