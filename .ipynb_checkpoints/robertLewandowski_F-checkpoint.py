####
# Each team's file must define four tokens:
#      team_name: a string
#      strategy_name: a string
#      strategy_description: a string
#      move: A function that returns 'c' or 'b'
####

team_name = 'robertLewandowski'
strategy_name = 'sneaky cooperator'
strategy_description = 'cooperates until 3 cs to backstab or backstabs if backstabbed twice'

import random

# YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
    
    # Priority 1: If they backstabbed twice in a row (anywhere in history)
    if 'bb' in their_history:
        return 'b'
    
    # Priority 2: If they cooperated 3 times (anywhere in history)
    # NOTE: We must check 'ccc' BEFORE 'cc', otherwise 'cc' will always trigger first.
    elif 'ccc' in their_history:
        return 'b'
        
    # Priority 3: If they cooperated 2 times
    elif 'cc' in their_history:
        return 'c'
        
    # Default
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
     
    # Test 1: Check logic order. 
    # History is 'ccc'. Logic should skip 'cc' and hit 'ccc' -> return 'b'.
    if test_move(my_history='',
              their_history='ccc',
              my_score=0,
              their_score=0,
              result='b'):
         print('Test 1 passed')

    # Test 2: Check 'bb' trigger.
    if test_move(my_history='bbb',
              their_history='cbb', 
              my_score=0, 
              their_score=0,
              result='b'):
        print('Test 2 passed')