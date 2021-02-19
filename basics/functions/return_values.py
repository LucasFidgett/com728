def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight


def calc_avg_weight(beep_weight, bop_weight):
    average = sum_weights(beep_weight, bop_weight) / 2
    return average

def run():
    beepWeight =  int(input("What is the weight of Beep?\n"))
    bopWeight = int(input("What is the weight of Bop?\n"))

    user_input = input("What would you like to calculate?\n")
    if user_input == "sum":
        answer = sum_weights(beepWeight, bopWeight)
        print(f"The sum of Beep's and Bop's weights is: {answer}")
    elif user_input == "average":
        answer = calc_avg_weight(beepWeight, bopWeight)
        print(f"The average of Beep's and Bop's weights: {answer}")

run()