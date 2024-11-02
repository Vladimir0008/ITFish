# 304
# s = 'aaaaa'
# print(s.upper())
#
# 305
# s = str(input("Write the team name: "))
# print(s + "! This is a champion!")

# 306
# s = str(input("Write the string: "))
# res = s[-2::]
# print(res*5)

# 307
# s = str(input("Write the num: "))
# print(s*2)

# 308
# s = str(input("Write the num: "))
# print(s[::-1]

# 309 Дано рядок. Змініть регістр символів в цьому рядку так, щоб перша буква кожного слова була великою, а інші літери - малими.
# s = str(input("Write the string: "))
# s = s.title()
# print(s)

# 310 Дано натуральне число. Знайти число, що отримується в результаті приписування по двійці в початок і кінець запису вхідного числа.
# s = str(input("Write the num: "))
# print('2' + s + '2')

# 311 Користувач вводить рядок і набір символів. Напишіть програму, яка перевіряє чи починається рядок із зазначених символів.
# s = str(input("Write the first str: "))
# s2 = str(input("Write the checked str: "))
#
# s2len = len(s2)
# s1res = s[0:s2len]
# print(s1res==s2)

# 312 Дано рядок. Визначити порядковий номер першої вказаної букви. Якщо такої літери немає, вивести нуль.
# mainStr = str(input("Write the main str: "))
# character = str(input("Write letter which u're looking for: "))
# res = 0
# print(character in mainStr)
# for i in range(len(mainStr)):
#     if character == mainStr[i]:
#         res = i + 1
#         break
# print(res)

# 313 Дано слово. З’ясуйте, чи слово починається і закінчується на одну і ту ж букву? Регістр літер не враховувати.

# s = str(input("Write the main str: ")).lower()
# print (s[0] == s[-1])

# 314 Напишіть програму, яка отримує три рядки: прізвище, ім’я і по батькові особи, а потім виводить на екран ініціали та прізвище.

# sName = str(input("Write surname: "))
# name = str(input("Write name: "))
# fName = str(input("Write fName: "))
#
# res =  name[0] + "." + fName[0] + ". " + sName
#
# print(res)

# 315 Скласти програму, яка визначає, який з двох введених рядків довший і друкує його. Якщо рядки рівні, вивести повідомлення equally.
# a = str(input("Write the main str: "))
# b = str(input("Write the main str: "))
#
# if len(a) > len(b):
#     print(a)
# elif len(a) < len(b):
#     print(b)
# else:
#     print("equallya")

# 316 Дано натуральне число. Знайти число, що отримується з вхідного перестановкою його першої та останньої цифр. Врахувати випадок введення одноцифрового числа.
# n = str(input("Write a num: "))
# first = n[0]
# last = n[-1]
# body = n[1:-1]
#
# if len(n) == 1:
#     print(n)
# else:
#     print(last + body + first)
#
# 317 Дано два слова. Скласти програму, яка визначає, чи перше слово починається на ту ж букву, на яку закінчується друге слово.

# s = str(input("Write a word: "))
# s2 = str(input("Write another word: "))
#
# print(s[0] == s2[-1])

# 318 Дано натуральне число. Знайти число, що отримується видаленням з вхідного усіх зазначених цифр.
# n = str(input("Write a number: "))
# d = str(input("Write a digit for del: "))
#
# print(n.replace(d, ""))

# 319 Напишіть програму, яка зчитує значення a і b і виводить вірш, в якому замість a і b використовуються ці значення.

# a = str(input("Write a: "))
# b = str(input("Write b: "))
#
# print(f"{a} and {b} sat in the tree.\n{a}  had fallen, {b} was stolen.\nWhat's remaining in the tree?")

# 320 Користувач вводить рядок, в якому можуть бути пристуні пропуски. Визначити, чи є рядок паліндромом, тобто таким, який однаково читається як справа наліво,
# так і зліва направо. Для літер регістр не враховувати. Приклади рядків-паліндромів: racecar, 10201, Ada, Never odd or even.
# s = str(input("Write a word: "))
# print(s.lower() == s[::-1].lower())


# 333 Напишіть програму, яка виводить останнє слово у рядку. Слово – це послідовність непробільних символів, обмежена пропусками або межами рядка.
# Вхідний рядок містить довільну послідовність символів. Програма повинна вивести останнє слово цього рядка.

# s = str(input("Write a string: "))
# l = s.split(" ")
# print(l[-1])

# 334 Напишіть програму, яка по введеному числу n від 1 до 9 виводить на екран n пінгвінів з відповідним номером - число від 1 до n.
# Зображення одного пінгвіна має розмір 5 x 9 символів, між двома сусідніми пінгвінами також є порожній (з пропусків) стовпець.
# Дозволяється вивести порожній стовпець після останнього пінгвіна. Для спрощення малювання скопіюйте пінгвіна із вихідних даних.
# Врахуйте, що виведення на екран виконується порядково, а не «попінгвінно».
#    _~_        _~_        _~_        _~_
#   (o o)      (o o)      (o o)      (o o)
#  /  V  \    /  V  \    /  V  \    /  V  \
# /(  1  )\  /(  2  )\  /(  3  )\  /(  4  )\
#   ^^ ^^      ^^ ^^      ^^ ^^      ^^ ^^
# n = int(input("Write a number: "))
#
# cnt = 1
# row1 = '    _~_    '
# row2 = '   (o o)   '
# row3 = '  /  V  \\  '
# row5 = '   ^^ ^^   '
#
# while cnt <= n:
#     print(row1, end="\t")
#     cnt = cnt + 1
# print("\t")
# cnt = 1
# while cnt <= n:
#     print(row2, end="\t")
#     cnt = cnt + 1
# print("\t")
# cnt = 1
# while cnt <= n:
#     print(row3, end="\t")
#     cnt = cnt + 1
# print("\t")
# cnt = 1
# while cnt <= n:
#     print(f' /(  {cnt}  )\\ ', end="\t")
#     cnt = cnt + 1
# print("\t")
# cnt = 1
# while cnt <= n:
#     cnt = cnt + 1
#     print(row5, end="\t")

# 335 Дано рядок, який, можливо, містить пропуски. «Витягніть» з цього рядка всі символи, які є цифрами і складіть з них новий рядок.

# s = str(input("Write a string: "))
# l = list(s)
# res = ''
# for i in range(len(l)):
#     if l[i].isdigit():
#         res+=l[i]
# print(res)


# 337 Виведіть усі символи ASCII з кодами від n (n > 32) до m (m < 127) і їх коди в наступному вигляді: «символ код».

# n = int(input("Write a start symbol code: "))
# f = int(input("Write a finish symbol code: "))
#
# while n <= f:
#     print(chr(n) + " " + str(n))
#     n += 1

# 338 У рядку є кілька слів, розділених одним або декількома пропусками.
# Потрібно прибрати з тексту зайві пропуски: два і більше пропусків поспіль, а також всі пропуски на початку і в кінці рядка.
# На вхід програмі подається рядок, що складається не більше ніж з 255 символів. Надрукувати новий рядок.
# s = str(input("Write a string: "))
# l = s.split(" ")
#
# isEmptyInList = '' in l
#
# while isEmptyInList:
#     l.remove('')
#     isEmptyInList = '' in l
#
# print(' '.join(l))

# 339 Дано вираз, який має один з наступних виглядів: 'A+B', 'A-B' або 'A*B', де A і B - цілі числа від 0 до 1000000000. Визначте значення цього виразу.
# s = str(input("Write a string: "))
#
# if len(s.split("*")) == 2:
#     l = s.split("*")
#     res = int(l[0]) * int(l[1])
# elif len(s.split("+")) == 2:
#     l = s.split("+")
#     res = int(l[0]) + int(l[1])
# elif len(s.split("-")) == 2:
#     l = s.split("-")
#     res = int(l[0]) - int(l[1])
# print(res)

# 341 Виведіть поспіль, без пропусків, усі символи, що лежать в таблиці ASCII між двома заданими символами.
# Програма отримує на вхід два символу, кожен в окремому рядку і повинна вивести рядок, що починається першим із заданих символів і закінчується другим.

# s = str(input("Write a symbol1: "))
# s2 = str(input("Write a symbol2: "))
# start = ord(s)
# finish = ord(s2)
#
# while start <= finish:
#     print(chr(start), end=" ")
#     start+=1

# 359 Напишіть програму, яка зчитує рядок, введений користувачем, що містить дату у формі mm/dd/yyyy.
# Програма має вивести на екран дату у вигляді Місяць Число, Рік.
# s = str(input("Write a date: "))
# l = s.split("/")
#
# month = ''
#
# match l[0]:
#     case '1':
#         month = "January"
#     case '2':
#         month = "February"
#     case '3':
#         month = "March"
#     case '4':
#         month = "April"
#     case '5':
#         month = "May"
#     case '6':
#         month = "June"
#     case '7':
#         month = "July"
#     case '8':
#         month = "August"
#     case '9':
#         month = "September"
#     case '10':
#         month = "October"
#     case '11':
#         month = "November"
#     case '12':
#         month = "December"
#
# print(month + " " + l[1] + ", ", l[2])

# 362 Напишіть програму, яка зчитує рядок, введений користувачем, та визначає у ньому: кількість великих літер, кількість малих літер, кількість символів пропуску.
# s = str(input("Write a string: "))
# cntUpper = 0
# cntLower = 0
# cntSpaces = 0
# for i in range(len(s)):
#     if s[i].isupper():
#         cntUpper += 1
#     elif s[i].islower():
#         cntLower += 1
#     elif s[i].isspace():
#         cntSpaces += 1
# print("Upper " + str(cntUpper))
# print("Lower " + str(cntLower))
# print("Spaces " + str(cntSpaces))

# 380 Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій,
# кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.

# s = str(input("Write a string: "))
# sign = "+"
# res = 0
# for i in range(len(s)):
#     if s[i] == "+":
#         sign = "+"
#         continue
#     elif s[i] == "-":
#         sign = "-"
#         continue
#     if sign == "+":
#         res += int(s[i])
#     elif sign == "-":
#         res -= int(s[i])
# print(res)

# 382 Напишіть програму, на вхід якої даються чотири числа a, b, c і d, кожне у своєму рядку.
# Програма повинна вивести фрагмент таблиці множення для всіх чисел відрізка [a; b] на всі числа відрізка [c; d].
# Числа a, b, c і d є натуральними і не перевищують 10, a ≤ b, c ≤ d. Дотримуйтесь формату виведення як у вихідних даних.
# Для поділу елементів всередині рядка використовуйте \t - символ табуляції. Зауважте, що лівим стовпчиком і верхнім рядком виводяться самі числа із заданих відрізків.

# a = int(input("Write a: "))
# b = int(input("Write b: "))
# c = int(input("Write c: "))
# d = int(input("Write d: "))
#
# i = c - 1
# while i <= d:
#     if i < c:
#         print(" ", end="\t")
#     else:
#         print(i, end="\t")
#     i += 1
# print("\t")
#
# while a <= b:
#     i = c - 1
#     while i <= d:
#         if i < c:
#             print(a, end="\t")
#         else:
#             print(a * i, end="\t")
#         i += 1
#     print("\t")
#     a += 1

# 383 Напишіть програму для друку літери A за допомогою введеного користувачем символа.
# a = str(input("Write a  symbol: "))
#
# for i in range(6):
#     for j in range(5):
#         if i == 0 and j == 0 :
#             print(" ", end="")
#         elif i == 0 and j == 4 :
#             print(" ", end="")
#         elif i in (1,2,4,5,6) and j in (1,2,3) :
#             print(" ", end="")
#         else:
#             print(a, end="")
#     print("\t")

# 389 Користувач вводить рядок цифр без пропусків. Необхідно написати програму, яка «розіб’є» це число на трійки цифр справа наліво комами.
# Якщо число містить менше трьох цифр, то воно виводиться без змін.

# s = str(input("Write a number: "))
# a = len(s) % 3
#
# if len(s) <= 3:
#     print(s)
# else:
#     for i in range(len(s)):
#         if i == a - 1:
#             print(s[i], end=",")
#         elif (i - a + 1) % 3 == 0 and i < len(s) - 1:
#             print(s[i], end=",")
#         else:
#             print(s[i], end="")

# 398 Напишіть програму, яка переводить натуральне число N (1 ≤ N ≤ 3999) з римської системи числення в десяткову.
# Вхідний рядок містить число N, записане в римській системі числення. Програма повинна вивести десятковий запис числа N.
# s = str(input("Write a roman number: "))
# dct = {"I": 1,
#        "V": 5,
#        "X": 10,
#        "L": 50,
#        "C": 100,
#        "D": 500,
#        "M": 1000}
#
# res = 0
# i = len(s) - 1
#
# while i >= 0:
#        if s[i] == "I":
#               res += dct.get(s[i])
#        if s[i] in ("V", "X"):
#               if s[i-1] == "I" and i > 0:
#                      res += dct.get(s[i]) - dct.get(s[i-1])
#                      i = i - 1
#               else:
#                      res += dct.get(s[i])
#        if s[i] in ("L", "C"):
#               if s[i-1] == "X" and i > 0:
#                      res += dct.get(s[i]) - dct.get(s[i-1])
#                      i = i - 1
#               else:
#                      res += dct.get(s[i])
#        if s[i] in ("D", "M"):
#               if s[i-1] == "C" and i > 0:
#                      res += dct.get(s[i]) - dct.get(s[i-1])
#                      i = i - 1
#               else:
#                      res += dct.get(s[i])
#        i = i - 1
#
# print(res)
#399 Кодування довжин послідовностей - це базовий алгоритм стиснення даних. Реалізуйте один з найпростіших його варіантів.
# На вхід алгоритму подається рядок, що містить символи англійського алфавіту.
# Цей рядок розбивається на групи однакових символів, що йдуть підряд («серії»). Кожна серія характеризується символом і кількістю повторень.
# Саме ця інформація і записується в код: спочатку пишеться довжина серії повторюваних символів, потім сам символ.
# У серій довжиною в один символ кількість повторень не записується.
# s = str(input("Write a string: "))
#
# symbol = s[0]
# cnt = 1
# result = ''
#
# for i in range(1, len(s)):
#        if s[i] == symbol:
#               cnt += 1
#        else:
#               if cnt > 1:
#                      result += str(cnt) + symbol
#               else:
#                      result += symbol
#               cnt = 1
#               symbol = s[i]
#        if i == len(s) - 1:
#               if cnt > 1:
#                      result += str(cnt) + symbol
#               else:
#                      result += symbol
#
# print(result)

#400 Дано рядок, який може містити пропуски. Визначте, чи є цей рядок паліндромом, за умови, що великі і малі літери не розрізняються,
# а всі символи, які не є буквами, повинні бути пропущені. Виведіть слово Yes, якщо слово є паліндромом і слово No, якщо ні.
# Довжина вхідного рядка може бути до 100000 символів. При виконанні цього завдання не можна використовувати списки.
# import re
#
# s = str(input("Write a string: "))
# s = s.lower().replace(" ", "")
# s = re.sub(r'[^a-zA-Zа-яА-Я]', '', s)
#
# print(s)
# print(s[::-1])
# if s == s[::-1]:
#        print("Yes")
# else:
#        print("No")

#401 Дано рядок, що містить одне або більше цілих чисел від 0 до 1000000000, розділених знаками + або -. Розрахуйте значення цього виразу.
# s = str(input("Write a string: "))
# sign = "+"
# newSign = ""
# number = ''
# res = 0
# for i in range(len(s)):
#     if i == len(s) - 1:
#            number += str(s[i])
#     if s[i] in ("+", "-") or i == len(s) - 1:
#         newSign = s[i]
#         if sign == "+":
#               res += int(number)
#               number = ''
#               sign = newSign
#         elif sign == "-":
#               res -= int(number)
#               number = ''
#               sign = newSign
#         continue
#     number +=str(s[i])
#
# print(res)