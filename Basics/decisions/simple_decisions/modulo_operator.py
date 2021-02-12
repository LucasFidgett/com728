userInput = int(input("Please enter a whole number \n"))

userMod = userInput % 2

if userMod == 1:
    print(f"The number {userInput} is an odd number.")
else:
    print(f"The number {userInput} is an even number.")