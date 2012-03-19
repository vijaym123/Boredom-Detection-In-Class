#Importing PIL library 
import Image

#size  is a integer tuple containing the image size.
size = 1280,1280

infile = "/home/vijay/Desktop/input.png"
#Path of the Image
 
pic = Image.open(infile)

#Converting the image to thumbnail.
pic.thumbnail(size)

#Saving the thumbnail.
pic.save("/home/vijay/Desktop/output.jpeg")
