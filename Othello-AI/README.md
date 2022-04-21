# Othello-Agents
## Introduction
The project is about implementing two AI agent of for othello reversi which is a strategy board game for two players playing on 8x8 uncheckered board it was invented in 1883, the first AI agent is using the MiniMax method to make a play and the other is using the alphabet method to make a play.

This project is focusing on measuring the preformance and speed of two agents playing Othello, but first what is Othello?

Othello or reverse  is a strategy board game for two players, played on an 8×8 uncheckered board. It was invented in 1883. Othello, a variant with a change to the board's initial setup, was patented in 1971.


Jumping back to the project which will measure the two agents (MiniMax, AlphaBeta) and compare which strategy is best.


##	The problem
The two agents (MiniMax, AlphaBeta) will be implemented with Java, then biding them against a random AI to measure the preformance and speed of the agents, next step will be biding the two agents against each other and gather the result.

##	Results
Both Minimax and Alphabeta agents has won against random (further details below).

##	Evaluation Function
Our evaluation function is very simple, it takes the score of our player and the score of the opponent,
And return "Agent player score – opponent player score".

In the “Minimax algorithm” our agent will always consider itself the “MAX”, and in the same with “AlphaBeta algorithm” it considers itself the “Alpha”.

So the more score our evaluation function get the better.
 
##	Data structure
The data structure used for both agents is array list for it’s easy and fast approach.
 
##	Agents Performance
The performance of the two agents was tested by making each of them play 10 games against the Random Agent, which plays random move each round, and the results was as follows:

### blbMinimax vs Random Agent:
Against the Random Agent, this agent has won 8 games, tie in 1, and lost 1 game:

![image](https://user-images.githubusercontent.com/62726823/155143618-c83b8d30-3a55-4953-bf61-dcd492173d7b.png)


### blbAlphaBeta vs Random Agent:
Against the Random Agent, this agent has won 7 games , and lost 3 games against RandomOthelloPlayer

![image](https://user-images.githubusercontent.com/62726823/155143691-573fe601-2c6a-477e-adfc-e27292580fa4.png)

### blbMinimax vs blbAlphaBeta
and for the final match we but blbMiniMax against blbAlphabeta, and the results were very interesting, 

![image](https://user-images.githubusercontent.com/62726823/155143217-440bc521-98db-4819-b244-05a270a74e85.png)

When MiniMax was player 1, it won 4 games and lost 1 game

But when MiniMax was player 2, it won 1 game, and lost 4 games against AlphaBeta.

## Conclusion
If we paid close attention to the match between Minimax and AlphaBeta we notice there were 4 results similar to each other, that’s due the implementation we followed, and how Minimax will always go as max, and AlphaBeta will always go as alpha, which resulted in similar results, in the end we got that the agent which play first will win 80% of the time against the other.
