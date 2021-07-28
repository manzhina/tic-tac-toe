from start import start


def win_player(name_win, name_second):
    """ conclusion of the winner """
    print("Поздравляю, " + name_win.return_name() + ", ты победил!")
    print("Не расстраивайся, " + name_second.return_name() + " В следующий раз победа будет за тобой!")


def current_game(my_field, name_1, name_2, zeroes_move: bool, side_1: int, side_2: int, symb: list, length_win: int):
    win_row_1 = 'x' * length_win
    win_row_2 = 'o' * length_win
    k_act = side_1 * side_2         # number of possible moves
    while not (my_field.win(win_row_1)) and not (my_field.win(win_row_2)):
        if zeroes_move:
            name_2.act(my_field, symb, 'o', side_1)
        else:
            name_1.act(my_field, symb, 'x', side_1)
        if k_act == 0:
            print("Ничья! Потная игра выдалась, а вы молодцы!")
            return False
        k_act -= 1
        my_field.print_field()
        zeroes_move = not zeroes_move
    return True


def main():
    my_field, name_1, name_2, zeroes_move, side_1, side_2, symb, length_win = start()
    if current_game(my_field, name_1, name_2, zeroes_move, side_1, side_2, symb, length_win):
        if zeroes_move:
            win_player(name_2, name_1)
        else:
            win_player(name_1, name_2)


main()
