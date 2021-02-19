user_rows = int(input("How many rows should I have?\n"))

user_columns = int(input("How many columns should I have?\n"))

print("Here I go:\n")

for columns in range(user_columns):
    for row in range(user_rows):
        print(":)", end = "")
    print("")