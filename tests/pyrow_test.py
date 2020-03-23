from ../src import pyrow 
import unittest


class TestMyClass(unittest.TestCase):

    def test_something_cool(self):
        self.assertEqual(False, True)

if __name__ == '__main__':
    unittest.main()