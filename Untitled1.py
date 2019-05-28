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



def create_frame(file):
    
    img = Image.open(file) #opens the image
    img = ImageOps.expand(img,border=20,fill= (139,69,19))#creates the inner border
    img = ImageOps.expand(img,border=100,fill=(255, 137, 80)) #creates the middle border
    img = ImageOps.expand(img,border=50,fill= (139,69,19))#creates outermost border
    
    directory = os.listdir('/home/ubuntu/workspace/practice')
    os.chdir('/home/ubuntu/workspace/practice')
    for file in directory:
        print("Now processing file: ", file)
        create_frame(file)
        print("Finished processing file: ", file)
    