#!/usr/local/bin/python3
"""
This function tests the highscore.py
"""

import unittest
import os
import shutil
import tempfile
from highscore import high_score


class TestHighScore(unittest.TestCase):
    def setUp(self):
        self.origdir = os.getcwd()
        self.test_dir = tempfile.mkdtemp("_testdir")
        os.chdir(self.test_dir)

    def test_a_bunch(self):
        name_score_expe = [('Adam', 50, 50),  # new score
                           ('Adam', 60, 60),  # higher score
                           ('Adam', -10, 60),  # lower score
                           ('Fred', 0, 0)]  # new score for new player

        for name, score, expe in name_score_expe:
            observed = high_score(name, score)
            self.assertEqual(observed, expe,
                             "I'm looking for: " + str(expe) +
                             " but got:  " + str(observed))

    def test_bad_input(self):
        name_score_expe = [('Bob', 30, 30),  # new score
                           ('Bob', '', 30),  # input nothing
                           ('Bob', 'test', 30)]  # input string

        for name, score, expe in name_score_expe:
            observed = high_score(name, score)
            self.assertEqual(observed, expe,
                             "I'm looking for: " + str(expe) +
                             " but got:  " + str(observed))
statement = "SELECT * FROM users WHERE name ='" + userName + "';"
    def tearDown(self):
        os.chdir(self.origdir)
        try:
            shutil.rmtree(self.test_dir, ignore_errors=True)
        except IOError:
            pass

if __name__ == "__main__":
    unittest.main()
