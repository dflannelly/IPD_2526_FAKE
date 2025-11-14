####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


#YOUR TEAM DETAILS HERE
team_name = 'MasonTeam' # Only 10 chars displayed.
strategy_name = 'Dont_Cross_Me'
strategy_description = 'Depending on what letter you type in you either gain or loss points'

import random

def game():
  counter = 0
  global my_history
  global their_history
  global my_score
  global their_score

  my_history = []
  their_history = []

  my_score = 0
  their_score = 0

  game_length = random.randint(100,150)

  for i in range(game_length):
     choice1 = Dont_Cross_Me()
     choice2 = wild_card()

     my_history += choice1
     their_history += choice2

     release = 0
     reward = 100
     punishment = -250
     severe_punishment = -500

     if choice1 == 'c' and choice2 =='c':
       my_score +=  release
       their_score += release

     elif choice1 == 'b' and choice2 =='b':
       my_score += punishment
       their_score += punishment

     elif choice1 == 'c' and choice2 =='b':
       my_score += severe_punishment
       their_score += reward

     elif choice1 == 'b' and choice2 =='c':
       my_score += reward
       their_score += severe_punishment

     counter +=1

  print("Broccoli Bruisers :", my_score)
  print("Wild Card :",their_score)

  print("Broccoli Bruisers: ",my_history)
  print("Wild Card: ", their_history)
game()



#YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
def Dont_Cross_Me()
  if len(my_history)==0:
    return('c')

  elif 'b' in their_history:
    return('b')
  else:
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
