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


def game_loop(word, count):
    # Display underscores for each letter in current_word with a space in between
    # Print list of already used guesses
    # Ask for guess
    # Read guess
    # Call check_guess(current_word, guess)
    print("Doing game loop...")


if __name__ == '__main__':
    # Display game title and current high score (stored in an external file)
    # Ask for username and if they want to start a game
    # Read wordlist from external JSON-file
    # Prototype version: use hardcoded short list
    hangman_words = ["jazz", "fluff", "haphazard", "zephyr", "fishhook", "exodus"]
    # Until GUI: Count up to 16 for every wrong guess, since the drawn hangman has 16 lines.
    # Starting count = 0
    hangman_count = 0
    # Select current word randomly from wordlist
    current_word = select_word(hangman_words)
