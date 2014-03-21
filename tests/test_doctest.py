import unittest
import doctest
import servicelog

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(servicelog))
    return tests

