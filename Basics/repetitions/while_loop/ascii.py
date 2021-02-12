userInput = int(input("How many bars should be charged?\n"))
i = 1

while i < userInput+1:
    print(f"Charging: {'█ '*i}")
    i = i+1

print("The battery is fully charged.")