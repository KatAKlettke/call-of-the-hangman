menu_texts = {
    "welcome_text": "Welcome to Hangman!",

}


class SaveGame:

    def __init__(self, name):
        """
        A savegame object for a hangman game which records nickname, number of guesses, whether the game is complete or
        not, whether the game has been won or not, and guessed letters so far.
        :return:
        """
        self.playername = name
        self.game_completed = False
        self.number_of_guesses = 0
        self.game_won = False
        self.letters_guessed = []

    def __str__(self):
        return f"Playername: {self.playername}, Game completed: {self.game_completed}," \
                f"number of guesses: {self.number_of_guesses}, game won: {self.game_won}," \
                f"letters guessed: {self.letters_guessed}"
