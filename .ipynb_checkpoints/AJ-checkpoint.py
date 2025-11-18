####
# Each team's file must define four tokens:
#      team_name: a string
#      strategy_name: a string
#      strategy_description: a string
#      move: A function that returns 'c' or 'b'
####

# YOUR TEAM DETAILS HERE
team_name = 'AJ' # Only 10 chars displayed.
strategy_name = 'Figth back hard'
strategy_description = 'If attacked, fight back forever (Grim Trigger), except turn 11.'

import random

# YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
    # Check if it is the first turn (index 0) or the 11th turn (index 10)
    if len(my_history) == 0 or len(my_history) == 10:
        return 'c'
    
    # If the opponent has EVER defected (betrayed)
    elif 'b' in their_history:
        return 'b' 
        
    # Otherwise, cooperate
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
    
    # Test 1: First move.
    # Expected: 'c' because len(my_history) is 0.
    if test_move(my_history='',
                 their_history='',
                 my_score=0,
                 their_score=0,
                 result='c'):
        print('Test 1 passed')

    # Test 2: Opponent has NOT betrayed yet.
    # my_history='bbb', their_history='ccc'. 
    # 'b' is NOT in their_history, so we expect 'c'.
    if test_move(my_history='bbb',
                 their_history='ccc',
                 my_score=0,
                 their_score=0,
                 result='c'):
        print('Test 2 passed')
        
    # Test 3: Opponent HAS betrayed previously.
    # 'b' IS in their_history ('cbc'), so we expect 'b'.
    if test_move(my_history='ccc',
                 their_history='cbc',
                 my_score=0,
                 their_score=0,
                 result='b'):
        print('Test 3 passed')