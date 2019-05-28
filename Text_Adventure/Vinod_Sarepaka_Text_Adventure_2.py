

def Intro():
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~Saving Earth~~~~~~~~~~~~~~~~~~~")
    print (" Once upon a time, you  were walking in the park alone.")
    print (" You saw a cat sitting by the edge of the water chanting spells.")
    print (" The cat seemed to have glowing eyes and levitate off of the ground.")
    
def scene_2():
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Scene 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print " You get sucked into the portal"
    print " You see a Dungeon surrounded in lava and and a rickety bridge leading to a cave"
    
def scene_3():
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~scene 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print " You hear the roar of a dragon coming from in front of you. There is a dragon"
    print " flying above you, maintaining eye contact with you. You are very scared."
    
    
def Decision(prompt):
    Question = raw_input(prompt)
    return Question
    

Intro()
answer = Decision(" Press 'y' to walk to cat or 'n' to walk away from cat: ")
if answer == 'y':
    print " You walk towards the cat, and then all of a sudden, it turns into"
    print " a man and opens a portal. He tells you that the fate of the world rests"
    print " on your shoulders and that you should enter the portal."
    
elif answer == 'n':
    print " you walk past the weird cat and continue along until you hear rapid"
    print " footsteps behind you. You look back and see the cat transform into a man and"
    print " Tell you to go into the portal. You are confused at first but blindly accept."
else:
    print "invalid"
    
    
scene_2()
answer = Decision(" Press 'y' to explore the dungeon or 'n' to explore the cave: ")
if answer == 'y':
    print " you walk around in the dungeon and find old remains of humans inside the cells"
    print " When you take a closer look, you can see burn marks across their face."
    print " You feel uneasy and try to not throw up, and think of ways to get home."
    
elif answer == 'n':      #prints these strings if you answer 'n'
   print " You decide to cross the bridge, and explore the cave and see if there is a way out."
   print " When you get to the bridge, you notice that a few of the boards are missing. You "
   print " are scared but willing to do anything just to get out."

else:
    print "invalid"      #prints invalid if you print anything other than 'y' or 'n'
    
scene_3()
answer = Decision(" Press 'y' to hide from dragon or press 'n' to fight dragon: ")
if answer == 'y':
    print " You run into an empty cell and hide. You are very afraid and can't move."
    print " The roar of the dragon seems to be getting closer and closer. You can't "
    print " handle the suspense. Then, the dragon comes behind you and kills you"
    print " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~YOU DIE :(~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
elif answer == 'n':
    print " You look for a weapon that you can use to kill the dragon. You find an "
    print " enchanted sword and charge toward the dragon. The draqon blows fire, and "
    print " you shield youself from its deadly fire using a shield that you took from"
    print " a skeleton in the dungeon. With one big blow to the head, the dragon is dead!"
    print " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`YOU WIN!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`"
    
else:
    print "invalid"
    

    
    
    
