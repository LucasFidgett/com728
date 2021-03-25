import json


def read(file_path):
    with open(file_path) as file:
        data = json.load(file)

        city = data["city"]
        print(f"City name: {city}")

        pop = data["population"]
        print(f"Population: {pop}")

        for bot in data["bots"]:
           name = bot["name"]
           stats = bot["stats"]
           print(f"{name} has the following stats: {stats}")


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()

