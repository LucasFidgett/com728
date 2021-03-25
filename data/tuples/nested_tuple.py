def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run():
    likelihoods = steps()
    good_steps = []
    bad_steps = []

    for i in likelihoods:
        if (i[1] >= 50):
            bad_steps.append(i)
        else:
            good_steps.append(i)

    print(f"Good Steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

if __name__ == "__main__":
    run()
