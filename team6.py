####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Vince reschs team' # Only 10 chars displayed.
strategy_name = 'conclued untill betryed '
strategy_description = 'be fair untill hes untrustworthy'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)%2==0: 
        return 'c'
            else: return 'b'
    if 
        

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
   if len(my_history)==0:
       return 'c'
   if 'b' in their_history:
       return 'b' 
   else:
       return 'c'
        