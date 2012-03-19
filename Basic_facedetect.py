"""
Source : Internet + My little contribution in understanding and drawing boxes around the detected faces. 
This program is used to detect faces in the image with the help of haar-like features.
This is basic sample programs, i have been playing around to get around with OpenCV and PIL.
"""
# Usage: python face_detect.py <image_file>
import sys, os
from opencv.cv import *
from opencv.highgui import *
import Image
import ImageDraw

def detectface(image):
  """Converts an image to grayscale and prints the locations of any
     faces found"""
  #converts the image to grey scale.   
  grayscale = cvCreateImage(cvSize(image.width,image.height), 8, 1)
  cvCvtColor(image, grayscale, CV_BGR2GRAY)

  storage = cvCreateMemStorage(0)
  cvClearMemStorage(storage)
  cvEqualizeHist(grayscale, grayscale)
  cascade = cvLoadHaarClassifierCascade('haarcascade_frontalface_alt.xml',cvSize(1,1))
  faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2,CV_HAAR_DO_CANNY_PRUNING, cvSize(50,50))
  
  a = []
  img = Image.open(sys.argv[1])
  draw = ImageDraw.Draw(img)
  if faces:
    for f in faces:
      print("[(%d,%d) -> (%d,%d)]" % (f.x, f.y, f.x+f.width, f.y+f.height))
      a.append( [(f.x, f.y), (f.x+f.width, f.y+f.height)] )

  for i in a:
   draw.rectangle(i)
  print len(a)
  img.save('Detected_Faces.jpg')		
      

def main():	
  image = cvLoadImage(sys.argv[1]);
  detectfaces(image)

if __name__ == "__main__":
  main()
