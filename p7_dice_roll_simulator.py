import random

# setting min and max value for the dice

min_val = 1
max_val = 6

rolling_again = "yes"

while rolling_again == "yes" or rolling_again == "y":
    print("Rolling the Dices....")
    print("The values are :")

    # generating and printing first random integer from 1 to 6
    print(random.randint(min_val, max_val))

    # generating and printing second random integer from 1 to 6
    print(random.randint(min_val, max_val))

    # asking the user to roll the dices again
    rolling_again = input("Roll the Dices Again?\n")
