user_sequence = input("Please enter a sequence:\n")
user_char = input("Please enter a character for the marker\n")

marker1 = None
marker2 = None

for i in range(len(user_sequence)):
    letter = user_sequence[i]

    if letter == user_char:
        if marker1 == -1:
            marker1 = i
    else:
        marker2 = i

print(f"The distance between the markers is {marker1 - marker2 - 1}.")

#given up