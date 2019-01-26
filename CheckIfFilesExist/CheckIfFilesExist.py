import os
import shutil
import argparse

parserX = argparse.ArgumentParser(description = 'Move the files listed in a *.txt file')
parserX.add_argument('-dest', help = 'Destionation dirrectory to look into.')
argsX = parserX.parse_args()


if not argsX.dest:
	destinationFolder = input('Enter the destination folder location :')
else:
	destinationFolder = argsX.dest


try:

	if not destinationFolder:
		destinationFolder = os.getcwd()

except:
	print('Something went wrong !')
	print('Nothing executed !')

else:

	print('--------------------------------------------------------------')
	print('Searching for files in Location : ' + destinationFolder)
	print('--------------------------------------------------------------')

	try:

		with open('FilesToCheck.txt','r') as FileListRef:

			fileContent = FileListRef.read()
			files = fileContent.split('\n')
			print(files)

			files_in_dest = os.listdir(destinationFolder)

			for fileX in files:
				if fileX in files_in_dest:
					print(fileX + ' is present ')
				else:
					print(fileX + ' is NOT present ####')

	except:
		print('Failed to open FilesToCheck.txt')
		print('Ensure that FilesToCheck.txt is present with list of files to check for')


input('\n\n\nPress enter key ... ')