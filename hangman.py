import os
import words_lib
from random import choice


def get_word():
    return choice(words_lib.word_list).upper()


def print_hangman(tries):
    figure = [
        r"""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
        r"""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
        r"""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
        r"""
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
        r"""
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
        r"""
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
        r"""
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]

    return figure[tries]


def play_again():
    response = input("Do you wish to play again ?(Y/N): ").lower()
    if response == 'y':
        return True
    return False


def main():

    # Initial
    tries = 7
    print("\nHANGMAN")
    guessed = False

    # get the word for the game
    answer = get_word()
    blanks = '_' * len(answer)
    guessed_char = []

    # run for all the 7 tries (game loop)
    while not guessed:

        # initail prints
        print(print_hangman(tries-1))
        print(blanks)
        guess = input('Input the guessed letter: ').upper()

        # input validation
        if len(guess) == 1 and guess.isalpha():

            # if the letter is already guessed
            if guess in guessed_char:
                print('You have already guessed the letter.', guess)

            # if the guess is wrong
            elif guess not in answer:
                print("WRONG GUESS!!")
                tries -= 1
                guessed_char.append(guess)

            # in case of write guess
            else:
                guessed_char.append(guess)
                blanks_list = list(blanks)

                # position of the guessed character in answer
                indices = [i for i, c in enumerate(answer) if c == guess]
                for index in indices:
                    blanks_list[index] = guess
                blanks = ''.join(blanks_list)

                # check win
                if '_' not in blanks:
                    print("CONGRATS!! YOU GUESSED THE WORD", blanks)
                    guessed = True

        else:
            print("only alphabet are acceptable.")


if __name__ == "__main__":
    main()
    while play_again():
        main()
