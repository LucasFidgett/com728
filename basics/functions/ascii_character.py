print("Program Started!")

i = 0
while i != 1:
    userInput = int(input("Please enter an ASCII code: "))

    if abs(userInput) in range(32, 126):
        print(f"The character represented by the ASCII code {userInput} is {chr(userInput)}")
        i = 1
    else:
        print("Please enter a ASCII character code between 32 and 126.")

