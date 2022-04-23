'''
Minimax agent uses minimax to choose the best move from 1 to 9 in tic tac toe.
'''
# ----------------------------------- Imports -----------------------------------
import numpy as np
from sqlalchemy import null

# ----------------------------------- Supporting Fucntions -----------------------------------

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

# Aplly a move and return the board after.
def applyMove(move, board, playerTurn):
    XYposition = get_XYposition(move) # Get XY Cordinates of this position.
    tempBoard = np.array(board, copy=True)
    tempBoard[XYposition[0], XYposition[1]] = playerTurn # No need for checking if posision is avilable, since it was done in by the agent.
    return tempBoard # return the temp board

# ----------------------------------- Mini max Agent -----------------------------------

# gives positive value is max win, negative value if max lose, or 0 when tied.
# returns natural, negative, or positive.
def Evaluate(board):
    if(any(np.sum(board, 1) == -3) or any(np.sum(board, 0) == -3) or (sum(np.diag(board)) == -3) or (sum(np.diag(board[::-1])) == -3)):
        return 100 # If O (agent) wins

    if(any(np.sum(board, 1) == 3) or any(np.sum(board, 0) == 3) or (sum(np.diag(board)) == 3) or (sum(np.diag(board[::-1])) == 3)):
        return -100 # If X (player) wins
        
    if(any(np.sum(board, 1) == -2) or any(np.sum(board, 0) == -2) or (sum(np.diag(board)) == -2) or (sum(np.diag(board[::-1])) == -2)):
        return 10 # If O (agent) wins

    if(any(np.sum(board, 1) == 2) or any(np.sum(board, 0) == 2) or (sum(np.diag(board)) == 2) or (sum(np.diag(board[::-1])) == 2)):
        return -10 # If X (player) wins

    if(any(np.sum(board, 1) == -1) or any(np.sum(board, 0) == -1) or (sum(np.diag(board)) == -1) or (sum(np.diag(board[::-1])) == -1)):
        return 10 # If O (agent) wins

    if(any(np.sum(board, 1) == 1) or any(np.sum(board, 0) == 1) or (sum(np.diag(board)) == 1) or (sum(np.diag(board[::-1])) == 1)):
        return -1 # If X (player) wins

    return 0

    '''
    .......................................Evaluation function can be improved.......................................
        score = 0
    score = score + sum(np.sum(board, 1) == -3) + sum(np.sum(board, 0) == -3) + sum((np.diag(board)) == -3) + sum(np.diag(board[::-1]) == -3) * 100
    score = score + sum(np.sum(board, 1) == -2) + sum(np.sum(board, 0) == -2) + sum((np.diag(board)) == -2) + sum(np.diag(board[::-1]) == -2) * 10
    score = score + sum(np.sum(board, 1) == -1) + sum(np.sum(board, 0) == -1) + sum((np.diag(board)) == -1) + sum(np.diag(board[::-1]) == -11) * 1

    score = score - sum(np.sum(board, 1) == 3) + sum(np.sum(board, 0) == 3) + sum((np.diag(board)) == 3) + sum(np.diag(board[::-1]) == 3) * 100
    score = score - sum(np.sum(board, 1) == 2) + sum(np.sum(board, 0) == 2) + sum((np.diag(board)) == 2) + sum(np.diag(board[::-1]) == 2) * 10
    score = score - sum(np.sum(board, 1) == 1) + sum(np.sum(board, 0) == 1) + sum((np.diag(board)) == 1) + sum(np.diag(board[::-1]) == 1)

    return score
    '''

# The Minimax function checks the score by calling to evaluate the function
def minimax(board, cureentDepth, playerTurn):
    maxDepth = 5
    scores = 0
    if(Evaluate(board) != 0 or cureentDepth == maxDepth): # Stop when reaching max depth or if the game has ended.
        return Evaluate(board)

    validMoves = getValidMoves(board) # List of valid moves for the temp board
    if(len(validMoves) > 0): # If there is valid moves then
        ChoosenMoveScore = 0
        for i in validMoves:
            temp_state = applyMove(i, np.array(board, copy=True), playerTurn)
            temp_score = minimax(temp_state, cureentDepth+1, playerTurn*-1)
            if(playerTurn == -1):
                if(temp_score > ChoosenMoveScore):
                    ChoosenMoveScore = temp_score
                else:
                    if(temp_score < ChoosenMoveScore):
                        ChoosenMoveScore = temp_score
        return ChoosenMoveScore
    else:
        return minimax(np.array(board, copy=True), cureentDepth+1, playerTurn*-1)
    
# FindBestMove return the board and add the best move on the board
def FindBestMove(board, validMoves):
    bestMove = null
    bestMoveScore = -999

    for i in validMoves:
        temp_state = applyMove(i, np.array(board, copy=True), -1)
        temp_score = minimax(temp_state, 1, -1)

        if(temp_score > bestMoveScore):
            bestMove = i
            bestMoveScore = temp_score
    return bestMove

# This function sum up all the functions in this project
def PlayWithMinimax(board):
    validMoves = getValidMoves(board) # List of valid moves for the original board

    tempBoard = np.array(board, copy=True)
    choosenMove = FindBestMove(tempBoard, validMoves)
    return choosenMove