userSteps = int(input("How far are we from the cave?\n"))
userCount = userSteps

for i in range(userSteps):
    print(f"{userCount} steps remaining")
    userCount = userCount - 1

print("\nWe have reached the cave")