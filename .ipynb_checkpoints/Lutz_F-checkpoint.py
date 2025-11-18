####
# Each team's file must define four tokens:
#      team_name: a string
#      strategy_name: a string
#      strategy_description: a string
#      move: A function that returns 'c' or 'b'
####

team_name = 'MasonTeam_F' 
strategy_name = 'Grim Trigger'
strategy_description = 'Cooperate until betrayed once, then betray forever.'

import random

# YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score): 
    # Check if it's the first move
    if len(my_history) == 0:
        return 'c'

    # If the opponent has EVER betrayed you
    elif 'b' in their_history:
        return 'b'
        
    # If they have 'c' (and no 'b' because of the check above)
    elif 'c' in their_history:
        return 'c'
        
    # Default fallback
    else:
        return 'c'

def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.
    '''
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

    # Test 2: They betrayed in the past ('b' is in history).
    # Your logic says if 'b' is in history, return 'b'.
    if test_move(my_history='ccc',
              their_history='cbb', 
              my_score=0, 
              their_score=0,
              result='b'):
        print('Test 2 passed')
        
    # Test 3: They have never betrayed.
    if test_move(my_history='ccc',
              their_history='ccc', 
              my_score=0, 
              their_score=0,
              result='c'):
        print('Test 3 passed')
