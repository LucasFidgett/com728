def display_in_box(user_word):
    box_top = (len(user_word) + 3) * '*'
    print(box_top)
    print(f"* {user_word} *")
    print(box_top)


def display_in_lowercase(user_word):
    print(user_word.lower())
    # return(user_word.lower())


def display_in_uppercase(user_word):
    print(user_word.upper())
    # return(user_word.upper())


def display_in_mirrored(user_word):
    mirrored_word = ""
    for i in reversed(user_word):
        mirrored_word = mirrored_word + i
    print(f"{user_word} | {mirrored_word}")


def display_repeated(user_word):
    times_repeated = int(input("How many repetitions of the word?\n"))
    for i in range(times_repeated):
        print(f"{user_word.lower()} {user_word.upper()}", end=" ")


def run():
    i = 0
    user_word = input("Please enter a word\n")
    while i == 0:
        user_option = input("""Please select an option...
[1] Display word in box
[2] Display word in lowercase
[3] Display word in uppercase 
[4] Display word mirrored
[5] Display word repeated
[x] Exit\n""")
        if user_option == "1":
            display_in_box(user_word)
        elif user_option == "2":
            display_in_lowercase(user_word)
        elif user_option == "3":
            display_in_uppercase(user_word)
        elif user_option == "4":
            display_in_mirrored(user_word)
        elif user_option == "5":
            display_repeated(user_word)
        elif user_option == "x":
            i = 1
        else:
            print("Invalid input")


run()
