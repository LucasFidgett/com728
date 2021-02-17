userFirstNum = int(input("Please enter the first number: "))
userSecNum = int(input("Please enter the second number: "))

if userFirstNum < userSecNum:
    print("The second number is the smallest")
elif userFirstNum > userSecNum:
    print("The first number is bigger")
elif userFirstNum == userSecNum:
    print("The numbers are equal")
else:
    print("Invalid input")