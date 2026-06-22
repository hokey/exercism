"""
Hangman FRP
"""

# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    """
    Hangman FRP
    """
    def __init__(self, word):
        """
        Initialize the Hangman class
        :param word: The word to guess
        """
        self.remaining_guesses: int = 9
        self.status: str = STATUS_ONGOING
        self.guessed_letters: set[str] = set()
        self.word: str = word.lower()

    def guess(self, char:str) -> None:
        """
        Guess a letter
        :param str char: The letter to guess
        :return None:
        """
        char = char.lower()

        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        if self.remaining_guesses == 0:
            self.guessed_letters.add(char)

            if "_" not in self.get_masked_word():
                self.status = STATUS_WIN
            else:
                self.status = STATUS_LOSE
            return

        if char not in self.word or char in self.guessed_letters:
            self.remaining_guesses -= 1
        else:
            self.guessed_letters.add(char)

        if "_" not in self.get_masked_word():
            self.status = STATUS_WIN

    def get_masked_word(self):
        """
        Get the masked word
        :return: The masked word
        """
        return "".join([character if character in self.guessed_letters else "_" for character in self.word])

    def get_status(self):
        """
        Get the status of the game
        :return str: The status of the game
        """
        return self.status
