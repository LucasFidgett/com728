userAmount = int(input("How many numbers should I sum up?\n"))
i = 1
total = 0
while i <= userAmount:
    print(f"Please enter number {i} of {userAmount}")
    total = int(input()) + total
    i = i + 1
print(f"The total is {total}.")