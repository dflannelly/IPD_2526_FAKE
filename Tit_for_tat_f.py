####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


#YOUR TEAM DETAILS HERE
team_name = 'Tit_for_tat_f' # Only 10 chars displayed.
strategy_name = 'Randomness until see betrayal patten in opponent'
strategy_description = 'Randomly chooses b/c until certain patterns are recognized then it acts accordingly'

import random



#YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
    # Tit-for-tat style strategy
    if len(my_history) == 0:
        return 'b'  # first move betray

    # If opponent colluded 3 times in a row → betray
    if len(their_history) >= 3 and their_history[-3:] == "ccc":
        return 'b'

    # If opponent betrayed 2 times in a row → betray
    if len(their_history) >= 2 and their_history[-2:] == "bb":
        return 'b'

    # If we betrayed 4 times in a row → collude
    if len(my_history) >= 4 and my_history[-4:] == "bbbb":
        return 'c'

    # Otherwise, randomly choose 'b' or 'c'
    return random.choice(['b', 'c'])




    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
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
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
