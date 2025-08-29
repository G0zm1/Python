from random import randint
from art import logo, lose, win

guessing_number = randint(1,100)
ATTEMPTS = 0
game_over = False
print(logo)


def decrease_attempts(attempts):
    return ATTEMPTS - 1


print("Welcome to the Number Guessing Game!\n\n")
print("I'm thinking of a number between 1 and 100.\n")
DIFFICULTY = input("Choose a difficulty. Type 'easy' ord 'hard'").lower()


if DIFFICULTY == "easy":
    ATTEMPTS = 10
elif DIFFICULTY == "hard":
    ATTEMPTS = 5

print(f"You have {ATTEMPTS} remaining to guess the number.")

while not game_over:
    guess = int(input("Make a guess: "))
    if guess != guessing_number:
        ATTEMPTS = decrease_attempts(ATTEMPTS)
        if guess < guessing_number:
            print("Too low.\nGuess again.\n")
        elif guess > guessing_number:
            print("Too high.\nGuess again.\n")
        print(f"You have {ATTEMPTS} remaining to guess the number.")

        if ATTEMPTS == 0:
            print(f"The answer was {guessing_number}\n{lose}")
            game_over = True
    else:
        print(f"You got it! The answer was {guessing_number}\n{win}")
        break



