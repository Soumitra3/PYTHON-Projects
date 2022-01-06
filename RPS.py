import random 

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def play():
    user = input("What's your choice? 'r' for Rock, 'p' for paper, 's' for scissor \n")
    comp = random.choice(['r', 'p', 's'])

    if is_win(user,comp):
       print(f'You WON! The computer chose {comp}')

    print(f'You lost! The computer chose {comp}')

    if user == comp:
       print(f'It is a tie! The computer chose {comp}')
    
play()