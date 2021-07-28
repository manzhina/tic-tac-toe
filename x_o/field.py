class Field:
    def __init__(self, side_1: int, side_2: int):
        self.width = side_2
        self.height = side_1
        self.field = [['' for i in range(self.height + 1)] for j in range(self.width + 1)]
        self.k_letters = self.width
        self.current_line = 1
        self.symbols_used = []      # left column values
        self.symbols = [chr(i) for i in range(96, 123)]        # symbols of the English alphabet
        self.symbols[0] = ' '
        self.row = ''  # possibly a winning line

    def initialization_field(self):
        for i in range(self.width + 1):
            for j in range(self.height + 1):
                if j < 10:
                    self.field[i][j] = '.'
                elif j < 100:
                    self.field[i][j] = '. '
                else:
                    self.field[i][j] = ' . '

        self.field[0][0] = '  '

        for i in range(1, self.height + 1):
            self.field[0][i] = i

        for i in range(len(self.symbols)):
            for j in range(1, len(self.symbols)):
                self.field[self.current_line][0] = self.symbols[i] + self.symbols[j]
                if self.symbols[i] != ' ':                                          # without spaces
                    self.symbols_used.append(self.symbols[i] + self.symbols[j])
                else:
                    self.symbols_used.append(self.symbols[j])
                self.current_line += 1
                self.k_letters -= 1
                if self.k_letters == 0:
                    return

    def print_field(self):
        for line in self.field:
            print(*line)

    def return_symbols(self):
        return self.symbols_used

    def return_field(self):
        return self.field

    def return_index(self, i: int, j: int):
        return self.field[i][j]

    def change_index(self, i: int, j: int, change_symbol: chr):
        self.field[i][j] = self.field[i][j].replace('.', change_symbol)

    def win_str(self, row: str, win_row: str):
        """
        check for a winning line

        :return:
            True, if winning
        """
        k = 0
        while k != (len(self.row) - 1):  # removing spaces from a string
            if row[k] == ' ':
                row = row[:k] + row[(k + 1):]
            k += 1

        if self.row.find(win_row) != -1:
            return True

    def win_d(self, win_row: str, condition_flag_1: bool, k_flag: bool,
              side_flag_1: int, flag_j: bool, condition_2: int):
        """
        check winnings diagonal

        :return:
            True, if the win
        """
        min_side = min(self.width, self.height)
        for i in range(1, condition_2 - min_side + 2):
            if k_flag:
                j = 1
            else:
                j = side_flag_1
            k = i
            while k <= condition_2:
                if (condition_flag_1 and (j <= 0)) or (not condition_flag_1 and (j > side_flag_1)):
                    break
                if flag_j:
                    self.row += str(self.field[k][j])
                else:
                    self.row += str(self.field[j][k])
                k += 1
                if k_flag:
                    j += 1
                else:
                    j -= 1
            if self.win_str(self.row, win_row):
                return True

    def win_v_g(self, win_row: str, condition_1: int, condition_2: int, flag_i_j: bool):
        """
        check winnings vertically and horizontally

        :return:
            True, if the win
        """
        for i in range(1, condition_1 + 1):
            self.row = ''            # possibly a winning line
            for j in range(1, condition_2 + 1):
                if flag_i_j:
                    self.row += str(self.field[i][j])
                else:
                    self.row += str(self.field[j][i])
            if self.win_str(self.row, win_row):
                return True

    def win(self, win_row: str):
        """
        check winnings

        :return:
            True, if the win
        """
        if self.win_v_g(win_row, condition_1=self.width, condition_2=self.height, flag_i_j=True)\
                or self.win_v_g(win_row, condition_1=self.height, condition_2=self.width, flag_i_j=False):
            return True

        if self.win_d(win_row, condition_flag_1=False, k_flag=True,
                      side_flag_1=self.height, flag_j=True, condition_2=self.width)\
                or self.win_d(win_row, condition_flag_1=True, k_flag=False,
                              side_flag_1=self.height, flag_j=True, condition_2=self.width)\
                or self.win_d(win_row, condition_flag_1=False, k_flag=True,
                              side_flag_1=self.width, flag_j=False, condition_2=self.height)\
                or self.win_d(win_row, condition_flag_1=True, k_flag=False,
                              side_flag_1=self.width, flag_j=False, condition_2=self.height):
            return True
