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
filename = os.path.join(directory, 'cat-1a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
#fig.show()
fig.savefig('cat-1a.png')


#7a. (300,400)
#7b. (64,42)

#8.

#8a.
#1. fig is an instance of the class figure 
#2. ax is in an instance of the class axis

#8b. 
#Similarly, in line 25, the method savefig is being called on the object fig.
#That method is being given 1 argument. That method is a method of the 
#class subplot.

#9.
# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
filename = os.path.join(directory, 'woman.jpg')
img = plt.imread(filename)
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('two_woman.jpg')


# Create a 1x5 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 5)
# Show the image data in the first subplot
filename = os.path.join(directory, 'cat_plot.png')
img = plt.imread(filename)
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('five_cats.png')






'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing')




#11a:
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'leaf_earing.png')
# Read the image data into an array
img = plt.imread(filename)
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[0].set_xlim(300, 200)
ax[0].set_ylim(300, 200)
ax[0].set_title("Experiment")
ax[0].set_xlabel('Width')
ax[0].set_ylabel('Height')
ax[0].minorticks_on()
ax[1].imshow(img, interpolation='none')
ax[1].set_xlim(300, 200)
ax[1].set_ylim(300, 200)
ax[1].set_title("Experiment")
ax[1].set_xlabel('Width')
ax[1].set_ylabel('Height')
ax[1].minorticks_on()
# Show the figure on the screen
# fig.show()
fig.savefig('experiment.png')





#11b:
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat-1a.png')
# Read the image data into an array
img = plt.imread(filename)
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[0].set_xlim(300, 200)
ax[0].set_ylim(300, 200)
ax[0].set_title("closeup")
ax[0].set_xlabel('Width')
ax[0].set_ylabel('Height')
ax[0].minorticks_on()
ax[1].imshow(img, interpolation='none')
ax[1].set_xlim(300, 200)
ax[1].set_ylim(300, 200)
ax[1].set_title("Closeup")
ax[1].set_xlabel('Width')
ax[1].set_ylabel('Height')
ax[1].minorticks_on()
ax[2].imshow(img, interpolation='none')
ax[2].set_xlim(300, 200)
ax[2].set_ylim(300, 200)
ax[2].set_title("Closeup")
ax[2].set_xlabel('Width')
ax[2].set_ylabel('Height')
ax[2].minorticks_on()
# Show the figure on the screen
# fig.show()
fig.savefig('three_closeup.png')


#12.axes.fill fills in a polygon with a certain color, and you can adjust
#the colors by inputing different rgb values.



#13.

# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'crazymice.jpg')
# Read the image data into an array
img = plt.imread(filename)
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[1].plot(116, 42, 'ro')
ax[1].plot(140, 42, 'ro')
ax[1].plot(37, 48, 'ro')

# Show the figure on the screen
# fig.show()
fig.savefig('crazymice_plot.jpg')






