name = str(input("What is your name?\n"))
age = int(input("What is your age?\n"))
height = float(input("what is your height (in meters)?\n"))
weight = int(input("What is your weight (in KG)?\n"))

bmi = weight / (height*height)

print(f"{name} you are {age} years old and your bmi is {bmi}.")