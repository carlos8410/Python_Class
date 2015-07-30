#!/usr/local/bin/python3

import unittest
import os
import zipfile
import time
import shutil
import tempfile

from Test_Driven_Dev import zipme


class TestZipme(unittest.TestCase):
    
    def setUp(self):
        """
        Set up a test folder archive_test with directory tree shown as below:
        archive_test
        -- old    (file)
        -- newer  (file)
        -- newest (file)
        -- test_dir
            -- file_1.test (file)
            -- sub_dir
                -- file_2.test (file)
        """

        self.zip_path = tempfile.mkdtemp("_testdir")
        self.zip_filename = os.path.join(self.zip_path, 'zip_me.zip')
        
        self.file_names = ['old', 'newer', 'newest']
        for fn in self.file_names:
            open(os.path.join(self.zip_path, fn), 'w').close()
            time.sleep(0.1)
        os.mkdir(os.path.join(self.zip_path, 'test_dir'))
        os.mkdir(os.path.join(self.zip_path, 'test_dir', 'sub_dir'))
        open(os.path.join(self.zip_path, 'test_dir', 'file_1.test'),'w').close()
        open(os.path.join(self.zip_path, 'test_dir', 'sub_dir', 'file_2.test'),'w').close()
        time.sleep(0.1)

    def test_zipme(self):
        zipme.zip_me(self.zip_path)
        zf = zipfile.ZipFile(self.zip_filename)
        files_in_zip = zf.namelist()
        zf.close()
        #expected = set(self.file_names)
        expected = set()
        for item in self.file_names:
            #expected.add(os.path.join(os.path.basename(self.zip_path), item))
            expected.add(os.path.basename(self.zip_path) + '/' + item)
        #expected = set(os.path.join(os.path.basename(self.zip_path), self.file_names))
        print ('expected=', expected)
        observed = set(files_in_zip)
        self.assertEqual(observed, expected)

    def tearDown(self):
        os.remove(self.zip_filename)
        try:
            shutil.rmtree(self.zip_path, ignore_errors=True)
        except IOError:
            pass

if __name__ == "__main__":
    unittest.main()


