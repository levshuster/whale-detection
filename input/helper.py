import zipfile
import os
def unzip_file(filename, folder):
	if not os.path.exists(filename):
		print('File does not exist')
		return
	else :
		with zipfile.ZipFile(filename, 'r') as zip_ref:
			zip_ref.extractall(folder)
			print('File unzipped successfully')
