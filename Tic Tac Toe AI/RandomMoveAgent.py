'''
Randomized agent used to measure the quality of other agents.
'''
import numpy as np
import random

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

# Return a random move from the valid moves.
def playRandomMove(board):
    validMoves = getValidMoves(board)
    random_move = random.choice(validMoves)
    return random_move