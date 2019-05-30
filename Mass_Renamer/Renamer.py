# Written by Guru Sarath
# 29 May 2019

import os

FolderPath = 'FolderX'
genericName_File = 'GenericFileName_'
genericName_Folder = 'GenericFoldername_'
i = 0 #File counter
j = 0 #Folder counter 

for x in os.listdir(FolderPath):

	splitX = x.split('.') #separate name and extension

	try:
		extension = '.' + splitX[1]
		os.rename('FolderX\\' + x, 'FolderX\\' + genericName_File + str(i) + extension)
		i += 1
	except:
		#Any file without an extension is considered a folder
		extension = ''
		os.rename('FolderX\\' + x, 'FolderX\\' + genericName_Folder + str(j) + extension)
		j += 1