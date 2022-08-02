import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly choses word from word list

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    hangman = ''  # string displaying how many mistakes are left
    hangman_progress = 0
    hangman_list = ['|\n',
                    ' \\\n',
                    '  O\n',
                    ' /|\\\n',
                    '/ | \\\n',
                    '  |\n',
                    ' / \\\n',
                    '/   \\\n']

    while len(word_letters) > 0 and hangman_progress < len(hangman_list):
        # letters used
        print("You have used these letters: ", " ".join(used_letters))
        print(hangman)

        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(" ".join(word_list))

        # getting user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                hangman += hangman_list[hangman_progress]
                hangman_progress += 1

        elif user_letter in used_letters:
            print("You already entered that letter. Please enter another letter.")

        else:
            print("Invalid character. Please enter a letter. ")

    if hangman_progress == len(hangman_list):
        print(hangman)
        print(f"You lose. The word was {word}. Try again!")
    else:
        print(f"Congrats, you guessed the word {word}!")


hangman()
