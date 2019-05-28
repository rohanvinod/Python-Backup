#13. 
#A. Matplotlib.pyplot is an interface used for plotting.
#B. Numpy is a core library for scientific computing.
#C. PIL is a python imaging library
#15. 
#15a. Line 19 calls the function subplots from the matplotlib.pyplot (plt) library. 
#The function is being called with 2 argument(s): 1, and 2. The function returns 
#2 object(s), which is/are being assigned to ax.

#15b. 
#line 23 calls .imshow() on ax[1].
#line 24 calls .xticks() on ax[1]
#line 25 calls .set_xlim() on ax[1]
#line 26 calls .set_ylim() on ax[1]
#line 27 calls .savefig() on fig

#15c.
# The coordinates of the upper left part of the eye is (966, 1253).

#16.
#16a. The coordinates of the upper left corner of the eye are (690, 950). The 
#width of the eye is about 90 and the height is 50. 

#17.
#17a. Line 30 uses the join() method from the os.path module. It is being passed
# 1 argument. The value it returns is being assigned to the variable directory.

#17b. In line 31 the open() function of the PIL.Image module returns a new
# PIL.Image object, which is being assigned to the variable earth.img.

# 17c. the two numbers in the parenthesis represents the power that you want 
# to zoom into the eye with.

#17d. The purpose of (89, 87) is to resize the image to a width of 89 and a 
#height of 87. 

#17e. Line 30 calls the function .join() from the os.path library with 1 
#argument(s): earth.png. The function returns 1 object(s), which is/are
#being assigned to earth_file.

#17f. 
#i. An additional argument that can be passed with the rejoin() method is the
# and y values of the new image.
#ii. the default value is 

#17g. The size of the image with the x and the y coordinates.
#17h: the output was the coordinates of all of the earth images sizes.
#17i. the image on the right has less pixels so it looks more blurry and the 
# quality is worse. 

#18. The resize method changes the size of the image by creating more or less 
# pixels.

#19. 
#19a. 
# student_img = 750,000
# earth_small = 960,500
#19b:
#N/A
#19c. 
#student.jpg bytes = 206 KB
#smallEarth.png bytes = 18.2 KB
#19d. 
#The sizes of the images from step A are way larger than the size of the images
#from step C. 
#19e. It will paste the color instead of the image into a new file.
#19f. if they are different, then the code will not work, and won't produce
#the image.
#19g: 
#the first part of the argument; "earth_small" is saying to paste the image 
#earth_small on the student_img. The coordinates; (1162, 966) are assigning the 
#image a size and the last part of the argument is stating that the image 
#"earth_small" should be masked. 


