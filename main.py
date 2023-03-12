import random
import json
import wordlist
import data


def check_guess(word, guess):
    # Take the char guess and cycle through the string word.
    # If there is a match, generate a list of the index numbers where the letter has been found.
    # If there is a second match, append to that list.
    # Print updated word
    # If there is no match, add 1 to hangman_count and let the user know it was not a match
    pass


def game_loop(word, display_word):
    # Display underscores for each letter in current_word with a space in between
    display_string = "".join(display_word)
    print(display_string)
    # Print list of already used guesses
    global already_guessed
    if len(already_guessed) > 0:
        print("Already guessed:")
        print(already_guessed)
    # Ask for guess
    print("What letter is your next guess?")
    # Read guess
    guess_input = input()
    guess_letter = guess_input[0]
    already_guessed.append(guess_letter)
    # Call check_guess(current_word, guess)
    check_guess(word, guess_letter)


def select_word(input_list):
    # Use RNG to generate a random number between 0 and (list.len() -1)
    rng_number = random.uniform(0, (len(input_list)-1))
    chosen_word = input_list[rng_number]
    result_list = []
    for i in range(0, len(chosen_word)):
        result_list.append(chosen_word[i])
    return result_list


def start_game(list_of_words):
    # Resetting count and guesses in case they have content
    global hangman_count
    hangman_count = 0
    global already_guessed
    already_guessed = []
    # Select current word randomly from wordlist
    current_word = select_word(list_of_words)
    # Prepare the displayed list of underscores for the game loop
    display_list = []
    for i in range(len(current_word)):
        display_list.append("_ ")
    # Call game loop with prepared data
    game_loop(current_word, display_list)


if __name__ == '__main__':
    # Prototype version: use hardcoded short list for words to choose from
    # hangman_words = ["jazz", "fluff", "haphazard", "zephyr", "fishhook", "exodus"]
    # Until GUI: Count up to 16 for every wrong guess, since the drawn hangman has 16 lines.
    # Starting count = 0
    hangman_count = 0
    # Preparing list of guesses
    already_guessed = []
    # Display game title and current high score (stored in an external file)
    print(data.menu_texts["welcome_text"])
    # Ask for username and if they want to start a game
    print("Press y to start game.")
    input_game_start = input()
    if input_game_start == "y":
        start_game(wordlist.hangman_words)
    else:
        print("It seems you don't want to play right now. See you around!")
