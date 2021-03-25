def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods

def run():
    likelihoods = likelihood()
    print(f"Minimum likelihood of falling: {min(likelihoods)}%")
    print(f"Maximum likelihood of falling: {max(likelihoods)}%")

if __name__ == "__main__":
    run()

    # or

    # min_value, max_value = likelihood