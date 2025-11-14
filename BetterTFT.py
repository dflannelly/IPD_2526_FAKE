####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Better TFT' # Only 10 chars displayed.
strategy_name = 'Better Tit for Tat'
strategy_description = 'It is Tit for Tat so it picks the move the opponent did last. It also gives out 2 c after a bad pattern repeats. It also changes c,b,c,b loops to b,b,b,b loops'

# NEEDS TO BE RERUN BEFORE EVERY MATCH (global variables need to be reset)
# NEEDS TO BE RERUN BEFORE EVERY MATCH (global variables need to be reset)
# NEEDS TO BE RERUN BEFORE EVERY MATCH (global variables need to be reset)

OnceandDone = 0
times = 1
betray = 0
import random
def move(my_history, their_history, my_score, their_score):
    # NEEDS TO BE RERUN BEFORE EVERY MATCH (global variables need to be reset)
    global OnceandDone
    global times
    global betray
    
    if len(my_history) == 0:
        return('c')

    if OnceandDone == 1:
        OnceandDone += 1
        return('c')

    if len(my_history) >= 5 and times <= 3:
        if their_history[-4:-1] == my_history[-5:-2] and their_history[-4:-1] != ['c','c','c','c']:
            OnceandDone = 1
            times += 1
            return('c')

    if betray >= 1:
        if betray == 1:
            betray += 1
            return('b')
        if their_history[-1] == 'c':
            betray = 0
            OnceandDone = 1
            return('c')
        else:
            return('b')
            
    if len(my_history) >= 5 and times > 3:
        if their_history[-4:-1] == my_history[-5:-2] and their_history[-4:-1] == ['b','c','b','c']:
            betray = 1
            return('b')

    if their_history[-1] == 'b':
        return('b')
    if their_history[-1] == 'c':
        return('c')

    
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
