import csv


def export(file_path, bots_to_export):
    print("Exporting...")

    with open(file_path, "a") as file:

        for i in range(bots_to_export):
            bot_id = int(input("Please enter the bot id:\n"))
            bot_name = input("Please enter bot name:\n")
            bot_colour = input("Please enter bot colour:\n")
            data = f"{bot_id}, {bot_name}, {bot_colour}\n"
            file.write(data)
    print("Done!")

export("exported_bots.csv", 2)
