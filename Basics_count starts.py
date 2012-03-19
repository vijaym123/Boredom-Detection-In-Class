"""
Author : Vijay Mahantesh SM.
Source of learing : http://software-carpentry.org/
Program was written as a part of learing PIL.
This program counts the number of starts in the universe picture. 
"""

import Image
import time

#color code for different colors.
black = (0,0,0)
white = (255,255,255)
red = (178,34,34)


def monochrome( pic , thershold ):
    """
    Syntax : monochrome( image , thershold )
    This function converts the image to monochrome. based on the thershold value as passed as a aurgument by the user. 
    """	
    #Gets the size of the image
    xsize,ysize = pic.size
    #temporary storage. where monochrome image is stored.
    temp = pic.load()
    #Iterates over all the pixels.
    for x in range(xsize):
       for y in range(ysize):
       	  #gets the r,g,b component of the given pixel.	
          r,g,b = temp[x,y]
          #is the r,g,b component is greater than the threshold. that pixel is converted to black
          if (r+g+b)>= thershold : temp[x,y] = black
          #else it is made a white
          else : temp[x,y] = white
    #the output image is stored here.      
    pic.save("/home/vijay/Desktop/universe1.jpg")
    return

def count (pic):
    """
    Syntax : count ( image )
    This function is used to count the number of starts in the image. Basically it counts the number of white patches in the monoshrome image of the universe photo.
    """	
    #Gets the size of the image
    xsize,ysize = pic.size
    #temporary storage. where monochrome image is stored.
    temp = pic.load()
    #Count Variable is used to count the number of white patches in the image. 
    count = 0
    #Iterates over all the pixels.
    for x in range(xsize):
       for y in range(ysize):
       	  #if the given pixel is white. count is incremented. Considering the fact that it is a star. 	
          if temp[x,y] == white :
              count=count+1
              #fill function is called to investigate its surronding pixels.
              fill(temp,xsize,ysize,x,y)
    return count

def fill( temp , xsize , ysize ,x_start,y_start) :
    """
    Syntax : fill(temp , xsize , ysize ,x_start,y_start )
    This function is called to check weather the patch surround the given pixel is white. If so those pixels are colored red. These pixels are colored red because to during the next iteration. The stars which are mentioned counted once SHOULD not be counted again. 
    """	
    #Q is a variable used for Queing the pixels. which might be white.
    Q = [(x_start,y_start)]
    while Q :
        x,y,Q=Q[0][0],Q[0][1],Q[1:]
        if temp[x,y] == white :
            temp[x,y]=red
            #Queing the surrounding pixels, which might be white.  
            if x > 0 : Q.append((x-1,y))
            if x < xsize-1 : Q.append((x+1,y))
            if y > 0 : Q.append((x,y-1))
            if y < ysize-1 : Q.append ((x,y+1))
    return

#main function
#input image
pic = Image.open("/home/vijay/Desktop/Universe.jpg")
#converting the image to monochrome.
monochrome( pic , 200 )
#Retriving the monochrome image.
pic = Image.open("/home/vijay/Desktop/universe1.jpg")
#Counting the number of starts.
c =count( pic )
print "Number of starts in the given universe picture is : " , c 
