import numpy as np 
import mahotas 
import mahotas.demos 
from mahotas.thresholding import soft_threshold 
from matplotlib import pyplot as plt 
from os import path 

f = mahotas.demos.load('luispedro', as_grey = True) 
plt.gray() 
print("Image") 
plt.imshow(f) 
plt.show() 
f = f[50:200, 20: 250] 
print("Cropped Image") 
plt.imshow(f) 
plt.show() 
