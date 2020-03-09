import random
high_score = 0
score = 0
roll_again = True

'''  ================================================================
     This function rolls all of the dice.
     
     Parameters:
         > num_sides:  How many sides do you want the dice to have?
         > num_dice:  How many dice do you want to roll?
         
     Return value:  The total of all of the dice.
     ================================================================ '''


def roll(num_sides, num_dice):
    rolled = 0
    total = 0

    print("You rolled:")
    while rolled < num_dice:
        single = random.randint(1, num_sides)
        total += single
        print("[" + str(single) + "]")
        rolled = rolled + 1

    return total


while roll_again:
    score = roll(6, 5)
    print("You rolled:  " + str(score))

    if score > high_score:
        print("It's a new high score!")
        high_score = score

    user_input = ""
    while user_input != "y" and user_input != 'n':
        user_input = input("Do you want to roll again? (y/n)")
        if user_input == "n":
            roll_again = False

    print("\n")
