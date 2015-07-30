#!/usr/local/bin/python3
"""
This function zip all FILEs under the path into zip_me.zip.
This zip file doesn't include any subdirectory or files under the subdirectory
"""

import glob
import os
import zipfile


def zip_me(path):
    file_to_zip = [fn for fn in glob.glob(os.path.join(path, "*")) if os.path.isfile(fn)]
    zip_file = os.path.join(path, 'zip_me.zip')
    zf = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    for fn in file_to_zip:
        # This Zip file doesn't have full directory, only files themselves.
        zf.write(fn, arcname=os.path.join(os.path.basename(os.path.dirname(fn)),os.path.basename(fn)))

    zf.printdir()
    zf.close()


if __name__ == "__main__":
    #path = r'V:\workspace\Archives_Homework\src'
    path = r'E:\Desktop\python'
    if not os.path.exists(path):
        os.mkdir(path)
    zip_me(path)
