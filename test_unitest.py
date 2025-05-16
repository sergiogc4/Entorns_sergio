from estudio import *
import unittest

def suma(a,b):
    return a+b
class Testsuma(unittest.TestCase):
    def test_positius(self):
        self.assertEqual(suma(2,3),5)


if __name__=="__main__":
    unittest.main()