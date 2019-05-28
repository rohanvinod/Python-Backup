
def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip

#1.3.2 Function Test
def hyp(leg1, leg2):
    '''return the length of the hypothenuse of a right triangle'''
    hyp = (leg1**2 + leg2**2)**0.5
    return hyp
    
    
def mean(a,b,c):
    '''returns the mean of three numbers'''
    mean = (a + b + c )/3.
    return mean
    
    
    
def perimeter(base, height):
    '''returns the length of the base and the height'''
    per = (base*2 + height*2)
    return per
    
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)


