####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random

team_name = 'Judgement' # Only 10 chars displayed.
strategy_name = 'Ratio-based choice'
strategy_description = 'If the opponent has mostly cooperated, cooperate back. Otherwise, backstab.'
    
def move(my_history, their_history, my_score, their_score):
   if len(my_history) < 5:
      return('c')
   else:
      theirC = their_history.count('c')
      theirB = their_history.count('b')
      if theirC > 0 and theirB > 0:
        theirRatio = theirC / theirB
        if theirRatio >= 1.5:
          pick = random.choice(('b','c','c','c','c'))
          return(pick)
        else:
          pick = random.choice(('b','b','b','b','c'))
          return(pick)
      elif theirC == 0:
        return('b')
      elif theirB == 0:
        return('c')
      else:
        return('b')


    
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
