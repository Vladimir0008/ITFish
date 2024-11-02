# 1/211
"""n = int(input("Input n: "))

for i in range(n+1):
    for j in range(i):
        print(i, end=" ")
    print("\t")
"""
import sys

# 2/212
"""n = int(input("Input n: "))
cnt = n
for i in range(n):
    for j in range(cnt):
        print("*", end="")
    print("\t")
    cnt = cnt - 1"""

# 3/213
"""n = int(input("Input n: "))
cnt = 0

for i in range(n):
    print("#", end="")
    for j in range(n):
        if j == cnt:
            print("#", end="")
        else:
            print(" ", end="")

    print("\t")
    cnt = cnt + 1
"""
# 4/217
"""
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

while a <= b:
    if a % c == 0:
        print(a, end=" ")
    a = a + 1
"""

# 5/222
"""n = int(input("Input n: "))

for i in range(n+1):
    if i%5 == 0 and i%3 == 0:
        print("*35*")
    elif i%5 == 0:
        print("*5*")
    elif i%3 == 0:
        print("*3*")
    else:
        print(i)
"""
#6/279
"""n = int(input("Input n: "))
cnt = 1
a = 1
b = 1

print(a, end=" ")
while cnt <= n:
    print(cnt, end=" ")
    cnt = a + b
    a = b
    b = cnt
    
"""
#6/282

"""cnt = 0
isNotFinish = True
num = sys.maxsize
#print(num)

while isNotFinish:
    n = int(input("Input number: "))
    if n == 0:
        break
    if n > num:
        cnt = cnt + 1
    num = n
print(cnt)
"""
#7/287
"""cnt = 0
sign = ""
firstValue = int(input("Input number: "))

if firstValue >=0:
    sign= "+"
else:
    sign = "-"

isNotFinish = True
while isNotFinish:

    n = int(input("Input number: "))
    if n == 0:
        break
    if sign == "+" and n < 0:
        cnt = cnt + 1
        sign = "-"
    elif sign == "-" and n >= 0:
        cnt = cnt + 1
        sign = "+"
print(cnt)
"""