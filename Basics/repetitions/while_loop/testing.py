print("How many live cables must I avoid?")
live_cables = int(input())

cables_avoided = 0

print()

while cables_avoided < live_cables:
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print(f"...Done {cables_avoided} live cables avoided")

print("All live cables have been avoided")
