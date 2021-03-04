import csv


def read(csv_file_path):
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file)

        headings = next(csv_reader)
        print(f"Headings:\n {headings}")

        print("Values:")
        for values in csv_reader:
            print(values)


def run():
    read("bots.csv")


if __name__ == "__main__":
    run()
