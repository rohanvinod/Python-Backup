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
import color_transfer



def create_frame():
    
    img = Image.open('sulfur.JPG') #opens the image
    img = ImageOps.expand(img,border=20,fill= (255, 69, 0))#creates the inner border
    img = ImageOps.expand(img,border=100,fill=(255, 137, 80)) #creates the middle border
    img = ImageOps.expand(img,border=50,fill= (255, 69, 0))#creates outermost border
    img.save('sulfur_modified.JPG') #saves the image as sulfur_modified.JPG
    
    
    img = Image.open('family.png')
    small_img = img.resize((300,100)) #resizes the image.
    small_img.save('small_family.png')
    
    img = Image.open('sulfur_modified.JPG')
    new_img = Image.open('small_family.png')
    new_img = img.paste(new_img, (640,50)) #specifies the position.
    
    img = Image.open('Circle.png')
    new_img = img.resize((00, 100))
    new_img.mll_family.png')
    
    img.save("family_final.png", "PNG")
    
create_frame()




































































































    new_img = img.paste(new_img, (640,50)) #sp