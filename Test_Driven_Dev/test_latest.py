#!/usr/local/bin/python
"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""

import unittest
import time

from Test_Driven_Dev import latest


class TestLatest(unittest.TestCase):
	def setUp(self):
		self.path = "E:\\Desktop\\"
		self.file_name = ["file.old", "file.bak", "file.new"]
		for file in self.file_name:
			f = open(file, 'w').close()
			time.sleep(0.1)

	def test_latest_no_number(self):
		"blablabla"
		expected = [self.path + "file.new"]
		test_latest = latest.latest(self.path)
		self.assertEqual(set(expected), set(test_latest)) 

	def test_latest_with_arg(self):
		"blablabla"
		expected = [self.path + "file.new", self.path + "file.bak"]
		test_latest = set(latest.latest(self.path, 2))
		self.assertEqual(set(expected), set(test_latest))

	# def tearDown(self):
	# 	for file in self.file_name:
	# 		os.remove(self.path + file)

if __name__ == "__main__":
	unittest.main()