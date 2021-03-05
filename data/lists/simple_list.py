def directions():
    directions_list = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions_list


def run():
    directions_display = directions()
    print(directions_display)


if __name__ == "__main__":
    run()
