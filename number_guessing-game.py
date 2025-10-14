import random
from colorama import Fore, Style

def number_guessing_game():
    print(Fore.CYAN + "🎯 Welcome to the Number Guessing Adventure! 🎯")
    print("Choose your difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-30)")
    print("3. Hard (1-50)")
    print("4. Expert (1-70)")
    print("5. Master (1-100)")

    # Choose level
    while True:
        try:
            level = int(input("Enter 1, 2, 3, 4, or 5: "))
            if level == 1:
                max_number = 10
                break
            elif level == 2:
                max_number = 30
                break
            elif level == 3:
                max_number = 50
                break
            elif level == 4:
                max_number = 70
                break
            elif level == 5:
                max_number = 100
                break
            else:
                print(Fore.YELLOW + "⚠ Please choose 1, 2, 3, 4, or 5.")
        except ValueError:
            print(Fore.RED + "❌ Enter a valid number!")

    secret_number = random.randint(1, max_number)
    attempts = 0
    guessed = False

    print(Fore.MAGENTA + f"\nI'm thinking of a number between 1 and {max_number}. Can you guess it? 🤔")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print(Fore.BLUE + "⬆ Too low! Try again.")
            elif user_guess > secret_number:
                print(Fore.BLUE + "⬇ Too high! Try again.")
            else:
                print(Fore.GREEN + f"🎉 You guessed it! The number was {secret_number}!")
                print(Fore.CYAN + f"It took you {attempts} attempts. 🏆")
                guessed = True
        except ValueError:
            print(Fore.RED + "❌ Please enter a valid number!")

# Run the game
number_guessing_game()