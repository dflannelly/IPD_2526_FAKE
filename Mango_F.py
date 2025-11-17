####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


#YOUR TEAM DETAILS HERE
team_name = 'Mango' # Only 10 chars displayed.
strategy_name = 'The All C strategy'
strategy_description = 'It always chooses to cooperate ('c') on every single round of the game, no matter what the opponent does. It does not betray.'

import random



#YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
	
def my_simple_strategy(my_history, their_history):

    if len(my_history) == 0:
    
        return 'c' 
    else:
        
        return 'c'

def always_cooperate_opponent(my_history, their_history):
    
    return 'c'

def calculate_score(move1, move2):
    # Scoring: (My Score, Opponent's Score)
    # C/C: (3, 3) - Best for both
    # C/B: (0, 5) - I lose, they win
    # B/C: (5, 0) - I win, they lose
    # B/B: (1, 1) - Both lose a bit
    
    if move1 == 'c' and move2 == 'c': return 3, 3
    if move1 == 'c' and move2 == 'b': return 0, 5
    if move1 == 'b' and move2 == 'c': return 5, 0
    if move1 == 'b' and move2 == 'b': return 1, 1
    return 0, 0 

def run_simulation(strategy1, strategy2, rounds=5):
   
    history1, history2 = [], []
    score1, score2 = 0, 0

    print("--- Simulation Start (My simple strategy vs friendly opponent) ---")
    print("-" * 35)

    for i in range(rounds):
        
        move1 = strategy1(history1, history2)
        move2 = strategy2(history2, history1)

    
        s1_round_score, s2_round_score = calculate_score(move1, move2)
        score1 += s1_round_score
        score2 += s2_round_score
        history1.append(move1)
        history2.append(move2)

        print(f"Round {i+1}: My Move ({move1}) vs. Opponent Move ({move2}) | Scores: {s1_round_score}-{s2_round_score}")

    print("-" * 35)
    print(f"Total Score (My Strategy): {score1}")
    print(f"Total Score (Opponent): {score2}")
    print("--- Simulation Complete ---")


run_simulation(my_simple_strategy, always_cooperate_opponent, rounds=5)

          
