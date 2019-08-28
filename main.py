game_still_going = True
winner = None
current_player = "X"

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

def print_board():
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

def play_game():
    print_board()
    while game_still_going:

        handle_turn(current_player)
        check_game()
        #flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner==None:
        print("Tie")

def check_game():
    check_win()
    check_tie()

def check_win():
    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner
    return

def check_rows():
    global game_still_going

    # checking each row for winner when the game is still going
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"

    #if one of the row is true, stop the game by making it "False"
    #print the row whether it is X or O winner
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]

    return

def check_columns():
    global game_still_going

    # checking each row for winner when the game is still going
    column1 = board[0] == board[3] == board[6] != "_"
    column2 = board[1] == board[4] == board[7] != "_"
    column3 = board[2] == board[5] == board[8] != "_"

    # if one of the column is true, stop the game by making it "False"
    # print the column whether it is X or O winner
    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return

def check_diagonals():
    global game_still_going

    # checking each diagonals for winner when the game is still going
    diagonal1 = board[0] == board[4] == board[8] != "_"
    diagonal2 = board[2] == board[4] == board[6] != "_"

    # if one of the diagonal is true, stop the game by making it "False"
    # print the diagonal whether it is X or O winner
    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return

def check_tie():
    global game_still_going

    if "_" not in board:
        game_still_going = False

    return

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return current_player

def handle_turn(player):
    global current_player
    print(player + "'s turn: ")

    position = input("Choose a position from 1 - 9: ")

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid position. Try again: ")

    position = int(position) - 1

    if board[position] != "_":
        print(f"Slot #{position + 1} is filled. Try again: ")
    else:
        board[position] = player
        flip_player()
        print_board()

play_game()
