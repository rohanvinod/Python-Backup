from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
#4. 





def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')








def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')
    
    
    
    
def Roll_Hundred_Pair():
    die1 = random.randint(1,6)
    dei2 = random.randint(1, 6)
    print([random.randint(1,6) for _ in xrange(100)])
    
   
   
   
    
def dice(n):
    answer = 0
    for i in range (0, n-1):
        die = random.randint(1, 6)
        answer = answer + die
    return answer
    
    
    


def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
#line 2 was necessary because if you comment it out, the program will not work.



def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Summarize the function in this docstring.
    
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # Summarize the following section of code here
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # explain index here
        print(p+', ', end='')
    print(players[len(players)-1]) # explain this line here

    ####
    # Summarize the following section of code here
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    





def goguess(n):
    n = random.randint(1, 10)
    guess = int(raw_input("Enter an integer from 1 to 10: "))
    while n != "guess":
        print
        if guess < n:
            print ("guess is low")
            guess = int(raw_input("Enter an integer from 1 to 10: "))
        elif guess > n:
            print ("guess is high")
            guess = int(raw_input("Enter an integer from 1 to 10: "))
        else:
             print('You guessed in', guess, 'guesses!')
             break


def matches(ticket, winners):
    ''' '''
    
    
    
    
    
    
    
    
    
    
'''1conclusion. the disadvantages of this is that you have to write a lot more
lines of code rather than just a few lines of code.'''
'''2conclusion. analysis is an iteration through a code.'''
'''3conclusion. while loop goes on forever and the for loop has a start and an
end''
''''''4conclusion. Me and my partner worked very well, and we  worked on each problem
step by step until we figured out the solution.'''
    
    
    
#1.3.7 Function Test
print(Roll_Hundred_Pair())
print(validate())
print(goguess(7))
print(dice(6))


