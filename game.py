import random

def number_guessing_game():
    # Step 3: Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Step 4: Initialize a variable to count the number of attempts
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Step 5: Use a loop to let the player guess multiple times
    while True:
        # Step 6: Ask for the user's guess
        guess = int(input("Enter your guess: "))

        # Step 7: Increment the number of attempts
        attempts += 1

        # Step 8: Give feedback based on the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts!")
            break  # End the game once the correct guess is made

if __name__ == "__main__":
    number_guessing_game()
