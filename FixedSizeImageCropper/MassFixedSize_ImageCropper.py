import numpy as np 
from os import listdir
from skimage import data, io, color
import matplotlib.pyplot as plt
from PIL import Image

print("Started.....")
fol = 'G:\\Guru_Sarath\\Study\\TAMU\\691_Research\\ICA_Image_Sequences\\3_jpg'
files = listdir(fol)


images = []
shapes = []
for f in files:
	path = fol + '\\' + f
	image = io.imread(path)
	print(path , image.shape)
	#image = resize(image, WorkingImageSize, anti_aliasing=True)
	shapes.append(image.shape)
	image = image[542:638, 566:675,:]
	images.append(image)

for count,i in enumerate(images):
	
	plt.imshow(i, vmin=0, vmax=255)
	plt.show()
	
	im = Image.fromarray(i)
	im.save( str(count) + "_.jpg")
	

