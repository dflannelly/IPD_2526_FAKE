####
# Each team's file must define four tokens:
#      team_name: a string
#      strategy_name: a string
#      strategy_description: a string
#      move: A function that returns 'c' or 'b'
####

team_name = 'Team 25'
strategy_name = 'Randomized Threshold'
strategy_description = 'Prints debug info and chooses randomly based on opponent betrayal frequency.'

import random

# YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
    # "Strategy with printed output + randomness."
    
    high_count = 0
    
    # NOTE: In this game, history is a string like 'cbcbb', not a list of numbers.
    # We will treat 'b' (betray) as the "high" value/significant event.
    
    print("Analyzing opponent history:", their_history)

    for past_move in their_history:
        print("Checking move:", past_move)
        if past_move == 'b':
            print(" -> This is a betrayal (High)!")
            high_count += 1

    print("Total betrayals (high numbers):", high_count)
  
    random_choice_if_high = random.choice(['b', 'c'])
    random_choice_if_low = random.choice(['b', 'c'])
  
    # Check if more than half the moves were betrayals
    # We use len(their_history) to get the total count of moves
    if len(their_history) > 0 and high_count > len(their_history) / 2:
        print("More than half were betrayals -> Random choice:", random_choice_if_high)
        return random_choice_if_high
    else:
        print("Half or fewer were betrayals -> Random choice:", random_choice_if_low)
        return random_choice_if_low

# ------------------------------------------------------------------
# Testing Code
# ------------------------------------------------------------------
def test_move(my_history, their_history, my_score, their_score, result):
    real_result = move(my_history, their_history, my_score, their_score)
    # Since your result is random, we mainly just want to see that it didn't crash
    # and that it returned a valid move ('b' or 'c').
    if real_result == 'c' or real_result == 'b':
        return True
    else:
        print("Error: move() returned " + str(real_result) + " which is not 'c' or 'b'")
        return False

# This block ONLY runs if you run this file directly.
# It does NOT run when the tournament imports this file.
if __name__ == '__main__':
     
    # Test 1: Check behavior with history 'cbcc'
    # 'b' is the "High" number.
    print("--- Running Test 1 ---")
    test_move(my_history='',
              their_history='cbcc', 
              my_score=0, 
              their_score=0,
              result='c') 
    
    print("\n--- Running Test 2 (Empty history) ---")
    test_move(my_history='',
              their_history='', 
              my_score=0, 
              their_score=0,
              result='c')