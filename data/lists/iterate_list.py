def directions():
    directions = ["Move Forward", "Move Back", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    directions_list = directions()
    for index in range(len(directions_list)):
        direction = directions_list[index]
        print(f"{index}: {direction}")


def run():
    menu()


if __name__ == "__main__":
    run()