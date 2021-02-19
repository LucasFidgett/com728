def cross_bridge(steps):
    userInput = steps
    for i in range(0, steps, 1):
        print("Crossed steps")
        steps = steps + 1

    if userInput < 6:
        print("We must keep going!")
    elif userInput >= 6:
        print("The bridge is collapsing!")

cross_bridge(3)
cross_bridge(6)
