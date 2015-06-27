#!/usr/local/bin/python
"""
Examine the contents of the current working directory and print out
a count of how many files have each extension (".txt", ".doc", etc.)
"""

import glob
import os

def fileTypeCount(path):
	ext_dict = {}
	file_list = [item for item in glob.glob(os.path.join(path,"*")) if os.path.isfile(item)]
	for file in file_list:
		ext = os.path.splitext(file)[1]
		if ext:
			ext_dict[ext] = ext_dict.get(ext, 0) + 1
		else:
			# in case for some file without any extention, use space for its key.
			ext_dict[' '] = ext_dict.get(' ', 0) + 1 

	print ("\nFile extention count for: %s" % path)
	for ext in sorted(ext_dict.keys()):
		if ext == ' ': 
			print ("No extention file => %s" % (ext_dict[ext]))
		else:
			print ("%s => %s" % (ext, ext_dict[ext]))

	return ext_dict


if __name__ == "__main__":
	fileTypeCount(r"E:\Desktop\python")