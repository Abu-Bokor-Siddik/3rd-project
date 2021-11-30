num1 = int(input("Pease enter a number"))
num2 = int(input("Pease enter a number"))
num3 = int(input("Pease enter a number"))
num4 = int(input("Pease enter a number"))

if(num1>num4):
    r1 = num1
else:
    r1 = num2

if(num2>num3):
    r2 = num2
else:
    r2 = num3

if(r1>r2):
    print(int(r1), "is greatest")
else:
    print(int(r2), "is greatest")