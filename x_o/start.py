# getting start values + interactive

import random

from player import Player
from field import Field


def name():
    """ get names """
    print("Хэй! Хотите поиграть в крестики-нолики? (:")
    name_1 = input("Введите имя первого игрока (он будет играть 'крестиками') ")
    name_2 = input("Введите имя второго игрока (он будет играть 'ноликами') ")
    return name_1, name_2


def side():
    """
    requesting the sides of the field

    :return:
        height, width
    """
    while True:
        side_1, side_2 = map(int, input("Введите стороны поля через пробел ").split())
        if side_2 <= 702:                # format a, b, ..., z, aa, ab... (max = 27 * 25 = 702)
            return side_1, side_2
        print("Вы что дикие? Давайте числа поменьше))")


def randomise(name1: str, name2: str):
    """
    determine the first move

    :return:
        False, if first cross
        True, if first zero
    """
    while True:
        print(name1 + ", нажми Enter и мы выведем для тебя 2 случайных числа :)", end='')
        something = input()
        number1, number2 = random.randint(1, 6), random.randint(1, 6)
        print(number1, number2)

        print(name2 + ", теперь ты :)", end='')
        something = input()
        number3, number4 = random.randint(1, 6), random.randint(1, 6)
        print(number3, number4)

        if (number1 + number2) > (number3 + number4):
            print(name1 + ", твоя сумма чисел больше. Твой ход первый!")
            return False
        elif (number1 + number2) < (number3 + number4):
            print(name2 + ", твоя сумма чисел больше. Твой ход первый!")
            return True
        else:
            print("Ой, ваша сумма чисел одинаковая... Давайте попробуем снова!")
            print()


def start():
    """ get start values + determine the first move"""
    name_1, name_2 = name()
    player_1 = Player(name_1)
    player_2 = Player(name_2)
    side_1, side_2 = side()
    my_field = Field(side_1, side_2)
    my_field.initialization_field()

    length_win = min(side_1, side_2)  # length of a winning position
    print("Для выигрыша, необходимо построить последовательсть из своих символов длиной", length_win,
          "на этой доске по вертикали, горизонтали или диагонали. Удачи!")
    my_field.print_field()
    print("Чтобы поставить символ на нужную позицию напишите её координаты через пробел(например: a 1, c 12)")
    print()
    print("Решим, кто будет ходить первый, с помощью рандома!")
    zeroes_move = randomise(name_1, name_2)  # move (0 - crosses; 1 - zeroes)
    symb = my_field.return_symbols()

    return my_field, player_1, player_2, zeroes_move, side_1, side_2, symb, length_win
