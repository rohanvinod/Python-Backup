from __future__ import print_function # must be first in file 
import random

#1.Nested if structures and testing:
def food_id(food):
    food = 'fruits', 'citrus', 'starchy'
    
    
    ''' Returns categorization of food
    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#1a. When I run the code, it prints out lines 23 and 25.
#1b. i. food_id('orange')
#1b. ii. food_id('banana')
#1b. iii. food_id('banana')
#1b. iv. food_id('orange')

#2. 

def food_id_test():
    
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
        
#3

def f(n):
    if type(n) == int:
        if (n % 2 == 0):
            if ( n % 3 == 0):
                print(str(n) + ' is a multiple of 6')
            else:
                print(str(n) + ' is a not multiple of 6')
        else:
            print(str(n) + ' is odd')
            
    else: 
        print('n is not an integer')
        
#4. f('3'), f(2), f(3), F(18).
#5. 
def f_test(n):
    if type(n) == int:
        if (n % 2 == 0):
            if ( n % 3 == 0):
                print(str(n) + ' is a multiple of 6')
            else:
                print(str(n) + ' is not a multiple of 6')
        else:
            print(str(n) + ' is odd')
            
    else: 
        print('n is not an integer')

#Part II: The raw_input() function, type casting, and print() from Python 3
#7. + in concatenation adds words together, and + as a numeric addition adds values.
#8. 


def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess < secret:
        print('Your guess is low')
    elif guess == secret:
        print('Right, my number is', guess, end='!\n')
    else:
        print('Your guess is high')
        
'''8a. line 11 pints the opposite of line 9, because there is no other option for 
the answer but to be right.'''
#9.
def quiz_decimal(low, high):
    secret = random.uniform(low, high)
    guess = int(raw_input('Guess: '))
    if low <= guess <= high:
        print ('good, ' + str(guess) + ' is >= ' + str(low)  +  ' and <= ' + str(high))
    else:
        print ('wrong, ' + str(guess) + ' is not >= ' +str(low) + ' and <= ' + str(high))
        
'''conclusion 1. the relationship between if stuctres and glass box testing is that 
they help find any bugs in the program'''
'''conclusion 2. 3 blocks of code might be executed by nested if -lse statements.'''
'''conclusion 3. the test suite looks for any flaws in the program.'''
'''conclusion 4.''' 

def f_challenge(n):
    if is_int(n):
        if is_even(n):
            if  is_multiple_of_6(n):
                print(str(n) + ' is a multiple of 6')
            else:
                print(str(n) + ' is  not multiple of 6')
        else:
            print(str(n) + ' is odd')
            
    else: 
        print('n is not an integer')
        
def is_int(n):
    if type(n) == int:
         return True
    else:
        return False
        
        
def is_even(n):
    if ( n % 2 == 0):
        return True
    else:
        return False

def is_multiple_of_6(n):
    if ( n % 6 == 0):
        return True
    else:
        return False

        
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)

        

        






