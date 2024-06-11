from decimal import Decimal
import random


def example_a():
    print('\nExample A')
    print('~~~~~~~~~')

    # "Magic Numbers" - do not hard code values into your program!
    # Always have a configuration section at the start of the function
    # So they can be easily changed later in one place
    # Larger programs have configuration files or an appsettings.json file for this stuff for the whole program.
    answer = 0

    number = int(input("How many Apple users does it take to change a lightbulb?: "))

    if number == answer:
        print("Correct! They just buy a new house, without any windows.")
    else:
        print(f"Nah, the answer is {answer} - They just buy a new house, without any windows!")


# Puzzle A - Lightbulbs
#
# Write a program that asks:
#   "How many dead hookers does it take to change a lightbulb?: "
# If the user enters more than 7 display:
#   "Yeah, got to be more than 7, because my basement is STILL dark."
# If the user enters less than 7 display:
#   "Well, I know it's more than 7, because my basement is STILL dark."
# If the user enters exactly 7, display:
#   "That's what I thought. I sent 7 down, but my basement is STILL dark."
# You will need to learn about "greater than" and "less than" symbols.
# Learn about "elif"
def puzzle_a():
    print('\nPuzzle A')
    print('~~~~~~~~~')


def example_b():
    print('\nExample B')
    print('~~~~~~~~~')

    print("Nuclear Missle Launch Program")
    print("-----------------------------")

    print("\nWho are we going to Nuke today, Mr President?")
    print("1: The secret nazi moon base")
    print("2: The tax department")

    target = int(input("Please enter the number of your selection: "))

    if target == 1:
        print(f"\nOk. Space-Hitler will be mad though...")
        confirmation = input(f"\nDo you confirm the launch to target the secret nazi moon base? Enter \"y\" or \"n\":")

        if confirmation == "y":
            print(f"Launch Confirmed! Bye Bye lunar reich!")
        elif confirmation == "n":
            print(f"Cancelling launch... Launch aborted!")
        else:
            print(f"Sorry, I cannot proceed with launch without explicit confirmation. Launch aborted!")
    elif target == 2:
        print(f"\nOk. Time to reduce taxes... to ash")
        confirmation = input(f"\nDo you confirm the launch to target the tax department? Enter \"y\" or \"n\":")

        if confirmation == "y":
            print(f"Launch Confirmed! Bye Bye taxes, hello new car!")
        elif confirmation == "n":
            print(f"Cancelling launch... Launch aborted!")
        else:
            print(f"Sorry, I cannot proceed with launch without explicit confirmation. Launch aborted!")
    else:
        print(f"You can't just enter random numbers when launching nukes!")


# Puzzle B - Forget About It!
#
# Write a program for an italian pizza restaurant
# Ask the customer if they would like a pizza, a calzone or lasagne
# For all choices, ask them if they want a regular or large
# Then print their order confirmation
# If they enter a wrong choice tell them "Tony Soprano owns this place, so you better order something"
# If they do not choose any of the options give them an error message
def puzzle_b():
    print('\nPuzzle B')
    print('~~~~~~~~~')


def example_c():
    print('\nExample C')
    print('~~~~~~~~~~~')

    user_input = input("Enter a number between 1 and 100: ")

    # Variable "number" has to be outside the "if statement" when we want to access it everywhere
    # Block Level Scope - Any variable created within brackets { } is only acessible within those brackets and sub-brackets.
    number = 0

    # Python's == checks the values are the same
    # Pythons "is" checks if they are the same object
    if user_input is not None and user_input != "":
        number = int(user_input)

        if number >= 1 and number <= 100:
            print("Fantastic, you can follow simple instructions!")
        else:
            print("Silly monkey! Can't count...")
    else:
        print("Error. You can't just enter blank space")

    print("\nBecause \"number = 0\" was declared outside of the if statement, I can access its final value here.")
    print(f"Number is now {number}")


# Puzzle C - Number Guesser
#
# Write a program that asks the user to guess a number
# Display "What number am I thinking of? It's between 1 and 10:"
# Generate a random number between 1 and 10.
# Check that the user's input is not blank or null
# Convert the user's input into an integer
# Check that the number is really between 1 and 10
# If it is within 1 digit of the random number generated ( +1 or -1) tell them
#   "Close! Out by one! Number was {number}"
# Otherwise, tell them
#   "Wrong! It was {number}"

# I'd expect the program to break if they enter a float like 1.52 or a string, that's ok for now.
# But it should not break if they just enter blank or hit return
def puzzle_c():
    print('\nPuzzle C')
    print('~~~~~~~~~~~')


if __name__ == '__main__':

    # Run the puzzles

    example_a()
    # puzzle_a()

    example_b()
    # puzzle_b()

    example_c()
    # puzzle_c()

