import random


def select_word(input_list):
    # Use RNG to generate a random number between 0 and (list.len() -1)
    rng_number = random.uniform(0, (len(input_list)-1))
    chosen_word = input_list[rng_number]
    result_list = []
    for i in range(0, len(chosen_word)):
        result_list.append(chosen_word[i])
    return result_list


def check_guess(word, guess):
    # Take the char guess and cycle through the string word.
    # If there is a match, generate a list of the index numbers where the letter has been found.
    # If there is a second match, append to that list.
    # Print updated word
    # If there is no match, add 1 to hangman_count and let the user know it was not a match
    print("Checking guess against word...")


def game_loop(word, display_word, guesses, count):
    # Display underscores for each letter in current_word with a space in between
    display_string = "".join(display_word)
    print(display_string)
    # Print list of already used guesses
    if len(guesses) > 0:
        print("Already guessed:")
        print(guesses)
    # Ask for guess
    print("What letter is your next guess?")
    # Read guess
    guess_input = input()
    guess_letter = guess_input[0]
    guesses.append(guess_letter)
    # Call check_guess(current_word, guess)
    check_guess(word, guess_letter)


def start_game(wordlist):
    # Resetting count and guesses in case they have content
    hangman_count = 0
    already_guessed = []
    # Select current word randomly from wordlist
    current_word = select_word(hangman_words)
    # Prepare the displayed list of underscores for the game loop
    display_list = []
    for i in range(len(current_word)):
        display_list.append("_ ")
    # Call game loop with prepared data
    game_loop(current_word, display_list, already_guessed, hangman_count)


if __name__ == '__main__':
    # Display game title and current high score (stored in an external file)
    # Ask for username and if they want to start a game
    # Read wordlist from external JSON-file
    # Prototype version: use hardcoded short list
    hangman_words = ["jazz", "fluff", "haphazard", "zephyr", "fishhook", "exodus"]
    # Until GUI: Count up to 16 for every wrong guess, since the drawn hangman has 16 lines.
    # Starting count = 0
    hangman_count = 0
    # Preparing list of guesses
    already_guessed = []
