import random


def get_random_word_test():
    print(game.get_random_word())
    print(game.get_random_word())
    print(game.get_random_word())


class Game:

    def __init__(self, allowed_attempts: int):
        self.__allowed_attempts = allowed_attempts
        self.__game_word = []

    def get_random_word(self):
        with open('data/WordsStockRus.txt', 'r', encoding='utf8') as file:
            line = file.readlines()
        self.__game_word = list(line[random.randint(0, 11650)].strip())
        return self.__game_word


difficult_game = int(input('Enter the number of available attempts: '))

game = Game(difficult_game)

if __name__ == '__main__':
    get_random_word_test()