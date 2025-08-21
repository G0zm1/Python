import random

lives = 6
from hangman_words import word_list
chosen_word = random.choice(word_list)

from hangman_art import logo, stages

print(logo)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess in correct_letters:
        print(f"You've already guessed: {guess}!")

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************\nThe word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
