import math
"""#1
password = "starlink"

inputPass = input()

if inputPass == password:
    print("Password accepted!")
else:
    print("Sorry, that's the wrong password")
"""
"""#2
inputNum = int(input("Vvedit chislo: "))

dct = {1: "One", 2: "Two", 3: "Three"}

if dct.get(inputNum) is not None:
    print(dct.get(inputNum))
else:
    print("Unknown")
"""
"""#3
inputNum = int(input("Vvedit chislo: "))

match inputNum:
    case 3:
        print("That's a triangle.")
    case 4:
        print("That's a quadrilateral.")
    case 5:
        print("That's a pentagon.")
    case 6:
        print("That's a hexagon.")
    case _:
        print("The number of sides is not supported by this program.")
"""
"""#4
inputNum = int(input("Vvedit chislo: "))

if 1 <= inputNum <= 3:
    print("initial level")
elif inputNum >= 4 and inputNum <=6:
    print("average level")
elif 7 <= inputNum and inputNum <=8:
    print("sufficient level")
elif inputNum >= 10 and inputNum <=12:
    print("high level")
else:
    print("Level is absent")
"""
"""#5
radius = float(input("Input radius: "))
length = float(input("Input square length: "))

circleArea = 3.14 * radius ** 2
squareArea = length * length

if circleArea > squareArea:
    print("Circle")
elif circleArea < squareArea:
    print("Square")
else:
    print("Areas are equal")
"""
"""#6
hours = float(input("Input hours: "))
wage = float(input("Input wage: "))

if hours <= 40:
    print(hours * wage)
else:
    print(40 * wage + (hours - 40) * wage * 1.5)
"""
"""#7
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

d = b**2 - 4*a*c

if d < 0:
    print("No roots")
elif d == 0:
    result = (-b + math.sqrt(d)) / (2 * a)
    print(round(result, 2))
else:
    result1 = (-b + math.sqrt(d)) / (2 * a)
    result2 = (-b - math.sqrt(d)) / (2 * a)
    print(round(result1, 2), " and ", round(result2 , 2))
"""
"""#8
first = float(input("Input first num: "))
second = float(input("Input second num: "))
action = str(input("Input action: "))

match action:
    case "+":
      print(first + second)
    case "-":
      print(first - second)
    case "*":
      print(first * second)
    case "/":
        if second == 0:
            print("Division by 0")
        else :
            print(first/second)
    case "mod":
      print(first % second)
    case "div":
        if second == 0:
            print("Division by 0")
        else:
            print(int(first/second))
    case _:
        print("Something went wrong")
"""
#9
num = int(input("vvedit 4 cifrove chislo: "))

first = int(str(num)[0])
second = int(str(num)[1])
third = int(str(num)[2])
fourth = int(str(num)[3])

if (first + second) == (third + fourth):
    print(True)
else:
    print(False)