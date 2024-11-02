# 1
"""inputNum = int(input("Please input 4-digit number: "))


first = str(inputNum)[0]
sec = str(inputNum)[1]
third = str(inputNum)[2]
fourth = str(inputNum)[3]

result = True

if first == sec or first == third or first == fourth or sec == third or sec == fourth or third == fourth:
    result = False

print(result)
"""

# 2
"""minutes = int(input("Please input  minutes: "))

if minutes % 5 == 3 or minutes % 5 == 2 or minutes % 5 == 1:
    print("green")
else:
    print("red")"""

# 3
"""d = int(input("Please input day: "))
m = int(input("Please input month: "))
y = int(input("Please input year: "))

print(str(d) + "." + str(m) + "." + str(y))

if d == 1 and m in (2, 4, 6, 9, 11):
    d = 31
    m = m - 1
elif d == 1 and m in (1, 5, 7, 8, 10, 12):
    d = 30
    if m == 1:
        m = 12
        y = y - 1
    else:
        m = m - 1
elif d == 1 and m == 3 and y % 4 == 0:
    d = 29
    m = m - 1
elif d == 1 and m in (3) and y % 4 != 0:
    d = 28
    m = m - 1
else:
    d = d - 1

print(str(d) + "." + str(m) + "." + str(y))
"""
# 4
"""n = 3

while i < n:
    print("Hello, Python!")
    i = i + 1

for i in range(n):
    print("Hello, Python!")
"""
# 5
"""a = int(input("Please input num1: "))
b = int(input("Please input num2: "))

cnt = b - a
res = a
for i in range(cnt + 1):
    print(res, end=" ")
 res = res + 1
"""
# 6
"""a = int(input("Please input sec: "))
res = a

for i in range(a + 1):
    if res == 0:
        print("Start")
    else:
        print(res)
    res = res - 1
"""

# 7
"""subjectCnt = int(input("Input subject count: "))

cnt = 1
res = 0.00
for i in range(subjectCnt):
    grade = float(input("Input grade " + str(cnt) + ": "))
    res = res + grade
    cnt = cnt + 1
print(res/subjectCnt)
"""
# 8
"""password = int(input("Input password: "))

isCorrect = False

while isCorrect is not True:
    inputPass = int(input("Input password: "))
    if inputPass == password:
        isCorrect = True
        print("Done")
        break
    print("Error")
 """
# 9
"""n = int(input("Input n: "))
operand = '-'
divider = 1
result = 4
for i in range(n-1):
    divider = divider + 2
    if operand == '-':
        result = result - 4/divider
        operand = '+'
    else:
        result = result + 4/divider
        operand = '-'
print(result)
"""
# 10
"""n = int(input("Input n: "))
cnt = 0
while cnt != n:
    zeroPoint = cnt
    innerCnt = 0
    while innerCnt != n:
        if zeroPoint < innerCnt:
            print('1', end='\t')
        elif zeroPoint == innerCnt:
            print('0', end='\t')
        else:
            print('-1', end='\t')
        innerCnt = innerCnt + 1
    print('\t')
    cnt = cnt + 1
"""
# 11
#Дано натуральне число n. Надрукуйте всі n-значні непарні натуральні числа в порядку спадання.
"""n = int(input("Input n: "))
rangeNumStr = ''

for i in range(n):
    rangeNumStr = rangeNumStr + '9'

rangeNum = int(rangeNumStr)

for i in range(rangeNum):
    if rangeNum % 2 == 1:
        if (len(str(rangeNum)) == n):
            print(rangeNum, end=' ')
        else:
            break
    rangeNum = rangeNum - 1
"""
#12
#Дано два натуральних числа a і b. Розробити програму для визначення найбільшого спільного дільника (НСД) заданих чисел. Використайте алгоритм Евкліда .
"""a = int(input("Input a: "))
b = int(input("Input b: "))

oper1 = abs(a)
oper2 = abs(b)

maxDivider = 1
isFound = False

while isFound is not True:
    if oper1 == oper2:
        maxDivider = oper1
        break
    elif oper1 > oper2:
       oper1 = oper1 - oper2
    else:
        oper2 = oper2 - oper1

print(maxDivider)
"""
#12
#Надрукувати всі парні числа з інтервалу [a, b] (a ≤ b). Розглянути варіант програми без використання інструкції розгалуження.
"""a = int(input("Input a: "))
b = int(input("Input b: "))

cnt = a + a % 2
while cnt <= b:
    print(cnt, end = " ")
    cnt = cnt + 2
 """
#13 Задумали два натуральних числа x і y (x, y ≤ 1000).
# Щоб відгадати ці числа, називають суму цих чисел a і їх добуток b. Відгадайте ці числа і виведіть їх в порядку зростання, розділяючи пропуском.

x = int(input("Input x: "))
y = int(input("Input y: "))

minNum = 0;
if x > y:
    minNum = y
else:
    minNum = x