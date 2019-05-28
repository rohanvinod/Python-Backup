#6a. Prediction: True
# my prediction was correct.

#6b. Prediction: True
# my prediction was correct.

#7.50>x and x<80 and 30<=y and y<=45 makes the statement false.

#8. when I assigned the new numbers to x and y, my compound conditional was false.

#9.Structures & the print() Function!!!!

from __future__ import print_function # use Python 3.0 printing 

def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 
#9a. predictions: I think it will tell me that if my age is lower than 13, I will be below the age limit.

#10. 
def report_grade(percent):
    if percent > 80:
        print('A grade of ' +  str(percent)  + ' percent indicates mastery. Keep up the good work!')
        return percent
    else: 
        print('A grade of ' +  str(percent) + ' percent does not indicate mastery. Seek extra practice or help')
        return percent
    '''Step 9b if-else'''

    
    
#11. 
def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
        
def letter_in_word(guess, word):
    if guess in word:
        return True
    else:
        return False
        
#12.        
def hint(color, secret):
    secret = ['red', 'red', 'red', 'yellow', 'yellow', 'black']
    if color in secret:
        print( color + ' is in the sequence')
    else:
        print( color + ' is not in the sequence')
    
        
        
#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('z', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)

#conclusion 1. if

    
# should check len(letter)==1
