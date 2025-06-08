board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

def display_board():
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

game_still_going = True

winner = None

current_player = "x"
def play_game():
    display_board()
    while game_still_going:
        handle_chance(current_player)
        check_if_game_over()
        flip_player()



def handle_chance(player):
    print(player + " s turn")
    position = input("enter position")
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("wrong input")
        position=int(position)-1
        if board[position]=="_":
            valid=True
        else:
            print("cannt go there")
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
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
        winner=None
    return

def check_rows():
    global game_still_going
    row_1 = board[0]==board[1]==board[2]!="_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    col_1=board[0]==board[3]==board[6]!="_"
    col_2 = board[1] == board[4] == board[7]!="_"
    col_3 = board[2] == board[5] == board[8]!="_"
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diag_1 = board[0]==board[4]==board[8]!="_"
    diag_2 = board[2]==board[4]==board[6]!="_"
    if diag_1 or diag_2:
        game_still_going=False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going=False
    return

def flip_player():
    global current_player
    if current_player == "x":
        current_player="0"
    elif current_player == "0":
        current_player = "x"
    return

play_game()
if winner=="x" or winner=="0":
    print(winner + " won the game")
elif winner==None:
    print("tie")