####
# Each team's file must define four tokens:
#      team_name: a string
#      strategy_name: a string
#      strategy_description: a string
#      move: A function that returns 'c' or 'b'
####

# YOUR TEAM DETAILS HERE
team_name = 'defRealFunct' # Only 10 chars displayed.
strategy_name = 'random until after 10 rounds'
strategy_description = 'randomly chooses letters'

import random

# YOUR CODE IN THE MOVE FUNCTION HERE
def move(my_history, their_history, my_score, their_score):
    round_num = len(my_history)
    
    # FIX: We count how many times they have cooperated in their ENTIRE history.
    # This ensures 'cs' is accurate every single turn.
    cs = their_history.count('c')

    # Round 0 (First move)
    if round_num == 0:
        return 'b'
    
    # Rounds 1 to 6
    elif 0 < round_num <= 6:
        answer = ['b', 'c']
        return random.choice(answer)
        
    # Round 7 onwards
    else:
        # If they betrayed us the last 2 times in a row
        if their_history[-1] == 'b' and their_history[-2] == 'b':
            return 'b'
        
        # If they have cooperated between 6 and 9 times TOTAL
        elif 5 < cs < 10:
            answer = ['b', 'c', 'c', 'c', 'c'] # 80% chance of 'c'
            return random.choice(answer)
        
        # If the last 3 moves didn't match
        elif (their_history[-1] != my_history[-1] and
              their_history[-2] != my_history[-2] and
              their_history[-3] != my_history[-3]):
            return 'b'
        
        # Default
        else:
            return 'b'

def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    
    # Because your strategy uses random, we mostly want to ensure it doesn't crash.
    # If the result is random, we can't strictly enforce == result, but we check if it runs.
    if real_result == result:
        return True
    else:
        # Only print error if we really expected a specific output (like round 0)
        # or if we want to see what happened.
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move (Round 0).
    # Your code forces 'b' on round 0.
    if test_move(my_history='',
              their_history='',
              my_score=0,
              their_score=0,
              result='b'):
         print('Test 1 passed')

    # Test 2: Random phase (Round 1-6).
    # We expect 'b' OR 'c'. We'll test for 'b', but it might fail 50% of the time.
    # That is acceptable for a random strategy.
    test_move(my_history='b',
              their_history='c',
              my_score=0,
              their_score=0,
              result='b')
              
    # Test 3: Double Betrayal Trigger (Round 7+).
    # their_history ends in 'bb', so we expect 'b'.
    if test_move(my_history='ccccccb',
              their_history='cccccbb', 
              my_score=0,
              their_score=0,
              result='b'):
         print('Test 3 passed')