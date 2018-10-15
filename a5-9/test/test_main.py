'''
Created on Nov 6, 2017

@author: Tudor
'''
import unittest
from test_domain import test_entities
from test_repository import test_repository

all_suites = unittest.TestSuite([test_entities.suite(), test_repository.suite()])

if __name__ == '__main__':
    tests = unittest.TextTestRunner()
    tests.run(all_suites)