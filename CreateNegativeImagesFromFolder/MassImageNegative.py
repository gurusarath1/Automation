import cv2
import numpy as np
import glob
 

folders = ['.\\Negative\\*.jpg']
outputPath = '.\\Output_Positive\\'


for i,fol in enumerate(folders):

	for filename in glob.glob(fol):
		filename_onlyName = filename.split('\\')[-1]
		print(filename_onlyName)
		img = cv2.imread(filename)
		im_neg = cv2.bitwise_not(img)
		print(outputPath + filename_onlyName)
		cv2.imwrite(outputPath + filename_onlyName, im_neg)