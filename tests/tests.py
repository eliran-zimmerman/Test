import unittest
import sys


class Test(unittest.TestCase):
    def __init__(self, testName, path) -> None:
        super(Test, self).__init__(testName) 
        self.path = path

    def test_calc(self):
        test_dict = {}
        with open(self.path, "r") as f:
            data = f.readlines()
        for line in data:
            line_s = line.split(":")
            test_dict[line_s[0]] = line_s[1]
        self.assertEqual(float(test_dict["output"]), (float(test_dict["input"]) - 32) / 1.8, "Should be same")


path = sys.argv[1]
suite = unittest.TestSuite()
suite.addTest(Test('test_calc', path))
ret = unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
if not ret:
    raise Exception
