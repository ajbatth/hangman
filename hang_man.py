from words import words
import random
import string


def get_valid_word():
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = len(word)
    while lives and len(word_letters):
        print('\n')
        print(f"lives left = {lives}")
        print("letters used are: ", ' '.join(used_letters))

        current_word_list = [letter if letter in used_letters else '_' for letter in word]
        print("current word: ", ' '.join(current_word_list))
        user_letter = input("Guess a Letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives -= 1
                print(f"Your letter {user_letter} is not in the Word.")

        elif user_letter in used_letters:
            print("You have used this letter before")

        else:
            print("This isn't a valid letter.")

    if lives == 0:
        print("OOPSS You died.\n Try again :)")

    else:
        print("WOOOOHOOOO  You guessed it right.\n Thanks for playing :)")


if __name__ == '__main__':
    hangman()
