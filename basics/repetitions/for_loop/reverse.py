userPhrase = input("What phrase do you see?\n")

print("Reversing...")
print("The phrase is: ", end="")
for i in range(len(userPhrase)-1, -1, -1):
    print(f"{userPhrase[i]}", end="")