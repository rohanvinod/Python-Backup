#1.4.2
#1-3: N/A
#4: The absolute file name of nice.jpg is desktop.
#5: ../../C:/Desktop/nice.jpg
#6: It is a absolute file name because relative file names do not start of with a C:\.
#You are not in a working directory because it doesn't use ".." to go up to the 
#main directories, it just enters a directory and accesses the items inside.
#In cloud 9, the outputs don't begin with "C:," however in the example given
#each one of the outputs begin with "C:."
#7. 
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

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
# Show the figure on the screen
# fig.show()
fig.savefig('women_plot')
#7: No, the code did not work. 