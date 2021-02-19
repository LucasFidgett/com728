userPhrase = input("What phrase do you see?\n")

print("Reversing...")
print("The phrase is: ", end="")


for i in userPhrase:
    print(f"{userPhrase[i]}", end="")


# Ask user for phrase
print("What phrase do you see?")
phrase = input()

# Identify markings
print("\nReversing...")
print("The phrase is ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)