from random_words import animals

import random

user_attempts = 10
user_starting_attempts = 0




def translate(word):
    translation = ''
    for letter_or_space in word:
        if letter_or_space in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ':
            translation = translation + '_'
        elif letter_or_space in ' ':
            translation = translation + ' '


    return translation

hangman_word = random.choice(animals).upper()
input(hangman_word)

hangman_word_as_list = list(hangman_word)
input(hangman_word_as_list)



user_letter_guess = input('Guess a letter: ').upper()

used_letters = []
done = False


:
    for letter in hangman_word_as_list:
        if letter in user_letter_guess:
            print(letter, end= '')
            user_starting_attempts += 0
            used_letters.append(letter)
        else:
            print('_', end= '')

    done = True




