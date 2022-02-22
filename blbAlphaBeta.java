package students.blb;

import java.util.Date;
import edu.ksu.csc.ai.othello.GameState;
import edu.ksu.csc.ai.othello.OthelloPlayer;
import edu.ksu.csc.ai.othello.Square;
import edu.ksu.csc.ai.othello.GameState.Player;

public class blbAlphaBeta extends OthelloPlayer {
	//enter the max depth here, I choose 4 because after it the agent will become very slow
	public int maxDepth = 4;

    public blbAlphaBeta(String name) {
        super(name);
    }


	public Square getMove(GameState currentState, Date deadline) {
		//array of all valid moves
		Square validMoves[] = currentState.getValidMoves().toArray(new Square[0]);
		
		//the move I will return, make it null at first
		Square ChoosenMove = null;
		
		//if the list is empty, then return the ChoosenMove as null.
		if(validMoves == null) {
			//m
			this.registerCurrentBestMove(ChoosenMove);
			return ChoosenMove;
		}
			
		
		GameState myGameState = (GameState)currentState.clone();
		
		//set variables for the current player and his opponent
		Player currentPlayer = myGameState.getCurrentPlayer();
		Player currentOpponent = myGameState.getOpponent(currentPlayer);
		
		//gives you the score on this state.
		int currentScore = myGameState.getScore(currentPlayer);
		
		ChoosenMove = alphabeta_Decision(myGameState, currentScore, validMoves, currentPlayer, currentOpponent);
		
		//return
		this.registerCurrentBestMove(ChoosenMove);
		return ChoosenMove;
	}

    public Square alphabeta_Decision(GameState state, int score, Square[] validMoves, Player currentPlayer, Player currentOpponent)
    {
    	//define variable for our move and set to null at the start.
		Square ChoosenMove = null;
		
		//define variable to store the score of our choosenMove, set to "-100" at first,
		//because the score could be <0, but not a big minus number like -100.
        int ChoosenMoveScore = -100;
        
        for (int i = 0; i < validMoves.length; i++)
        {
        	//get the state of the move "i"
            GameState temp_state = state.applyMove(validMoves[i]);
            //get the score for this current state.
            int temp_Score = alphabeta_Value((GameState)temp_state.clone(), 1, score,  Integer.MIN_VALUE, Integer.MAX_VALUE, currentPlayer, currentOpponent);
            //check if it's the best one yet.
            if (temp_Score > ChoosenMoveScore)
            {
            	//update the ChoosenMove and it's score.
                ChoosenMove = validMoves[i];
            	ChoosenMoveScore = temp_Score;
            }
        }
		return ChoosenMove;
    }

    public int alphabeta_Value(GameState state, int currentDepth, int alpha, int beta, int score, Player currentPlayer, Player currentOpponent) {
        if ((currentDepth == maxDepth) || (state.getStatus() != GameState.GameStatus.PLAYING)) 
        {
            return Evaluation(state, score, currentPlayer, currentOpponent);
        }
        
        Square temp_validMoves[] = state.getValidMoves().toArray(new Square[0]);
        
        if ((temp_validMoves != null) || (temp_validMoves.length > 0))
        {
            for (int i = 0; i < temp_validMoves.length; i++) 
            {
                GameState temp_State = state.applyMove(temp_validMoves[i]);
                
                int temp_Score = alphabeta_Value((GameState)temp_State.clone(), currentDepth + 1,
                		alpha, beta, score, currentPlayer, currentOpponent);
                
                if (temp_State.getCurrentPlayer() == currentPlayer)
                {   //if the current player is our player check the alpha
                    if (temp_Score > alpha)
                    {
                        alpha = temp_Score;
                    }
                } 
                else
                {   //else check the beta
                    if (temp_Score < beta)
                    {
                        beta = temp_Score;
                    }
                }
            }
            //our agent always consider himself "alpha" so we will return the best move for "alpha"
                return alpha;
        } 
        else 
        {
            return alphabeta_Value(state, currentDepth + 1, alpha, beta, score, currentPlayer, currentOpponent);
        }
    }
    
    //simple evaluation function.
    public int Evaluation(GameState state, int old_score, Player currentPlayer, Player currentOpponent)
    {
    	//this will get the diffrence between our agent socre and the opponent aget
    	//therefore our agent will always consider himself the "Alpha" agent, and the opponent the "Beta" agent.
        return (state.getScore(currentPlayer) - state.getScore(currentOpponent));
    }
}


//GameState <--- to get the state of the board

//Square(move) <--- to move 