class Player:
    def __init__(self, name):
        self.name = name

    def return_name(self):
        return self.name

    def correct(self, coord_1: str, coord_2: str, symbols_used: list, side_1: int, my_field):
        """
        check correct input

        :return:
            True/False
        """
        if not((coord_1 in symbols_used) and (coord_2.isdigit()) and (int(coord_2) > 0) and (int(coord_2)) <= side_1):
            print("Хм... Что-то пошло не так! " + self.name +
                  ", попробуй еще раз ввести координаты через пробел (напрммер:  a 2, c 12)")
            return False
        s = my_field.return_index((symbols_used.index(coord_1) + 1), int(coord_2))
        if '.' not in s:
            print("Тут уже стоит символ. Попробуй другое место!")
            return False
        return True

    def act(self, my_field, symbols_used: list, x_o: chr, side_1: int):
        """ player actions """
        print("Твой ход,", self.name)
        while True:             # checking for the correctness of entering coordinates
            coordinate_1, coordinate_2 = input().split()
            if self.correct(coordinate_1, coordinate_2, symbols_used, side_1, my_field):
                my_field.change_index((symbols_used.index(coordinate_1) + 1), int(coordinate_2), x_o)
                break
