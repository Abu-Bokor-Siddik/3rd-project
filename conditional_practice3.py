# names = ["Tanim" , "Lodi", "samir", "zishan", "mahathir","zishan"]
# name = input("Please enter your name")

# if(name in names):
#     print("This name is present")
# else:
#     print("This name is not present")

marks = int(input("please enter your marks"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
elif marks>=40:
    grade = "E"
else:
    grade = "Fail"

print("your grade is" + grade)

