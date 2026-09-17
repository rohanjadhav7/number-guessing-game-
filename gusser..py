import random

def start_game():
    target_number = random.randint(1, 10)
    print("Welcome to the Number Guesser!")
    print("I am thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Spot on! The number was {target_number}.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    start_game()