# Define the function
def commence():
    # Lines 4 & 5 print out the statements
    print("The Avengers Initiative")
    print("Please enter the number of days: ")
    # Line 6 reads the users input and stores as the variable num_of_days
    num_of_days = int(input())
    # Line 7 prints out the statement with the variable num_of_days using an f string
    print(f"The Avengers Initiative will commence in {num_of_days} days.")


# Run the function
commence()


# Define the function passing through leader
def lead(leader):
    # If function, if the answer is Tony Stark the message "The Avengers are ready will display"
    # If it is anything else the if function will print "We need a better leader."
    if leader == "Tony Stark":
        print("The Avengers are ready!")
    else:
        print("We need a better leader.")


# Call the function passing through Hulk and Tony Stark as the string respectively
lead("Hulk")
lead("Tony Stark")


# Define the function passing through num_avengers
def assemble(num_avengers):
    # Print line
    print("Assembling Avengers...")
    # Starts a for loop starting at 0 (i) counting up to the value stored in the variable num_avengers
    # and loops that amount of times (3). Each loop printing the string ... Avenger has assembled.
    for i in range(num_avengers):
        print("... Avenger has assembled.")


# Calls the function and passes through the integer 3
assemble(3)
