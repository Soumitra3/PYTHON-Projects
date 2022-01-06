import random

def guess(x):
    random_n = random.randint(1,x)
    guess = 0
    while guess!=random_n:
        guess = int(input(f'Enter a random numer between 1 and {x}: '))
        if guess < random_n:
            print("Sorry,Incorrect guess!")
        elif guess > random_n:
            print("Oops! Too High")
    print(f'Yay, Congrats! Ypu have guessed the correct number {random_n}')

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (h), too low (l) or correct (c): ") 
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess}, correctly! ") 
    
      
guess(10)
comp_guess(100)
          