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


def create_frame(file):
    '''The create frame function creates a frame around various images with
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
    width, height = img.size
    img = ImageOps.expand(img,border=20,fill= (139,69,19))#creates the inner border
    img = ImageOps.expand(img,border=100,fill=(255, 137, 80)) #creates the middle border
    img = ImageOps.expand(img,border=50,fill= (139,69,19))#creates outermost border
    
    
    
    img3 = Image.open('sulfur_modified.jpg')
    small_circle_img = Image.open('small_circle.jpg')
    circle_width, circle_height = small_circle_img.size
    
# These for loops paste the small_circle image repeatedly until a specified point.
#=============================================================================#
    # Top row
    img.paste(small_circle_img, (50, 50))
    
    for x in range(math.floor(width/circle_width)):
        x = (x * 100) + 50
        img.paste(small_circle_img, (x, 50))
#=============================================================================#        
    # Bottom row
    img.paste(small_circle_img, (50, height - 150))

    for x in range(math.floor(height/circle_width)):
        x = (x * 100) + 50
        img.paste(small_circle_img, (x, 1025))
#=============================================================================#
    # Left side
    
    for y in range(math.floor(width/circle_width)):
        y = (y * 100) + 50
        img.paste(small_circle_img, (50 , y))
#=============================================================================#
    # Right side
    img.paste(small_circle_img, (1470, 50))
    img.paste(small_circle_img, (1470, 1030))
    math.floor(width/circle_width)
    for y in range(math.floor(width/circle_width)):
        y = (y * 100) + 50
        img.paste(small_circle_img, (1470 ,y))
#=============================================================================#    
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
        create_frame(file)
        print("Finished processing file: ", file)