print("Program started!")
i = 0
while i != 1:
    userInput = input("Please enter a standard character: ")

    if len(userInput) == 1:
        print(f"The ASCII code for {userInput} is {ord(userInput)}.")
        print("Program Ended")
        i = 1
    else:
        print("Please enter a single character.")

