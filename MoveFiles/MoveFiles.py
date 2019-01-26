import os
import shutil
import random
import math
import argparse


parserX = argparse.ArgumentParser(description = 'Moves files given in MoveFiles_FilesList.txt file')
parserX.add_argument('-src', help='source directory')
parserX.add_argument('-dest', help='destination directory')
parserX.add_argument('-a', '--all', action='store_true', help = 'Copy all the files from source')
argsX = parserX.parse_args()

if not argsX.src and not argsX.all:
	sourceFolder = input('Enter the source folder location :')
else:
	sourceFolder = argsX.src


if not argsX.dest:
	destinationFolder = input('Enter the destination folder location :')
else:
	destinationFolder = argsX.dest


try:

	if not sourceFolder:
		sourceFolder = os.getcwd()

	if not destinationFolder:
		destinationFolder = os.getcwd() + '\\Moved_' + str(math.ceil(random.random() * 1000))
		os.mkdir(destinationFolder)

except:
	print('Something went wrong !')
	print('Nothing executed !')

else:

	print('--------------------------------------------------------------')

	print('Source Location : ' + sourceFolder)
	print('destination Location : ' + destinationFolder)

	print('--------------------------------------------------------------')

	try:


		if not argsX.all:
			with open('MoveFiles_FilesList.txt', 'r') as FileListRef:
				fileContent = FileListRef.read()
				files = fileContent.split('\n')
				print(files)

		elif argsX.all:
			print('Copying all the files')
			files = os.listdir()
			print(files)

		for fileX in files:
			
			print(' >>>>> Copying ' + fileX, end = '  ...  ')

			try:
				shutil.copyfile(sourceFolder + '\\' + fileX, destinationFolder + '\\' + fileX)
			except:
				print('###### failed ######')
			else:
				print('Completed :)')


	except (FileNotFoundError):
		print('MoveFiles_FilesList.txt File Not Found !!!')
		print('Create a MoveFiles_FilesList.txt file with all the files to be moved listed in it.')
	print('--------------------------------------------------------------')


	input('\n\n\nPress enter key ... ')
