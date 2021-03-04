import csv


def extract(file_path):
    print("Extracting...")

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        names = ""

        for values in csv_reader:
            names += f"{values[1]}\n"

        print("Done! The extracted names are as follows:")
        print(names)


def run():
    extract("bots.csv")



if __name__ == "__main__":
    run()