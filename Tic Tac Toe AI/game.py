# ----------------------------------- Imports -----------------------------------
import numpy as np
from minimax import PlayWithMinimax
from RandomMoveAgent import playRandomMove

# ----------------------------------- Supporting Fucntions -----------------------------------
# To get the move (1-9) from human player.
def play_turn():
    pos = int(input("\n{} turn, which position you want to play? ".format(player_symbol(playerTurn)))) # Enter number from 1 to 9.

    XYposition = get_XYposition(pos) # Get XY Cordinates of this position.
    try:
        if(board[XYposition[0], XYposition[1]] == 0): # If the position is empty play.
            board[XYposition[0], XYposition[1]] = playerTurn 
        else: # If the posision isn't empty ask for another input.
            print("Posision is filled, please choose other posision.")
            play_turn() 
    except IndexError: # Exception when the input position is out of index.
        print("Illgeal move.")
        play_turn()

def bot_turn(chosenMove):
    XYposition = get_XYposition(chosenMove) # Get XY Cordinates of this position.
    board[XYposition[0], XYposition[1]] = playerTurn # No need for checking if posision is avilable, since it was done in by the agent.

# print_table() prints the board in a clear way for the player,
# and shows 1 as X, -1 as O, and 0 (empty fields) as their position number (from 1 to 9)
'''
Example:
Board array print without the function:
 1   0   1
-1   1  -1
-1   1  -1

Board array print with the function:

X  2  X
O  X  O
O  X  O
'''
def print_table(board):
    tempBoard = board
    tempBoard = np.where(board == -1, "O", tempBoard) # Replace -1 with O when printing
    tempBoard = np.where(board == 1, "X", tempBoard) # Replace 1 with X when printing
    
    temp = 1
    for pos in tempBoard: # Print the board with replacing each 0 with the position number, to help to player knowing the inputs.
        for elem in pos:
            if(elem == "0"):
                print("{}".format(temp).rjust(3), end="")
            else:
                print("{}".format(elem).rjust(3), end="")
            temp = temp + 1
        print(end="\n")

# To get the player symbol (1 is X, -1 is O)
def player_symbol(playerTurn):
    if(playerTurn == 1):
        return "X"
    return "O"

# Get position number (1-9) and return the XY Cordinates.
def get_XYposition(position):
    if(position == 1):
        return [0, 0]
    elif(position == 2):
        return [0, 1]
    elif(position == 3):
        return [0, 2]
    elif(position == 4):
        return [1, 0]
    elif(position == 5):
        return [1, 1]
    elif(position == 6):
        return [1, 2]
    elif(position == 7):
        return [2, 0]
    elif(position == 8):
        return [2, 1]
    elif(position == 9):
        return [2, 2]
    else:
        return [3, 3] # Will result in out of index exception.

# ----------------------------------- Mini max Agent -----------------------------------


# ----------------------------------- The main game -----------------------------------
board = np.zeros((3, 3)).astype(int) # board of the game is 3x3 and we can say X is 0, and O is 1.

playerTurn = 1 # player 1 (X) or -1 (O) turn.
avilableMoves = 9 # number of avilable moves, at the start 9.

def check_win():
    if(any(np.sum(board, 1) == 3) or any(np.sum(board, 0) == 3) or (sum(np.diag(board)) == 3) or (sum(np.diag(board[::-1])) == 3)):
        return True
    if(any(np.sum(board, 1) == -3) or any(np.sum(board, 0) == -3) or (sum(np.diag(board)) == -3) or (sum(np.diag(board[::-1])) == -3)):
        return True
    return False

while (avilableMoves > 0):
    print_table(board)
    if(playerTurn == 1):
        play_turn()
    else:
        chosenMove = PlayWithMinimax(board)
        bot_turn(chosenMove)
        print("\nThe has opponent played in position {}".format(chosenMove))
        
    
    if check_win():
        print_table(board)
        print("{} has won!".format(player_symbol(playerTurn)))
        input("")
        break
    playerTurn = playerTurn *-1
    avilableMoves = avilableMoves - 1

if(avilableMoves <= 0):
    print_table(board)
    print("Tie")
    input("")