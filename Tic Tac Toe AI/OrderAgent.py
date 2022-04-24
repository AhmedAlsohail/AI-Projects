'''
Order agent plays 1, 2, 3, ..., 9 in order and skips unvalid moves.
'''
import numpy as np

# Return a list of valid moves
def getValidMoves(board):
    tempBoard = board
    tempBoard = np.where(board == -1, "O", tempBoard) # Replace -1 with O when printing
    tempBoard = np.where(board == 1, "X", tempBoard) # Replace 1 with X when printing
    validMoves = []
    temp = 1
    for pos in tempBoard: # Add the positions (1-9) of valid moves (not X nor O).
        for elem in pos:
            if(elem == "0"):
                validMoves.append(temp)
            temp = temp + 1
    return validMoves

# Return the next avilable move.
def playOrderMove(board):
    validMoves = getValidMoves(board)
    nextMove = min(validMoves)
    return nextMove