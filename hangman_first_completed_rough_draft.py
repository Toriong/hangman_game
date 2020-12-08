from random_words import animals, movie_characters, USA_presidents, philosophers

import random

user_total_attempts = 10





def translate(word):
    translation = ''
    for letter_or_space in word:
        if letter_or_space in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ':
            translation = translation + ' _'
        elif letter_or_space in ' ':
            translation = translation + ' '


    return translation



input('Let\'s play Hangman! (Press ENTER to continue)')


random_words_choice = input('Choose the word type that you want to guess (choose a, b, c, or d): '
                            '\na. animals'
                            '\nb. movie characters'
                            '\nc. philosophers'
                            '\nd. US presidents'
                            '\nCHOICE: ')






if random_words_choice == 'a':
    animals_selected = random.choice(animals).upper()
    selected_word = animals_selected
    input('You\'ve chosen \'animals\' (Press ENTER to continue).')
    input('\n\nHere is your word to guess: ' + translate(selected_word) + '\n\n\n(Press ENTER to continue.)\n\n\n')

elif random_words_choice == 'b':
    movie_characters_selected = random.choice(movie_characters).upper()
    selected_word = movie_characters_selected
    input('You\'ve chosen \'movie characters\'.(Press ENTER to continue).')
    input('\n\nHere is your word to guess: ' + translate(selected_word) + '\n\n\n(Press ENTER to continue.)\n\n\n')

elif random_words_choice == 'c':
    philosophers_selected = random.choice(philosophers).upper()
    selected_word = philosophers_selected
    input('You\'ve chosen \'philosophers\'.(Press ENTER to continue).')
    input('\n\nHere is your word to guess: ' + translate(selected_word) + '\n\n\n(Press ENTER to continue.)\n\n\n')

elif random_words_choice == 'd':
    USA_presidents_selected = random.choice(USA_presidents).upper()
    selected_word = USA_presidents_selected
    input('You\'ve chosen \'USA presidents\'.(Press ENTER to continue).')
    input('\n\nHere is your word to guess: ' + translate(selected_word) + '\n\n\n(Press ENTER to continue.)\n\n\n')

else:
     exit('INVALID input. Please restart the program and try again.')





hangman_word_as_list = list(selected_word)


user_guess = []
used_letters = []
incorrect_guesses = []
correct_guesses = []
done = False


while not done:

    for letter in selected_word:
        if letter in user_guess:
            print(letter, end=' ')
            user_total_attempts += 0
            used_letters.append(letter)

        else:
            print('_', end=' ')






    print('')

    user_letter_guess = input('\nGuess a letter: ').upper()
    user_guess.append(user_letter_guess)



    if user_letter_guess in selected_word:
            correct_guesses.append(user_letter_guess)
            hangman_word_as_list = (''.join(list(selected_word)))
            print('\nCORRECT! Remaining guesses: ' + str(user_total_attempts) + '.')
            print('Correct guesses: ' + str((correct_guesses)) + '.')
            print('Incorrect guesses: ' + str((incorrect_guesses)) + '.')

    if ''.join(set(correct_guesses)) == ''.join(set(hangman_word_as_list)):
        break



    if user_letter_guess not in selected_word:
        incorrect_guesses.append(user_letter_guess)
        user_total_attempts -= 1
        print('\nINCORRECT! Remaining guesses: ' + str(user_total_attempts) + '.')
        print('Incorrect guesses: ' + str((incorrect_guesses)) + '.')
        print('Correct guesses: ' + str((correct_guesses)) + '.')
        if user_total_attempts == 0:
            break




if user_total_attempts == 0:
    print('\n\n\nYou are out of guesses! You LOSE! The word is ' + selected_word + '.')
else:
    print('\n\n\nCongrats! You WIN! The word is ' + selected_word + '.')










