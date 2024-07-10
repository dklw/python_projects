import random

while True:
    random_number = random.randint(1, 100)

    print("Welcome to the Guessing Game".center(100))

    attempts = 5

    while True:
        x = int(input("Enter your guess: "))
        attempts -= 1

        if x == random_number:
            print("Congratulations! You guessed it right.")
            break
        elif x < random_number:
            print("Too low!")
        else:
            print("Too high!")

        if attempts == 0:
            print("Sorry, you've run out of attempts. The correct number was", random_number)
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != 'yes':
        break
