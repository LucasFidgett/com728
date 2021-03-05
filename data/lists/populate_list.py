def directions():
    directions_to_return = ["Move Forward", "Move Back", "Turn Left", "Turn Right"]
    return directions_to_return


def menu():
    print("Please select a direction:")
    directions_list = directions()
    for index in range(len(directions_list)):
        direction = directions_list[index]
        print(f"{index}: {direction}")
    user_direction = int(input())
    return user_direction


def run():
    route = []
    print("Working out escape route...\n")
    for i in range(5):
        selection = menu()
        route.append(directions()[selection])
    print(route)


if __name__ == "__main__":
    run()
