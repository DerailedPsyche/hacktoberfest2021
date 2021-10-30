import mahotas 
import mahotas.demos 
import numpy as np 
from pylab import imshow, gray, show 
from os import path 

photo = mahotas.demos.load('luispedro') 
print("Origial Image") 
imshow(photo) 
show() 
photo = mahotas.demos.load('luispedro', as_grey = True) 
print("Image loaded as grey") 
imshow(photo) 
show() 
