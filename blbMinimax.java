package students.blb;

import java.util.Date;
import edu.ksu.csc.ai.othello.GameState;
import edu.ksu.csc.ai.othello.GameState.Player;
import edu.ksu.csc.ai.othello.OthelloPlayer;
import edu.ksu.csc.ai.othello.Square;

public class blbMinimax extends OthelloPlayer {
	//enter the max depth here, I choose 4 because after it the agent will become very slow
	 public int maxDepth = 4;
	 
	public blbMinimax(String name) {
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
		
		ChoosenMove = minimax_Decision(myGameState, currentScore, validMoves, currentPlayer, currentOpponent);
		
		//return
		this.registerCurrentBestMove(ChoosenMove);
		return ChoosenMove;
	}
	
    public Square minimax_Decision(GameState state, int score, Square[] validMoves, Player currentPlayer, Player currentOpponent)
    {
    	//defince variable for our move and set to null at the start.
		Square ChoosenMove = null;
		
		//define variable to store the score of our choosenMove, set to "-100" at first,
		//because the score could be <0, but not a big minus number like -100.
        int ChoosenMoveScore = -100;
        
        for (int i = 0; i < validMoves.length; i++)
        {
        	//get the state of the move "i"
            GameState temp_state = state.applyMove(validMoves[i]);
            //get the score for this current state.
            int temp_Score = minimaxValue((GameState)temp_state.clone(), 1, score, currentPlayer, currentOpponent);
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
    
    public int minimaxValue(GameState state, int currentDepth, int score, Player currentPlayer, Player currentOpponent)
    {
    	   //check if we finally reach the maxDepth or a state where there the games ends, get the score from heuristic.
    	   if ((currentDepth == maxDepth) || (state.getStatus() != GameState.GameStatus.PLAYING)) 
           {
               return Evaluation(state, score, currentPlayer, currentOpponent);
           }
    	   
    	   //get the possible move in this state.
           Square temp_validMoves[] = state.getValidMoves().toArray(new Square[0]);
           
           //if there are possible moves in this state then
           if((temp_validMoves != null) && (temp_validMoves.length > 0))
           {
               int ChoosenMoveScore = -100;
               for (int i = 0; i < temp_validMoves.length; i++)
               {
                   GameState temp_State = state.applyMove(temp_validMoves[i]);
                   int temp_Score = minimaxValue((GameState)temp_State.clone(), (currentDepth + 1), score, currentPlayer, currentOpponent);
                   
                   //our agent will always consider himself the MAX agent.
                   if (temp_Score > ChoosenMoveScore)
                   {
                	   ChoosenMoveScore = temp_Score;
                   }
               }
               return ChoosenMoveScore;
           }
           else
           {
        	   return minimaxValue(state, currentDepth + 1, score, currentPlayer, currentOpponent);
           }
    }
    
    //simple evaluation function.
    public int Evaluation(GameState state, int old_score, Player currentPlayer, Player currentOpponent)
    {
    	//this will get the diffrence between our agent socre and the opponent aget
    	//therefore our agent will always consider himself the max agent, and the opponent the min agent.
        return (state.getScore(currentPlayer) - state.getScore(currentOpponent));
    }
	
}

 
// GameState <--- to get the state of the board
 
// Square(move) <--- to move 