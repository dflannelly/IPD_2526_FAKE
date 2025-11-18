####
# Each team's file must define four tokens:
#      team_name: a string
#      strategy_name: a string
#      strategy_description: a string
#      move: A function that returns 'c' or 'b'
####

team_name = 'Declare War' # Only 10 chars displayed.
strategy_name = 'RNG'
strategy_description = 'Using random number generator, 80% Betray 20% cooperate.'

import random

# YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
    # random.choice picks one item from the list
    # 4 'b's and 1 'c' = 80% chance of betrayal
    thing = random.choice(['b', 'c', 'b', 'b', 'b'])
    return thing

def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    
    # Because your strategy is random, testing is tricky.
    # We just check if it runs without crashing.
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
     
    # Test 1: Betray on first move.
    # NOTE: Since your code is random, this test might fail 20% of the time 
    # (when it chooses 'c'). That is normal for this strategy!
    if test_move(my_history='',
              their_history='',
              my_score=0,
              their_score=0,
              result='b'):
         print('Test 1 passed (Randomly selected b)')
         
    # Test 2: Check another move
    test_move(my_history='bbb',
              their_history='ccc',
              my_score=0, 
              their_score=0,
              result='b')