#!/usr/local/bin/python
"""
Unit test for fileTypeCount(), including:
1. file only case
2. folder only case
3. file&folder combination case
"""

import unittest
import os
import tempfile
from Filetype_count import fileTypeCount
import shutil


class TestFileTypeCount(unittest.TestCase):
    def setUp(self):
        self.origdir = os.getcwd()
        self.test_dir = tempfile.mkdtemp("_testdir")
        os.chdir(self.test_dir)

    def create_basic_file(self):
        open("test.doc", 'w').close()
        open("test.ext", 'w').close()
        open("test.1", 'w').close()
        open("test._", 'w').close()
        open("test", 'w').close()

    def create_basic_folder(self):
        path1 = os.path.join(self.test_dir, 'temp1')
        path2 = os.path.join(self.test_dir, 'temp1.testdir')
        path3 = os.path.join(self.test_dir, 'temp1.  ')
        if not os.path.exists(path1): os.makedirs(path1)
        if not os.path.exists(path2): os.makedirs(path2)
        if not os.path.exists(path1): os.makedirs(path3)

    def test_file_only(self):
        self.create_basic_file()
        ext_dict = fileTypeCount(self.test_dir)
        expected_file_only = {'.doc': 1, '.ext': 1, '.1': 1, '._': 1, ' ': 1}
        self.assertEqual(expected_file_only, ext_dict)

    def test_folder_only(self):
        self.create_basic_folder()
        ext_dict = fileTypeCount(self.test_dir)
        expected_folder_only = {}
        self.assertEqual(expected_folder_only, ext_dict)

    def test_file_folder_combo(self):
        self.create_basic_folder()
        self.create_basic_file()
        ext_dict = fileTypeCount(self.test_dir)
        expected_file_folder_combo = {'.doc': 1, '.ext': 1, '.1': 1, '._': 1, ' ': 1}
        self.assertEqual(expected_file_folder_combo, ext_dict)

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.test_dir)

if __name__ == "__main__":
    unittest.main()
