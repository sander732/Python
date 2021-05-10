import random, sys
print('rock, paper, scissors')
#these variabels keep track of the number of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s losses, %s ties'%(wins, losses, ties))
    while True:
        print('enter your move: (r)ock (p)aper (s)cissors of (q)ui')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() 
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('type one of r, p, s, or q')
    if playerMove == 'r':
        print('rock vs...')
    elif  playerMove == 'p':
        print('paper vs...')
    elif playerMove == 's':
        print('scissors vs...')
    
    randomnummer = random.randint(1, 3)
    if randomnummer == 1:
        computerMove = 'r'
        print('rock')
    elif randomnummer == 2:
        computerMove = 'p'
        print('paper')
    elif randomnummer == 3:
        computerMove = 's'
        print('scissors')
    
    if playerMove == computerMove:
        print('it  is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif  playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and  computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1