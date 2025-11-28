# Created by: nissi
# Date: November 2025
# this program plays a game which askes the user for a number and if the user wants to quot he enters q



import random

def main():
    # generate random number from 0–9
    random_number = random.randint(0, 9)

    while True:
        try:
            # Ask user to guess a number
            user_input = int(input("Guess a number from 0 to 9 "))
    

        except ValueError:
            print("Please enter a valid number.")
            continue  # go back to top of loop

        # Compare guess with random number
        if user_input == random_number:
            print("You guessed right!")
            break   
        else:
            print("You guessed wrong!")


if __name__ == "__main__":
    main()
