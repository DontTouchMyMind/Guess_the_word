import random


class Game:

    def __init__(self, allowed_attempts: int):
        self.__allowed_attempts = allowed_attempts
        self.__game_word = []
        self.__player_word = []

    def get_random_word(self):
        """
        The method reads data-file and returns hidden random word from data-file.
        :return: type:list; random word.
        """
        with open('data/WordsStockRus.txt', 'r', encoding='utf8') as file:
            line = file.readlines()
        self.__game_word = list(line[random.randint(0, 11650)].strip())
        return self.__game_word

    def guess_letter(self, letter: str):
        """
        The method gets a letter and checks for its presence in the hidden word.
        If player make mistake, then the number of allowed attempts will decrease.
        :param letter: type:str; player letter.
        """
        self.__player_word.append(letter)
        if letter not in self.__game_word:
            self.__allowed_attempts -= 1

    def get_used_letters(self):
        """
        The method displays sorted list of used letters.
        :return: type:list; sorted list of used letters.
        """
        return sorted(set(self.__player_word))

    def get_visible_word(self):
        """
        The method displays current state of the game.
        :return: type:list; list with hidden and guessed letters.
        """
        return list(letter if letter in self.__player_word else '_' for letter in self.__game_word)

    @property
    def allowed_attempts(self):
        return self.__allowed_attempts


difficult_game = int(input('Enter the number of available attempts: '))

game = Game(difficult_game)
