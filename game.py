import random

print("🎮 Welcome to the Number Guessing Game 🎮")

while True:
    secret_number = random.randint(1, 50)
    attempts = 0

    print("\nI have selected a number between 1 and 50.")
    print("Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print(" Too low! Try again.")
        elif guess > secret_number:
            print(" Too high! Try again.")
        else:
            print(f" Correct! You guessed it in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(" Thanks for playing!")
        break
