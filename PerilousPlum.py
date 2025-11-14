####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Perilous Plum' # Only 10 chars displayed.
strategy_name = 'Randomness leaning towards betrays'
strategy_description = 'The first output starts with a betray and attacks from the start. From there, many of the rounds (including every 20 rounds) pull from a random list that favors betraying over colluding, making it unpredictable and patternless.'
import random

def move(my_history, their_history, my_score, their_score):
  list1 = ['b', 'b', 'b', 'c', 'c']
  list2 = ['b', 'b', 'c']
  if len(my_history) == 0:
    return('b')
  if len(my_history) == 1:
    return random.choice(list1)
  if len(my_history) >= 3:
    return random.choice(list2)
  if len(my_history)%20 == 0:
      return random.choice(list1)
  if their_history[-1] == 'c':
    return 'c'
  if their_history[-1]== 'b':
    return 'b'
  if their_history[-2]=='b':
    return 'b'

    
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
