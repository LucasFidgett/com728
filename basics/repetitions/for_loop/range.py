userInput = int(input("What level of brightness is required? (even number) \n"))

print("Adjusting brightness")

for i in range(2,userInput+1,2):
    print(f"Beep's brightness level:{i * '*'}")
    print(f"Bop's brightness level:{i * '*'}\n")


print("\nAdjustments complete!")
