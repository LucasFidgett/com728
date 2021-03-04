import os


def cwd():
    path = os.getcwd()
    print(f"Current Working Directory: {path}")
    for i in os.listdir(path):
        print(i)


def run():
    print("Processing...")
    cwd()


run()
