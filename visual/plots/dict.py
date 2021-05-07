import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}
    user_line = input("Select :, -- or - as the type of line to use:\n")
    user_colour = input("Select r, g or b as the colour to use\n")
    user_marker = input("Select which marker to use o, s or ^\n")

    paths['user_line'] = user_line
    paths['user_colour'] = user_colour
    paths['user_marker'] = user_marker

    return paths


def generate():
    user_lines = int(input("How many lines would you like to display?\n"))

    for i in range(user_lines):
        values = data()
        x_value = rnd.sample(range(1, 10), 5)
        y_value = rnd.sample(range(1, 10), 5)
        user_format = f"{values['user_colour']}{values['user_line']}{values['user_marker']}"
        plt.plot(x_value, y_value, user_format)

    plt.show()


def run():
    print("Running....")
    generate()
    print("Done!")


run()