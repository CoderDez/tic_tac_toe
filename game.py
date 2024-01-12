import os


class TicTacToe:
    def __init__(self):
        self.__player1 = self.__player2 = ""
        self.__won = False
        self.__turns = 0
        self.__winner = None
        self.__board = [" " for i in range(9)]

    def play(self):
        try:
            self.__announce_game()
            self.__get_player_names()
            self.__clear_console()
            self.__announce_game()
            self.__announce_contestants()
            self.__start_game()
            self.__show_result()

        except KeyboardInterrupt:
            print("\n\nYou ended the game!")
            exit(0)
        except Exception as e:
            print("\n\nSomething has went wrong: ", e)


    def __announce_game(self):
        game_name = "TIC TAC TOE"
        print(f"\n{game_name}")
        print("-" * len(game_name), end="\n\n")

    def __announce_contestants(self):
        print(f"{self.__player1} versus {self.__player2}!",end="\n\n")


    def __clear_console(self):
        os.system("cls" if os.name == "nt" else "clear")

    
    def __get_player_names(self):
        self.__player1 = self.__get_name(1)
        self.__player2 = self.__get_name(2)


    def __get_name(self, player_num: int):
        name = ""

        while not name.isalnum() or len(name) > 12:
            name = input(f"Enter name for player{player_num}: ")

            if not name.isalnum():
                print(f"Invalid name! names must be alphanumeric, try again...")
            elif len(name) > 12:
                print("Invalid name! names must be 12 characters long or less, try again...")

        return name
    

    def __start_game(self):
        
        while not self.__won and self.__turns < 9:
            self.__display_board()

            player = self.__player1 if self.__turns % 2 == 0 else self.__player2
            space = self.__have_turn(player)
            char = "X" if player == self.__player1 else "O"
            self.__change_space(space-1, char)

            self.__turns +=1

            if self.__turns >= 5:
                self.__check_for_win()


        self.__display_board()


    def __check_for_win(self):

        for i in range(0, 3):
            # row check
            row = self.__board[i * 3: (i*3) + 3]

            if row.count("X") == 3:
                self.__winner = self.__player1

            elif row.count("O") == 3:
                self.__winner = self.__player2

            # col check
            if not self.__winner:
                col = [self.__board[i], self.__board[i+3], self.__board[i+6]]

                if col.count("X") == 3:
                    self.__winner = self.__player1

                elif col.count("O") == 3:
                    self.__winner = self.__player2

            # diagonal check
            if not self.__winner:
                if i % 2 == 0:
                    adder = 4 if i == 0 else 2
                    diagonal = [self.__board[i], self.__board[i+adder], self.__board[i+(adder*2)]]

                    if diagonal.count("X") == 3:
                        self.__winner = self.__player1

                    elif diagonal.count("O") == 3:
                        self.__winner = self.__player2


            if self.__winner:
                self.__won = True
                break


                

    def __have_turn(self, player: str):
        chosen_valid = False

        while not chosen_valid:
            space = input(f"{player}, Enter space (1-9): ")

            if space.isdigit() and len(space) == 1:
                space = int(space)

                if space >= 1 and space <= 9:
                    chosen_valid = self.__is_space_available(space-1)

            if not chosen_valid:
                print("Invalid space!")

        return space
    

    def __is_space_available(self, space: int):
        return self.__board[space].isspace()

            
    def __change_space(self, space: int, char: str):
        self.__board[space] = char


    def __display_board(self):
        board_display = ""
        dash_line = "-" * 13 + "\n"
        board_display += dash_line

        for i in range(0, 3):
            entry = ""
            row = self.__board[i * 3: (i*3) + 3]

            for space in row:
                entry += f"| {space} "

            entry += "|\n"
            board_display += entry
            board_display += dash_line

        print(board_display)

    
    def __show_result(self):
        if self.__winner:
            print(f"\n\n{self.__winner} won!")
        else:
            print("Draw!")




if __name__ == "__main__":
    game = TicTacToe()
    game.play()

        








