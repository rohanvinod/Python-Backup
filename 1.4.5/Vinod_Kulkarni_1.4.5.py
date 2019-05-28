from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw 
import numpy as np

def round_corners_one_image(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask 
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def round_corners_of_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
#6
round_corners_of_all_images()
#1-4 N/A
#5: The name of the three functions are "round_corners_one_image", "get_images"
# and "round_corners_of_all_images."

#7a.
#Argument 1: Original_image
#Argument 2: Percent_of_side
#Return value: 3
#7b. The color of the new image would be magenta. 
#7c. The object from line 26 is "rounded_mask" and the object from line 27 is
#drawing_layer.
#7d. The alpha value would be 0
#7e. The first image (with the four circles); is creates by lines 41-48, while
#the other image is created by lines 33-38. In the first image, the circle in
#the top left was created by lines 41-42, the circle in the top right was made
#by lines 43-44, the circle in the bottom left was created by lines 45-46 and
#the circle in the bottom right was made by lines 47-48. 
#7f. the color that was filled is black. 
#7g. The color values are (0, 127, 127) which makes cyan.

#8a.
#8b. img_list and file_list are returned by the function.
#8c. os.getcwd(), os.listdir(directory), and os.path.join(directory, entry)
#8d. os.listdir returns a list containing the names of the entries in the 
#directory given by path. 
#8f. It does 

#9.
#9a. It is in a try except structure because the code will get an error so it is
# telling us to pass it and continue on.
#9b. It represents the length of the image_list
#9c. It iterates through the length of the image_list.

# EXTRA PRACTICE:
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'Dolly.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
height = len(img)
width = len(img[0])
for r in range(597):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
filename_Dolly = os.path.join(directory, 'Dolly.jpg')
img_Dolly = plt.imread(filename_Dolly)            
ax[0].imshow(img, interpolation='none')
            
fig.savefig('Modified.png')