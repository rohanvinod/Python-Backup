#4. (1,2,3) this is another example of a tuple.
#5. one convention is when mr brown tells us that the code cannot stretch past line.
#6a. 'b' because 1 is equal to 'b'
#6b. it will print [a:3] because 0 is a and 2 is 3.
#7a. it will tell us that a is equal to 10.
#7b. it will print '15'
#8a. list elements can be accessed individually.
#8b. it will print out [b:a]
#9. it will print false, then for the second statement, it will print false.
#10a. it will print values + [4, 5]
#10b. it will print out 6, 7 because those are the asigned values.
#11. it won't work because value will not equal value + 5.
#12. it will multiply it by 3.





import random
def roll_two_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2
    
    
print(roll_two_dice())


