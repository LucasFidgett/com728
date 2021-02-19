def cross_bridge(steps):
    userInput = steps
    for steps in range(steps):
        print("Crossed steps.")

    if userInput < 6:
        print("We must keep going!")
    elif userInput >= 6:
        print("The bridge is collapsing!")

cross_bridge(3)
cross_bridge(6)
