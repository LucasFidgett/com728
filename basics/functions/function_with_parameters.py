def climb_ladder(stepsRemaining, stepsCrossed):
    if stepsRemaining > stepsCrossed:
        print("Still some way to go!")
    elif stepsCrossed > stepsRemaining:
        print("We are almost there!")

climb_ladder(5,2)
climb_ladder(2,5)