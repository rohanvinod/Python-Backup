#4: Arrays are much faster than lists, however they are similiar because they both
#can mix different types of data. 
#5:
from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import PIL
# 'as' lets us use standard abbreviations
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
#6:
###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for row in range(200, 220):
    for column in range(50, 100):
        img[row][column] = [255, 255, 0] # red + green = yellow
        
        
        
        

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
###
# Make a rectangle of pixels yellow
###
height = len(img)
width = len(img[0])
for row in range(420, 450):
    for column in range(140, 160):
        img[row][column] = [0, 255, 0] 
fig.savefig('green_earing.png')
ax.imshow(img, interpolation='none')

print(type(img))
print(img)
print(len(img))
print(len(img[0]))

height = len(img)
width = len(img[0])
for row in range(420, 450):
    for column in range(140, 160):
        img[row][column] = [255, 0, 56] 
###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
            
fig.savefig('woman_sky_earing.png')
ax.imshow(img, interpolation='none')

img = plt.imread(filename)
#7a. It sets the size of the rectangle for the image that you are creating and 
#it assigns the color magenta to the image.
#7b. 
img = plt.imread(filename)

##
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: 
            img[r][c]=[255,255,0]
###
# Show the image data
###


###

#9

import sys

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row)/stripe_width % 2 == 0 or (column)/stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [255, 255, 255, 255] #white
            
            else:
                # Odd stripe
                image[row][column] = [0,0, 0, 255] #black
    return image
    
if __name__ == "__main__":
     image = make_mask(100,100,10)

     fig, ax = plt.subplots(1, 1)
     plt.axis('off')
     ax.imshow(image)
     fig.savefig('mask.png')            
    

     # Get the directory of this python script
     directory = os.path.dirname(os.path.abspath(__file__))
     # Build an absolute filename from directory + filename
     filename_woman = os.path.join(directory, 'woman.jpg')
     filename_mask = os.path.join(directory, 'mask.png')
    
     # Read the image data into an array
     img_woman = plt.imread(filename_woman)
     img_mask = plt.imread(filename_mask)
    
     # Create figure with 2 subplots
     fig, ax = plt.subplots(1, 2)
    
    
     # Show the image data in the first subplot
     ax[0].imshow(img_woman, interpolation='none')
     ax[1].imshow(img_mask, interpolation='none')
    
     fig.savefig('woman_mask.png')
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    