userLook = input("Where should I look?\n")

if userLook == "in the bedroom":
    userBedroom = input("Where in the bedroom should I look?\n")
    if userBedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("found some mess but no battery")

elif userLook == "in the bathroom":
    bathroomLook = input("Where in the bathroom should I look?\n")
    if bathroomLook == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

elif userLook == "in the lab":
    labLook = input("Where in the lab should I look?\n")
    if labLook == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")

else:
    print("I do not know where that is but I will keep looking!")
