import cv2
import numpy as np
import glob
 

folders = ['.\\Component_1\\*.jpg', '.\\Component_2\\*.jpg', '.\\Component_3\\*.jpg']

for i,fol in enumerate(folders):
	img_array = []
	for filename in glob.glob(fol):
	    img = cv2.imread(filename)
	    height, width, layers = img.shape
	    size = (width,height)
	    img_array.append(img)
	 
	 
	out = cv2.VideoWriter( str(i+1) + 'Vid.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
	 
	for i in range(len(img_array)):
	    out.write(img_array[i])
	out.release()