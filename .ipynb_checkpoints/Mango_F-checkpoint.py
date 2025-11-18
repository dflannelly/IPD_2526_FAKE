####
# Each team's file must define four tokens:
#      team_name: a string
#      strategy_name: a string
#      strategy_description: a string
#      move: A function that returns 'c' or 'b'
####

team_name = 'Mango' 
strategy_name = 'The All C strategy'
# FIXED: Used double quotes " " on the outside so you can use single quotes ' ' inside.
strategy_description = "It always chooses to cooperate ('c') on every single round."

import random

# YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
    # This is the only line you need for an 'All C' strategy
    return 'c'

# ------------------------------------------------------------------
# The code below acts as a sanity check to make sure your code runs.
# It replaces the complex simulation code you had before.
# ------------------------------------------------------------------
def test_move(my_history, their_history, my_score, their_score, result):
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: First move should be 'c'
    if test_move(my_history='',
              their_history='',
              my_score=0,
              their_score=0,
              result='c'):
         print('Test 1 passed')

    # Test 2: Even if they betray, we still cooperate (because we are "All C")
    if test_move(my_history='c',
              their_history='b', 
              my_score=0, 
              their_score=0,
              result='c'):
        print('Test 2 passed')