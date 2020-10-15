import mahotas 
import mahotas.demos 
from pylab import gray, imshow, show 
import numpy as np 
    
# loading image(input image file name inplace of 'lena')
img = mahotas.demos.load('lena')  
img = img.max(2)  
T_otsu = mahotas.otsu(img)    
img = img > T_otsu 
    
print("Image threshold using Otsu Mehtod") 
imshow(img) 
show() 
weight = np.ones((5, 5), float) 
new_img = mahotas.convolve(img, weight) 
print("Convolved Image") 
imshow(new_img) 
show() 
