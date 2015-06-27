#!/usr/local/bin/python3
import glob
import os
import zipfile

def latest(path, num=1):

    sort_list = sorted(glob.glob(os.path.join(path, "*")), key=os.path.getmtime)
    latest_files=[os.path.abspath(item) for item in sort_list[-num:]]
    latest_files.reverse()
    return latest_files

def zip_latest(fn, num, path):
	files_to_zip = latest(path, num)
	zf = zipfile.ZipFile(fn, 'w', zipfile.ZIP_DEFLATED)
	for f in files_to_zip:
		zf.write(f, arcname = os.path.basename(f))
	zf.close()
	
	
if __name__ == "__main__":
	file_list = latest(os.getcwd(), 2)
	print (file_list)

