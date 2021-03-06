import unittest
import sys, os
sys.path.append("..")


file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_exception_revised.txt'

class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(file_path,"w"):
            pass

    def test_dummy_boundary_testcase(self):
        try:
            with open(file_path,"a") as f:
                f.write("TestDummyTestCase=True\n")
                print("TestDummyTestCase = Passed")
        except (ValueError,OutOfBoundaryMarksError):
            with open(file_path,"a") as f:
                f.write("TestDummyTestCase=False\n")
                print("TestDummyTestCase = Failed")