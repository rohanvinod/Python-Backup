from __future__ import print_function
from PIL import Image
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw 
import numpy as np
import Image, ImageOps
import os
import math
import time



print ("_________________________________________________________")
print ("l      Welcome to the Image Manipulation Project        l")
print ("[         by Rohan Vinod and Riya Kulkarni              ]")
print ("[                      Period 5                         ]")
print ("l_______________________________________________________l")
time.sleep(2)
print ("INSTRUCTIONS")
print ("If you are inserting an image into the folder, add 'Image_'") 
print ("before of the name of the file that you are inserting.")
time.sleep(2)
Answer1 = raw_input('pick a color to use for the inner border: ')

Answer3 = raw_input('pick a color to use for the outer border: ')

print ("________Now creating your border! _______________________")





def create_frame(file):
    '''
    Answer 1, and answer 3 all control the color of the border of the
    frame. The user can specify which color they can use based on the user input
    that they type in.
    
    The create frame function creates a frame around various images with
    different sides. The parameter are the files that we are applying the frame
    to.
    
    The expand method from the imageOps library expands the sides of the
    images by a set number of pixels, then gives you the option of specifying
    what color you want it to be. 
    
    we used the .resize() function from the Image library, which resizes the 
    image to a specified size.
    
    To add pictures all around the frame, we used loops to loop the image to a 
    set number until it reached the end of the border. We did this with each of 
    the four sides of the image.'''
    
    
    
    img = Image.open(file) #opens the image
    
    img = ImageOps.expand(img,border=20,fill= (Answer1))#creates the inner border
    img = ImageOps.expand(img,border=100,fill=(0, 0, 0)) #creates the middle border
    img = ImageOps.expand(img,border=50,fill= (Answer3))#creates outermost border
    
    width, height = img.size      
    width = width - 100
    height = height - 100
    
    img3 = Image.open('sulfur_modified.jpg')
    small_circle_img = Image.open('small_circle.jpg')
    circle_width, circle_height = small_circle_img.size
    
# These for loops paste the small_circle image repeatedly until a specified point.
#=============================================================================#
    # Top row
    img.paste(small_circle_img, (50, 50))

    for x in range(1,int( math.floor(width/circle_width))):
        x = (x * 100) + 50
        #print("Top side processing ", x)
        img.paste(small_circle_img, (x, 50))
#=============================================================================#        
    # Bottom row
    img.paste(small_circle_img, (50, height - 50))

    for x in range(1, int(math.floor(width/circle_width))):
        x = (x * 100) + 50
        #print("Procesing Bottom", x)
        img.paste(small_circle_img, (x, height - 50))
#=============================================================================#
    # Left side
    
    for y in range(1, int (math.floor(height/circle_width))):
        y = (y * 100) + 50
        #print("Processing left side", y)
        img.paste(small_circle_img, (50 , y))
#=============================================================================#
    # Right side
    img.paste(small_circle_img, (width - 50, 50))
   
    for y in range(1, int(math.floor(height/circle_width))):#divides width of frame 
    #by small_circle_img width
        y = (y * 100) + 50
        #print("precessing right side", y)
        img.paste(small_circle_img, (width - 50 ,y))
#=============================================================================# 

    img.paste(small_circle_img, (width - 50, height - 50))#pastes the small_circle_img
    #on the corner of the frame.
    img.paste(small_circle_img, (50, height - 50))
    img.save(file)
    return(file)
        
directory = os.listdir('/home/ubuntu/workspace/1.4.7/Project_Images')
os.chdir('/home/ubuntu/workspace/1.4.7/Project_Images')


img = Image.open('family.jpg') #opens the image
small_img = img.resize((300,100)) #resizes the image.
small_img.save('small_family.jpg')#saves the image

circle_img = Image.open('Circle.jpg') #opens the image
small_circle_img = circle_img.resize((100, 100)) #resizes the image and makes
#it smaller
small_circle_img.save('small_circle.jpg') #saves the image


img1 = Image.open('family_final_beta.jpg') #opens the image that we want to paste 
    #the picture on
img2 = Image.open('small_family.jpg') #opens the image that we want to paste
img1.paste(img2, (650, 50)) #pastes the image with the coordinates of (650, 50)
img1.save('final_project.jpg')
    


for file in directory:
    if "Image" in file:
        print("Now processing file: ", file)
        time.sleep(1)
        create_frame(file)
        time.sleep(1)
        print("Finished processing file: ", file)
